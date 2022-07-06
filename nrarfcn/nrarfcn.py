class Table:
    def __init__(self, id: str, name: str, header: list, data: list):
        self.id = id
        self.name = name
        self.header = header
        self.data = data

    def get_cell(self, row: list, key: str):
        idx = self.header.index(key)
        return row[idx]


def _tables_data(key: str) -> Table:
    table_id = 'freq_nrarfcn'
    table_name = "Table 5.4.2.1-1: NR-ARFCN parameters for the global frequency raster"
    table_header = ['F_min_MHz', 'F_max_MHz', 'DF_global_kHz', 'Fref_offs_MHz', 'Nref_offs', 'Nref_min', 'Nref_max']
    table_data = [
        [0, 3_000, 5, 0, 0, 0, 599_999],
        [3_000, 24_250, 15, 3_000, 600_000, 600_000, 2_016_666],
        [24_250, 100_000, 60, 24_250.08, 2_016_667, 2_016_667, 3_279_165]
    ]

    table_freq_nrarfcn = Table(table_id, table_name, table_header, table_data)

    table_id = 'bands_fr1'
    table_name = "Table 5.2-1: NR operating bands in FR1"
    table_header = ['Band', 'F_UL_low', 'F_UL_high', 'F_DL_low', 'F_DL_high', 'Duplex_mode']
    table_data = [
        ['n1', 1920, 1980, 2110, 2170, 'FDD'],
        ['n2', 1850, 1910, 1930, 1990, 'FDD'],
        ['n3', 1710, 1785, 1805, 1880, 'FDD'],
        ['n5', 824, 849, 869, 894, 'FDD'],
        ['n7', 2500, 2570, 2620, 2690, 'FDD'],
        ['n8', 880, 915, 925, 960, 'FDD'],
        ['n12', 699, 716, 729, 746, 'FDD'],
        ['n14', 788, 798, 758, 768, 'FDD'],
        ['n18', 815, 830, 860, 875, 'FDD'],
        ['n20', 832, 862, 791, 821, 'FDD'],
        ['n25', 1850, 1915, 1930, 1995, 'FDD'],
        ['n26', 814, 849, 859, 894, 'FDD'],
        ['n28', 703, 748, 758, 803, 'FDD'],
        ['n29', 'N/A', 'N/A', 717, 728, 'SDL'],
        ['n30', 2305, 2315, 2350, 2360, 'FDD'],
        ['n34', 2010, 2025, 2010, 2025, 'TDD'],
        ['n38', 2570, 2620, 2570, 2620, 'TDD'],
        ['n39', 1880, 1920, 1880, 1920, 'TDD'],
        ['n40', 2300, 2400, 2300, 2400, 'TDD'],
        ['n41', 2496, 2690, 2496, 2690, 'TDD'],
        ['n48', 3550, 3700, 3550, 3700, 'TDD'],
        ['n50', 1432, 1517, 1432, 1517, 'TDD'],
        ['n51', 1427, 1432, 1427, 1432, 'TDD'],
        ['n53', 2483.5, 2495, 2483.5, 2495, 'TDD'],
        ['n65', 1920, 2010, 2110, 2200, 'FDD'],
        ['n66', 1710, 1780, 2110, 2200, 'FDD'],
        ['n70', 1695, 1710, 1995, 2020, 'FDD'],
        ['n71', 663, 698, 617, 652, 'FDD'],
        ['n74', 1427, 1470, 1475, 1518, 'FDD'],
        ['n75', 'N/A', 'N/A', 1432, 1517, 'SDL'],
        ['n76', 'N/A', 'N/A', 1427, 1432, 'SDL'],
        ['n77', 3300, 4200, 3300, 4200, 'TDD'],
        ['n78', 3300, 3800, 3300, 3800, 'TDD'],
        ['n79', 4400, 5000, 4400, 5000, 'TDD'],
        ['n80', 1710, 1785, 'N/A', 'N/A', 'SUL'],
        ['n81', 880, 915, 'N/A', 'N/A', 'SUL'],
        ['n82', 832, 862, 'N/A', 'N/A', 'SUL'],
        ['n83', 703, 748, 'N/A', 'N/A', 'SUL'],
        ['n84', 1920, 1980, 'N/A', 'N/A', 'SUL'],
        ['n86', 1710, 1780, 'N/A', 'N/A', 'SUL'],
        ['n89', 824, 849, 'N/A', 'N/A', 'SUL'],
        ['n90', 2496, 2690, 2496, 2690, 'TDD'],
        ['n91', 832, 862, 1427, 1432, 'FDD'],
        ['n92', 832, 862, 1432, 1517, 'FDD'],
        ['n93', 880, 915, 1427, 1432, 'FDD'],
        ['n94', 880, 915, 1432, 1517, 'FDD'],
        ['n95', 2010, 2025, 'N/A', 'N/A', 'SUL']
    ]

    table_bands_fr1 = Table(table_id, table_name, table_header, table_data)

    table_id = 'bands_fr2'
    table_name = "Table 5.2-2: NR operating bands in FR2"
    table_header = ['Band', 'F_UL_low', 'F_UL_high', 'F_DL_low', 'F_DL_high', 'Duplex_mode']
    table_data = [
        ['n257', 26500, 29500, 26500, 29500, 'TDD'],
        ['n258', 24250, 27500, 24250, 27500, 'TDD'],
        ['n259', 39500, 43500, 39500, 43500, 'TDD'],
        ['n260', 37000, 40000, 37000, 40000, 'TDD'],
        ['n261', 27500, 28350, 27500, 28350, 'TDD']
    ]

    table_bands_fr2 = Table(table_id, table_name, table_header, table_data)

    tables = {
        'freq_nrarfcn': table_freq_nrarfcn,
        'bands_fr1': table_bands_fr1,
        'bands_fr2': table_bands_fr2
    }

    return tables.get(key)


