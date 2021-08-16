import json
import re

import requests
from statham.schema.constants import NotPassed
from statham.schema.elements import Object
from statham.schema.validation import format_checker

from . import _endpoints as endpoints


@format_checker.register("date")
def is_date(value: str) -> bool:
    return bool(re.match(r"\d{4}-\d{2}-\d{2}", value))


class StathamJSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, Object):
            return {type(o).properties[k].source: v for k, v in o._dict.items() if not isinstance(v, NotPassed)}
        
        return json.JSONEncoder.default(self, o)


class Client:
    def __init__(self, api_key, api_endpoint_base='https://api2.toshl.com'):
        self.api_key = api_key
        self.api_endpoint_base = api_endpoint_base

        self.accounts = endpoints.Accounts(self)
        self.budgets = endpoints.Budgets(self)
        self.categories = endpoints.Categories(self)
        self.currencies = endpoints.Currencies(self)
        self.entries = endpoints.Entries(self)
        self.exports = endpoints.Exports(self)
        self.images = endpoints.Images(self)
        self.me = endpoints.Me(self)
        self.tags = endpoints.Tags(self)
    
    def request(self, href, method, argument_type=None, return_type=None, **kwargs):
        options = {}

        if argument_type:
            # Remap kwargs (which are modified to avoid Python reserved keywords) back into
            # the source keys of the argument object.
            remap = {}
            for k, v in kwargs.items():
                remap[argument_type.properties[k].source] = v

            # Construct the argument, which will validate all kwargs.
            argument = argument_type(remap)

            # If we GET, use the original remap, otherwise, JSON encode the argument.
            if method == 'GET':
                options['params'] = remap
            else:
                options['data'] = json.dumps(argument, cls=StathamJSONEncoder)
                options['headers'] = {'Content-Type': 'application/json'}

        # Do the request.
        response = requests.request(method,
                                    self.api_endpoint_base + href.format(**kwargs),
                                    auth=(self.api_key, ''),
                                    **options)
        
        # Check if the response is OK.
        if response.ok:
            # Attempt to construct the return type, handling lists, and some
            # dicts especially (Toshl decided that on some endpoints such as
            # the currencies list that they'd actually return a dict).
            if return_type:
                plain = response.json()
                if isinstance(plain, list):
                    return [return_type(p) for p in plain]
                elif set(plain.keys()).issubset(set(p.source for p in return_type.properties.values())):
                    return return_type(response.json())
                elif isinstance(plain, dict):
                    return {k: return_type(v) for k, v in plain.items()}
                else:
                    return plain
        else:
            response.raise_for_status()
