import unittest
from .nrarfcn import get_frequency, get_nrarfcn


class TestNrarfcn(unittest.TestCase):
    def test_get_frequency(self):
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

        different_channels = [
            (0, 1),
            (599999, 600000),
            (600000, 600001),
            (2016666, 2016667),
            (2016667, 2016668)
        ]

        for c1, c2 in different_channels:
            self.assertNotAlmostEqual(get_frequency(c1), get_frequency(c2), places=3)

        invalid_channels = [
            -1,
            3279166,
            1.0,
            None,
            '',
            '600000'
        ]

        for channel in invalid_channels:
            with self.assertRaises(ValueError):
                get_frequency(channel)


    def test_get_nrarfcn(self):
        freq_channel_table = [
            (0.0, 0),
            (2999.995, 599999),
            (3000.000, 600000),
            (24249.990, 2016666),
            (24250.080, 2016667),
            (99999.960, 3279165),
            (100000.0, 3279165),
            (2110.000, 422000),
            (1930.000, 386000),
            (2170.000, 434000),
            (1990.000, 398000),
            (1995.000, 399000),
            (2020.000, 404000),
            (4400.010, 693334),
            (4999.980, 733332),
            (24250.080, 2016667),
            (43500.000, 2337499),
            (26500.080, 2054167),
            (0, 0),
            (3000, 600000),
            (100000, 3279165),
            (2110, 422000),
            (1930, 386000),
            (2170, 434000),
            (1990, 398000),
            (1995, 399000),
            (2020, 404000),
            (43500, 2337499)
        ]

        for freq, channel in freq_channel_table:
            self.assertEqual(get_nrarfcn(freq), channel)

        different_freqs = [
            (0.0, 0.005),
            (2999.995, 3000.000),
            (3000.000, 3000.015),
            (24249.990, 24250.080),
            (24250.080, 24250.140)
        ]

        for f1, f2 in different_freqs:
            self.assertNotEqual(get_nrarfcn(f1), get_nrarfcn(f2))

        invalid_freqs = [
            -1.0,
            -1,
            -0.01,
            100000.01,
            100001,
            100001.0,
            None,
            '',
            '60000'
        ]

        for freq in invalid_freqs:
            with self.assertRaises(ValueError):
                get_nrarfcn(freq)


if __name__ == '__main__':
    unittest.main()
