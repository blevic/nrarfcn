import unittest
from nrarfcn import get_band_duplex_mode


class TestGetBandDuplexMode(unittest.TestCase):
    def test_str_bands(self):
        str_bands_duplex_mode = {
            'n1': 'FDD',
            'n2': 'FDD',
            'n3': 'FDD',
            'n5': 'FDD',
            'n7': 'FDD',
            'n8': 'FDD',
            'n12': 'FDD',
            'n14': 'FDD',
            'n18': 'FDD',
            'n20': 'FDD',
            'n25': 'FDD',
            'n26': 'FDD',
            'n28': 'FDD',
            'n29': 'SDL',
            'n30': 'FDD',
            'n34': 'TDD',
            'n38': 'TDD',
            'n39': 'TDD',
            'n40': 'TDD',
            'n41': 'TDD',
            'n48': 'TDD',
            'n50': 'TDD',
            'n51': 'TDD',
            'n53': 'TDD',
            'n65': 'FDD',
            'n66': 'FDD',
            'n70': 'FDD',
            'n71': 'FDD',
            'n74': 'FDD',
            'n75': 'SDL',
            'n76': 'SDL',
            'n77': 'TDD',
            'n78': 'TDD',
            'n79': 'TDD',
            'n80': 'SUL',
            'n81': 'SUL',
            'n82': 'SUL',
            'n83': 'SUL',
            'n84': 'SUL',
            'n86': 'SUL',
            'n89': 'SUL',
            'n90': 'TDD',
            'n91': 'FDD',
            'n92': 'FDD',
            'n93': 'FDD',
            'n94': 'FDD',
            'n95': 'SUL',
            'n257': 'TDD',
            'n258': 'TDD',
            'n259': 'TDD',
            'n260': 'TDD',
            'n261': 'TDD'
        }

        for band, duplex_mode in str_bands_duplex_mode.items():
            self.assertEqual(get_band_duplex_mode(band), duplex_mode)

    def test_int_bands(self):
        int_bands_duplex_mode = {
            1: 'FDD',
            2: 'FDD',
            3: 'FDD',
            5: 'FDD',
            7: 'FDD',
            8: 'FDD',
            12: 'FDD',
            14: 'FDD',
            18: 'FDD',
            20: 'FDD',
            25: 'FDD',
            26: 'FDD',
            28: 'FDD',
            29: 'SDL',
            30: 'FDD',
            34: 'TDD',
            38: 'TDD',
            39: 'TDD',
            40: 'TDD',
            41: 'TDD',
            48: 'TDD',
            50: 'TDD',
            51: 'TDD',
            53: 'TDD',
            65: 'FDD',
            66: 'FDD',
            70: 'FDD',
            71: 'FDD',
            74: 'FDD',
            75: 'SDL',
            76: 'SDL',
            77: 'TDD',
            78: 'TDD',
            79: 'TDD',
            80: 'SUL',
            81: 'SUL',
            82: 'SUL',
            83: 'SUL',
            84: 'SUL',
            86: 'SUL',
            89: 'SUL',
            90: 'TDD',
            91: 'FDD',
            92: 'FDD',
            93: 'FDD',
            94: 'FDD',
            95: 'SUL',
            257: 'TDD',
            258: 'TDD',
            259: 'TDD',
            260: 'TDD',
            261: 'TDD'
        }

        for band, duplex_mode in int_bands_duplex_mode.items():
            self.assertEqual(get_band_duplex_mode(band), duplex_mode)

    def test_invalid_band(self):
        invalid_bands = [
            'n4',
            4,
            'n6',
            6,
            0,
            1.0,
            -1,
            'n0',
            64,
            256,
            'n',
            ''
        ]

        for band in invalid_bands:
            with self.assertRaises(ValueError):
                get_band_duplex_mode(band)