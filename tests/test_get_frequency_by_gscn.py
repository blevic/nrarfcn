import unittest
from nrarfcn import get_frequency_by_gscn


class TestGetFrequencyByGscn(unittest.TestCase):
    def test_valid_channels(self):
        gscn_freq_map = {
            2: 1.250,
            500: 200.450,
            1000: 399.850,
            5000: 2000.450,
            7498: 2999.050,
            7499: 3000.000,
            10000: 6601.440,
            15000: 13801.440,
            20000: 21001.440,
            22255: 24248.640,
            22256: 24250.080,
            23000: 37106.400,
            25000: 71666.400,
            26639: 99988.320
        }

        for gscn, freq in gscn_freq_map.items():
            self.assertAlmostEqual(get_frequency_by_gscn(gscn), freq, places=3)

    def test_different_channels(self):
        different_channels = [
            (2, 3),
            (500, 501),
            (1000, 1001),
            (7498, 7499),
            (22255, 22256),
            (22256, 22257),
            (23000, 23001),
            (25000, 25001)
        ]

        for gscn1, gscn2 in different_channels:
            self.assertNotAlmostEqual(get_frequency_by_gscn(gscn1), get_frequency_by_gscn(gscn2), places=3)

    def test_invalid_channels(self):
        invalid_channels = [-1, 0, 1, 2.0, 23000.5, None, '', '2', 26640]

        for channel in invalid_channels:
            with self.assertRaises(ValueError):
                get_frequency_by_gscn(channel)
