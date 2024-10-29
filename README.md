# Toshling - a Python client library for the Toshl API

Toshling is an(other) implementation of a client for the [Toshl API](https://developer.toshl.com/docs/).

## Installation

Toshling can be installed from the PyPI using `pip`:
```
pip install toshling
```

## Usage

All interaction with Toshl is done via the `Client` class, which is constructed with your API key:

```python
import toshling

client = toshling.Client('xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxxxxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx')
```

Namespaces and methods under the client generally match the [API documentation](https://developer.toshl.com/docs/). All arguments passed must be in `keyword=value` form. Due to some keywords being reserved or invalid in Python, some substitutes must be made. Examples are below:

```python
accounts = client.accounts.list()
groceries_category = client.categories.list(search='Groceries')[0]
everything_but_groceries = client.entries.list(account=accounts[0].id,
                                               from_='2020-12-01',
                                               to='2020-12-31', not_categories=groceries_category.id)
client.entries.create(amount=168.43,
                      currency={'code': 'AUD'},
                      date='2020-03-06',
                      desc='Toilet paper for COVID-19 end-of-days',
                      account=accounts[0].id,
                      category=groceries_category.id)

for entry in client.entries.iterate(accounts=account_id,
                                    from_='2020-01-01',
                                    to='2020-12-31'):
    # Process each of many entries, with pagination transparently handled
    ...
```

More details on the required argument types and their validation can be found in the `toshling.models.argument_types` and `toshling.models.return_types`.

## Issues

Toshling has numerous flaws, mostly due to the incomplete [JSON Hyper-Schema](https://json-schema.org/draft/2019-09/json-schema-hypermedia.html) documents provided by Toshl, which are inconsistent, based on an old draft spec and do not match their actual API documentation.

Ideally the full client would be automatically generated from the schemas, but that is not currently possible. Instead, as much functionality as possible was implemented in a semi-automated manner, with the expectation that edge cases will present themself in day-to-day usage.

Please feel free to submit issues for consideration on GitHub.

## Related libraries

- [toshl](https://pypi.org/project/toshl/) - a seemingly unmaintained API client missing some key features such as getting entries.
- [toshl-api](https://pypi.org/project/toshl-api/) - an autogenerated client without much documentation.