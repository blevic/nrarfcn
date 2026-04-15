import unittest

from nrarfcn import get_frequency
from nrarfcn.tables import get_supported_releases, get_table


class TestTablesLoader(unittest.TestCase):
    def test_get_supported_releases(self):
        self.assertIn(17, get_supported_releases())
        self.assertIn(19, get_supported_releases())

    def test_get_table(self):
        table = get_table('bands_fr1', 17)

        self.assertEqual(table.id, 'bands_fr1')
        self.assertEqual(table.release_3gpp, 17)

        table = get_table('bands_fr1', 19)

        self.assertEqual(table.id, 'bands_fr1')
        self.assertEqual(table.release_3gpp, 19)

    def test_invalid_release(self):
        with self.assertRaises(ValueError):
            get_table('bands_fr1', 999)

    def test_api_release_argument(self):
        self.assertEqual(get_frequency(0, release_3gpp=17), 0.0)
        self.assertEqual(get_frequency(0, release_3gpp=19), 0.0)
