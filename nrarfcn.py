class Table:
    def __init__(self, name: str, header: list, data: list):
        self.name = name
        self.header = header
        self.data = data

    def get_cell(self, row: list, key: str):
        idx = self.header.index(key)
        return row[idx]

def get_frequency(nrarfcn: int) -> float:
    """Gets the frequency of a given NR-ARFCN, in MHz.

    Args:
        nrarfcn: The NR-ARFCN to get the frequency of.

    Returns:
        The frequency of the given NR-ARFCN, in MHz.

    Raises:
        ValueError: If the NR-ARFCN is not valid.
    """

    table_name = "Table 5.4.2.1-1: NR-ARFCN parameters for the global frequency raster"
    table_header = ['F_min_MHz', 'F_max_MHz', 'DF_global_kHz', 'Fref_offs_MHz', 'Nref_offs', 'Nref_min', 'Nref_max']
    table_data = [
        [0,      3_000,   5,  0,         0,         0,         599_999],
        [3_000,  24_250,  15, 3_000,     600_000,   600_000,   2_016_666],
        [24_250, 100_000, 60, 24_250.08, 2_016_667, 2_016_667, 3_279_165]
    ]

    table = Table(table_name, table_header, table_data)

    if type(nrarfcn) is not int:
        raise ValueError('NR-ARFCN must be an integer.')

    if nrarfcn < 0 or nrarfcn > 3_279_165:
        raise ValueError('NR-ARFCN must be between 0 and 3,279,165.')

    for row in table.data:
        if table.get_cell(row, 'Nref_min') <= nrarfcn <= table.get_cell(row, 'Nref_max'):
            freq_kHz = int(table.get_cell(row, 'Fref_offs_MHz') * 1000) \
                       + table.get_cell(row, 'DF_global_kHz') * (nrarfcn - table.get_cell(row, 'Nref_offs'))
            freq_MHz = freq_kHz / 1000
            return freq_MHz

    raise ValueError('NR-ARFCN is not valid.')
