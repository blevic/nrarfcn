import unittest
from nrarfcn import get_duplex_mode


class TestGetDuplexMode(unittest.TestCase):
    def test_str_bands(self):
        fdd_bands = ['n1', 'n2', 'n3', 'n5', 'n7', 'n8', 'n12', 'n13', 'n14', 'n18', 'n20', 'n24', 'n25', 'n26', 'n28',
                     'n30', 'n65', 'n66', 'n70', 'n71', 'n74', 'n85', 'n91', 'n92', 'n93', 'n94', 'n100']
        tdd_bands = ['n34', 'n38', 'n39', 'n40', 'n41', 'n46', 'n48', 'n50', 'n51', 'n53', 'n77', 'n78', 'n79', 'n90',
                     'n96', 'n101', 'n102', 'n104', 'n257', 'n258', 'n259', 'n260', 'n261', 'n262', 'n263']
        sdl_bands = ['n29', 'n67', 'n75', 'n76']
        sul_bands = ['n80', 'n81', 'n82', 'n83', 'n84', 'n86', 'n89', 'n95', 'n97', 'n98', 'n99']

        mode_bands_map = {
            'FDD': fdd_bands,
            'TDD': tdd_bands,
            'SDL': sdl_bands,
            'SUL': sul_bands
        }

        for mode, bands in mode_bands_map.items():
            for band in bands:
                self.assertEqual(get_duplex_mode(band), mode)

    def test_int_bands(self):
        fdd_bands = [1, 2, 3, 5, 7, 8, 12, 13, 14, 18, 20, 24, 25, 26, 28, 30, 65, 66, 70, 71, 74, 85, 91, 92, 93, 94,
                     100]
        tdd_bands = [34, 38, 39, 40, 41, 46, 48, 50, 51, 53, 77, 78, 79, 90, 96, 101, 102, 104, 257, 258, 259, 260, 261,
                     262, 263]
        sdl_bands = [29, 67, 75, 76]
        sul_bands = [80, 81, 82, 83, 84, 86, 89, 95, 97, 98, 99]

        mode_bands_map = {
            'FDD': fdd_bands,
            'TDD': tdd_bands,
            'SDL': sdl_bands,
            'SUL': sul_bands
        }

        for mode, bands in mode_bands_map.items():
            for band in bands:
                self.assertEqual(get_duplex_mode(band), mode)

    def test_invalid_band(self):
        invalid_bands = ['n4', 4, 'n6', 6, 0, 1.0, -1, 'n0', 64, 256, 'n', '']

        for band in invalid_bands:
            with self.assertRaises(ValueError):
                get_duplex_mode(band)
