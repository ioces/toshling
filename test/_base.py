import unittest
import toshling
import pathlib


class ApiTestCase(unittest.TestCase):
    def setUp(self):
        api_key_file_path = pathlib.Path(__file__).parent.resolve() / 'API_KEY'
        with open(api_key_file_path) as api_key_file:
            self.client = toshling.Client(api_key_file.read())
