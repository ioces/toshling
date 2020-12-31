from . import endpoints
import requests

class Client:
    def __init__(self, api_key, api_endpoint_base='https://api2.toshl.com'):
        self.api_key = api_key
        self.api_endpoint_base = api_endpoint_base

        self.accounts = endpoints.Accounts(self)
        self.budgets = None
        self.categories = None
        self.currencies = None
        self.entries = None
        self.exports = None
        self.images = None
        self.me = endpoints.Me(self)
        self.tags = None
    
    def get(self, path):
        response = requests.get(self.api_endpoint_base + path, auth=(self.api_key, ''))
        return response.json()