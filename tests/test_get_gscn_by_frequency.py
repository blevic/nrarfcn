import unittest
from nrarfcn import get_gscn_by_frequency


class TestGetGscnByFrequency(unittest.TestCase):
    def test_valid_freqs(self):
        gscn_freq_map = {
            2: 1.250,
            3: 1.350,
            4: 1.450,
            5: 2.450,
            6: 2.550,
            7: 2.650,
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
            self.assertEqual(get_gscn_by_frequency(freq), gscn)

    def test_different_freqs(self):
        different_freqs = [
            (1.250, 1.350),
            (1.280, 1.320),
            (1.299, 1.301),
            (1.450, 2.450),
            (1.550, 2.350),
            (1.650, 2.250),
            (1.750, 2.150),
            (1.850, 2.050),
            (1.910, 1.990),
            (1.940, 1.960),
            (2997.850, 2998.850),
            (2998.050, 2998.650),
            (2998.250, 2998.450),
            (2998.349, 2998.351),
            (3000.000, 3001.440),
            (3000.500, 3000.940),
            (3000.700, 3000.740),
            (3000.719, 3000.721),
            (24250.080, 24267.360),
            (24258.080, 24259.360),
            (24258.719, 24258.721),
        ]

        for freq1, freq2 in different_freqs:
            self.assertNotEqual(get_gscn_by_frequency(freq1), get_gscn_by_frequency(freq2))

    def test_invalid_freqs(self):
        invalid_freqs = [-1.0, -1, -0.01, 100000.01, 100001, 100001.0, None, '', '60000']

        for freq in invalid_freqs:
            with self.assertRaises(ValueError):
                get_gscn_by_frequency(freq)
