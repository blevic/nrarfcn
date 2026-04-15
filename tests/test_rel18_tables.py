import unittest

from nrarfcn import get_duplex_mode, get_frequency_range, get_gscn_range, get_nrarfcn_range


class TestRel18Tables(unittest.TestCase):
    def test_new_fr1_operating_bands(self):
        self.assertEqual(get_duplex_mode('n109', release_3gpp=18), 'FDD')
        self.assertEqual(get_frequency_range('n109', release_3gpp=18), (1432, 1517))

    def test_new_fr1_nrarfcn_ranges(self):
        self.assertEqual(get_nrarfcn_range('n109', release_3gpp=18), (286400, 303400))

    def test_new_fr1_ss_raster_ranges(self):
        self.assertEqual(get_gscn_range('n105', release_3gpp=18), (1535, 1624))
        self.assertEqual(get_gscn_range('n109', release_3gpp=18), (3584, 3787))
