import unittest

from nrarfcn import (
    get_band_by_lte_earfcn,
    get_duplex_mode,
    get_frequency_by_lte_earfcn,
    get_frequency_range,
    get_lte_bands_by_frequency,
    get_lte_earfcn_by_frequency,
    get_lte_earfcn_range,
)
from nrarfcn.tables import get_table


class TestLteApi(unittest.TestCase):
    def test_get_frequency_by_lte_earfcn(self):
        earfcn_freq_table = [
            (0, 2110.0),
            (300, 2140.0),
            (599, 2169.9),
            (18000, 1920.0),
            (26040, 1850.0),
            (66436, 2110.0),
            (134342, 1800.0),
            (74866, 606.0),
        ]

        for earfcn, frequency in earfcn_freq_table:
            self.assertEqual(get_frequency_by_lte_earfcn(earfcn), frequency)

    def test_get_lte_earfcn_by_frequency(self):
        self.assertEqual(get_lte_earfcn_by_frequency(2140.0), [300, 2250, 4450, 65836, 66736])
        self.assertEqual(get_lte_earfcn_by_frequency(1850.0), [1650, 3851, 18600, 26040, 36350])
        self.assertEqual(get_lte_earfcn_by_frequency(0), [])

    def test_get_lte_bands_by_frequency(self):
        self.assertEqual(get_lte_bands_by_frequency(1850.0), ['B2', 'B3', 'B9', 'B25', 'B35'])
        self.assertEqual(get_lte_bands_by_frequency(2140.0), ['B1', 'B4', 'B10', 'B65', 'B66'])
        self.assertEqual(get_lte_bands_by_frequency(0), [])

    def test_get_band_by_lte_earfcn(self):
        self.assertEqual(get_band_by_lte_earfcn(300), 'B1')
        self.assertEqual(get_band_by_lte_earfcn(26040), 'B25')
        self.assertEqual(get_band_by_lte_earfcn(66736), 'B66')
        self.assertEqual(get_band_by_lte_earfcn(74866), 'B113')

    def test_get_lte_earfcn_range(self):
        self.assertEqual(get_lte_earfcn_range('B25'), (8040, 8689))
        self.assertEqual(get_lte_earfcn_range('B25', direction='ul'), (26040, 26689))
        self.assertEqual(get_lte_earfcn_range(25, direction='ul'), (26040, 26689))
        self.assertEqual(get_lte_earfcn_range('B75', direction='ul'), ('N/A', 'N/A'))

    def test_shared_band_apis_route_lte_bands(self):
        self.assertEqual(get_duplex_mode('B66'), 'FDD')
        self.assertEqual(get_duplex_mode('B46'), 'TDD')
        self.assertEqual(get_duplex_mode('B107'), 'SDO')
        self.assertEqual(get_frequency_range('B66', direction='dl'), (2110, 2200))
        self.assertEqual(get_frequency_range('B66', direction='ul'), (1710, 1780))
        self.assertEqual(get_frequency_range('B75', direction='ul'), ('N/A', 'N/A'))

    def test_lte_uses_rel19_by_default(self):
        self.assertEqual(get_frequency_range('B1'), (2110, 2170))

        with self.assertRaises(ValueError):
            get_lte_earfcn_range('B1', release_3gpp=17)

        with self.assertRaises(ValueError):
            get_frequency_range('B1', release_3gpp=17)

    def test_lte_tables_load(self):
        bands = get_table('lte_bands', 19)
        earfcns = get_table('lte_earfcn', 19)

        self.assertEqual(bands.id, 'lte_bands')
        self.assertEqual(earfcns.id, 'lte_earfcn')
        self.assertEqual(len(bands.data), 73)
        self.assertEqual(len(earfcns.data), 73)

    def test_invalid_lte_inputs(self):
        invalid_earfcns = [-1, 262144, 262143, 1.0, None, '', '300']
        for earfcn in invalid_earfcns:
            with self.assertRaises(ValueError):
                get_frequency_by_lte_earfcn(earfcn)
            with self.assertRaises(ValueError):
                get_band_by_lte_earfcn(earfcn)

        invalid_freqs = [-1.0, -1, 100000.01, None, '', '2140']
        for frequency in invalid_freqs:
            with self.assertRaises(ValueError):
                get_lte_earfcn_by_frequency(frequency)
            with self.assertRaises(ValueError):
                get_lte_bands_by_frequency(frequency)

        invalid_bands = ['B15', 'B16', 'B0', 'B999', 'B', '', 1.0, None]
        for band in invalid_bands:
            with self.assertRaises(ValueError):
                get_lte_earfcn_range(band)

        with self.assertRaises(ValueError):
            get_lte_earfcn_range('B1', direction='sideways')
