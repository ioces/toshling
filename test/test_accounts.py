import unittest
import toshling


class TestAccounts(unittest.TestCase):
    def setUp(self):
        with open('API_KEY') as api_key_file:
            self.client = toshling.Client(api_key_file.read())
    
    def test_list(self):
        for account in self.client.accounts.list():
            self.assertIsInstance(account, toshling.models.return_types.Account)


if __name__ == '__main__':
    unittest.main()