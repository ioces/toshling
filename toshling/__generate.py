import requests
import pathlib
import shutil
import json
import pprint
import models.return_types
from jinja2 import Template
import statham.schema.parser
import statham.serializers.python
from json_ref_dict import materialize, RefDict
from statham.titles import title_labeller


API_SCHEMA = "https://api2.toshl.com/schema/"
SCHEMAS = [
    "user",
    "notification",
    "notification.list",
    # summary (no profile="..." listed at GET /me/summary)
    # setting (/me/settings returns profile="https://api2.toshl.com/schema/user")
    # device (/me/devices returns profile="https://api2.toshl.com/schema/user")
    # app (/me/apps returns profile="https://api2.toshl.com/schema/user")
    # payment (/me/payments returns profile="https://api2.toshl.com/schema/payment.list", but that doesn't exist. There seems to be a "Payment" model in the user schema, though?)
    # promos (/me/promos/foo returns profile="https://api2.toshl.com/schema/promos", but that doesn't exist)
    # shares (/me/shares returns profile="https://api2.toshl.com/schema/shares", but that doesn't exist)
    # steps (/me/steps returns profile="https://api2.toshl.com/schema/step.list", but that doesn't exist)
    # reports (no profile="..." listed at GET /reports)
    "account",
    "account.list",
    "repeat",
    # institutions (/institutions returns profile="https://api2.toshl.com/schema/institution.list", but that doesn't exist)
    # countries (/bank/countries returns profile="https://api2.toshl.com/schema/institution.country.list", but that doesn't exist)
    # connections (/bank/connections returns profile="https://api2.toshl.com/schema/connection.list", but that doesn't exist)
    # imports (/bank/imports returns profile="https://api2.toshl.com/schema/import.list", but that doesn't exist)
    # planning (/planning returns profile="https://api2.toshl.com/schema/planning", but that doesn't exist)
    "entry",
    "entry.list",
    "entry.sum",
    "entry.sum.list",
    "location",
    "location.list",
    #"review",
    #"review.list"
    #"entries.timeline",
    #"entries.timeline.list",
    "budget",
    "budget.list",
    "category",
    "category.list",
    "category.sum",
    "category.sum.list",
    "tag",
    "tag.list",
    "tag.sum",
    "tag.sum.list",
    "currency",
    "export",
    "export.list",
    "image"
]


def fix(obj):
    # Upgrade number/integer property ranges to JSON Schema draft 07 spec (statham doesn't like the old booleans)
    type_ = obj.get("type", None)
    if type_ == "number" or type_ == "integer":
        if "exclusiveMinimum" in obj:
            if obj["exclusiveMinimum"]:
                obj["exclusiveMinimum"] = obj["minimum"]
                del obj["minimum"]
            else:
                del obj["exclusiveMinimum"]
        
        if "exclusiveMaximum" in obj:
            if obj["exclusiveMaximum"]:
                obj["exclusiveMaximum"] = obj["maximum"]
                del obj["maximum"]
            else:
                del obj["exclusiveMaximum"]
    
    # Replace type of 'date' (which is invalid)
    if type_ == "date":
        obj["type"] = "string"
        obj["format"] = "date"
    
    # Retitle objects to their original Java names, because the others are not unique
    if type_ == "object" and "javaType" in obj:
        obj["title"] = obj['javaType'].split('.')[-1]
    
    return obj


# Clean up previous runs of the script
shutil.rmtree('schemas/', ignore_errors=True)

# Make somewhere to store original schemas
original_schema_path = pathlib.Path('schemas/original/')
original_schema_path.mkdir(parents=True, exist_ok=True)

# Get schemas
for schema_path in SCHEMAS:
    response = requests.get(API_SCHEMA + schema_path)
    if response.ok:
        schema = response.text
        with original_schema_path.joinpath(schema_path + '.json').open('w') as f:
            f.write(schema)

# Make somewhere to generate fixed schemas
fixed_schema_path = pathlib.Path('schemas/fixed')
fixed_schema_path.mkdir(parents=True, exist_ok=True)

# Create a dummy item.json for the fixed schemas
with fixed_schema_path.joinpath('item.json').open('w') as f:
    item = {"type": "object", "properties": {}, "description": "A dummy Item, because Toshl devs decided to not include item.json"}
    json.dump(item, f, sort_keys=True, indent=4)

# Fix all of the schemas, and while we're at it, create a top level object with definitions for all schemas.
top = {"definitions": {}}
for original_schema_file_path in original_schema_path.glob('*.json'):
    top["definitions"][original_schema_file_path.stem] = {"$ref": f"{original_schema_file_path.name}#"}

    fixed = None
    with original_schema_file_path.open() as f:
        fixed = json.load(f, object_hook=fix)

    with fixed_schema_path.joinpath(original_schema_file_path.name).open('w') as f:
        json.dump(fixed, f, sort_keys=True, indent=4)

