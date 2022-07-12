import unittest
from nrarfcn import get_frequency


class TestGetFrequency(unittest.TestCase):
    def test_valid_channels(self):
        channel_freq_table = [
            (0, 0.0),
            (599999, 2999.995),
            (600000, 3000.000),
            (2016666, 24249.990),
            (2016667, 24250.080),
            (3279165, 99999.960),
            (422000, 2110.000),
            (386000, 1930.000),
            (434000, 2170.000),
            (398000, 1990.000),
            (399000, 1995.000),
            (404000, 2020.000),
            (693334, 4400.010),
            (733332, 4999.980),
            (2016667, 24250.080),
            (2337499, 43500.000),
            (2054167, 26500.080)
        ]

        for channel, freq in channel_freq_table:
            self.assertAlmostEqual(get_frequency(channel), freq, places=3)

    def test_different_channels(self):
        different_channels = [
            (0, 1),
            (599999, 600000),
            (600000, 600001),
            (2016666, 2016667),
            (2016667, 2016668)
        ]

        for c1, c2 in different_channels:
            self.assertNotAlmostEqual(get_frequency(c1), get_frequency(c2), places=3)

    def test_invalid_channels(self):
        invalid_channels = [-1, 3279166, 1.0, None, '', '600000']

        for channel in invalid_channels:
            with self.assertRaises(ValueError):
                get_frequency(channel)
