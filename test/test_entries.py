from ._base import ApiTestCase
import toshling
from itertools import islice


class TestEntries(ApiTestCase):
    def test_iterate(self):
        entries = self.client.entries.iterate(
            from_='2020-01-01',
            to='2024-12-31',
            per_page=10)
        for entry in islice(entries, 50):
            self.assertIsInstance(entry, toshling.models.return_types.Entry)