with fixed_schema_path.joinpath('top.json').open('w') as f:
    json.dump(top, f, sort_keys=True, indent=4)

# Convert the JSON schemas into Python objects using statham. These
# form our return types.
schema = materialize(RefDict(str(fixed_schema_path.joinpath('top.json'))), context_labeller=title_labeller())
returns = statham.schema.parser.parse(schema)
with open('models/return_types.py', 'w') as f:
    f.write(statham.serializers.python.serialize_python(*returns))

# Iterate the LDOs from all schemas, with the aim of automatically discovering all API
# methods
api_methods = []
for n, s in schema['definitions'].items():
    # Get links (handle the extra crap statham puts into the definitions object)
    links = []
    try:
        links = s.get("links", [])
    except Exception:
        pass

    for link in links:
        href = link["href"]

        method = link.get("method", "GET")
        
        crumbs = [crumb.split('?')[0] for crumb in href.split('/') if crumb and crumb[0] != "{"]
        crumbs.append(link["rel"])
        if crumbs[-1] == "self":
            crumbs[-1] = "get"
        if crumbs[-1] == crumbs[-2]:
            crumbs = crumbs[:-1]
        
        # Get the argument type.
        argument = None
        if "schema" in link:
            # Sub in a sensible title and parse the argument structure.
            link["schema"]["title"] = '.'.join(crumbs + ["argument"])
            argument = statham.schema.parser.parse_element(link['schema'])

            # Toshl uses `!attribute` a bunch, which statham turns into `exclamation_mark_attribute`. Change these to `not_attribute`
            negated_keys = [key for key in argument.properties if key[:16] == "exclamation_mark"]
            for negated_key in negated_keys:
                argument.properties["not" + negated_key[16:]] = argument.properties.pop(negated_key)
        
        # Try guess some return types.
        return_ = None
        if crumbs[-1] in {'get', 'list', 'update'}:
            guesses = []
            
            guesses.append(s['title'])

            class_parts = [p.capitalize() for p in n.split('.')]
            if class_parts[-1] in {'List'}:
                class_parts = class_parts[:-1]
            guesses.append(''.join(class_parts))

            for guess in guesses:
                try:
                    return_ = getattr(models.return_types, guess)
                    break
                except Exception as e:
                    pass

        api_methods.append((tuple(crumbs), method, href, argument, return_))

# Toshl has a lot of duplicate method/endpoint pairs, lots of which are invalid. We
# will take only those with the longest crumbs (which usually means there is a verb on the end).
# Also discard/modify/add methods we know need modifying.
discard = {
    ('accounts', 'account'),
    ('budgets', 'budget'),
    ('categories', 'category'),
    ('entries', 'entry'),
    ('entries', 'locations', 'location'),
    ('entries', 'transactions'),
    ('entries', 'transactions', 'repeats', 'repeating transactions'),
    ('entries', 'transaction_pair'),
    ('months', 'month')
}
modify = {

}
add = {

}
seen = set()
filtered_api_methods = {}
for crumbs, method, href, arg, ret in sorted(api_methods, key=lambda x: (x[2].split('?')[0], x[1], -len(x[0]))):
    key = (href.split('?')[0], method)
    if key not in seen and crumbs not in discard:
        api_method = {'method': method, 'href': href, 'argument': arg, 'return': ret}
        api_method.update(modify.get(crumbs, {}))
        filtered_api_methods[crumbs] = api_method
    seen.add(key)
filtered_api_methods.update(add)
filtered_api_methods = dict(sorted(filtered_api_methods.items(), key=lambda x: x[0][:-1]))

#pprint.pprint(filtered_api_methods, sort_dicts=False)

# Write the argument models Python module.
with open('models/argument_types.py', 'w') as f:
    arguments = (api_method['argument'] for api_method in filtered_api_methods.values() if api_method['argument'])
    f.write(statham.serializers.python.serialize_python(*arguments))

# Automatically generate Python code for the endpoints.
classes = []
subclasses = []
prev_length = 0
for crumbs, api_method in reversed(filtered_api_methods.items()):
    classname = ''.join(n.capitalize() for n in crumbs[:-1])
    if not classes or classname != classes[-1]['name']:
        class_ = {'name': classname, 'methods': []}
        if len(crumbs) < prev_length:
            if prev_length - len(crumbs) > 1:
                raise RuntimeError("We don't handle intermediate paths yet.")
            class_['subclasses'] = subclasses
            subclasses = [(crumbs[-2], classname)]
        elif len(crumbs) > prev_length:
            subclasses = [(crumbs[-2], classname)]
        elif len(crumbs) == prev_length:
            subclasses.append((crumbs[-2], classname))
        classes.append(class_)
        prev_length = len(crumbs)

    method = {'name': crumbs[-1]}
    method.update(api_method)
    classes[-1]['methods'].append(method)

with open('_endpoints.py.tmpl') as tf, open('_endpoints.py', 'w') as ef:
    template = Template(tf.read())
    ef.write(template.render(classes=classes))