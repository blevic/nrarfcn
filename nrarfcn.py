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

    tables = {
        'freq_nrarfcn': table_freq_nrarfcn
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
