from ._base import ApiTestCase
import toshling


class TestAccounts(ApiTestCase):
    def test_list(self):
        for account in self.client.accounts.list():
            self.assertIsInstance(account, toshling.models.return_types.Account)