def get_frequency(nrarfcn: int) -> float:
    """Gets the frequency of a given NR-ARFCN, in MHz.

    Args:
        nrarfcn: The NR-ARFCN to get the frequency of.

    Returns:
        The frequency of the given NR-ARFCN, in MHz.

    Raises:
        ValueError: If the NR-ARFCN is not valid.
    """

    table = _tables_data('freq_nrarfcn')

    if not isinstance(nrarfcn, int):
        raise ValueError('NR-ARFCN must be an integer.')

    if nrarfcn < 0 or nrarfcn > 3_279_165:
        raise ValueError('NR-ARFCN must be between 0 and 3,279,165.')

    for row in table.data:
        if table.get_cell(row, 'Nref_min') <= nrarfcn <= table.get_cell(row, 'Nref_max'):
            f_offset = int(table.get_cell(row, 'Fref_offs_MHz') * 1000)
            delta_f = table.get_cell(row, 'DF_global_kHz')
            n_offset = table.get_cell(row, 'Nref_offs')
            freq_khz = f_offset + delta_f * (nrarfcn - n_offset)
            freq_mhz = freq_khz / 1000
            return freq_mhz

    raise ValueError('NR-ARFCN is not valid.')


def get_nrarfcn(frequency: float) -> int:
    """Gets the NR-ARFCN of a given frequency in MHz.

    Args:
        frequency: The frequency to get the NR-ARFCN of, in MHz.

    Returns:
        The NR-ARFCN of the given frequency.

    Raises:
        ValueError: If the frequency is not valid.
    """

    table = _tables_data('freq_nrarfcn')

    if not isinstance(frequency, float) and not isinstance(frequency, int):
        raise ValueError('Frequency must be a float or an integer.')

    if frequency < 0 or frequency > 100_000:
        raise ValueError('Frequency must be between 0 and 100,000.')

    for row in table.data:
        if table.get_cell(row, 'F_min_MHz') <= frequency <= table.get_cell(row, 'F_max_MHz'):
            f_offset = table.get_cell(row, 'Fref_offs_MHz')
            delta_f = table.get_cell(row, 'DF_global_kHz')
            n_offset = table.get_cell(row, 'Nref_offs')
            nrarfcn = n_offset + (frequency - f_offset) * 1000. / delta_f
            return min(round(nrarfcn), 3_279_165)

    raise ValueError('Frequency is not valid.')
