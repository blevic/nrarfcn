from nrarfcn.tables import tables_data

def get_frequency(nrarfcn: int) -> float:
    """Gets the frequency of a given NR-ARFCN, in MHz.

    Args:
        nrarfcn: The NR-ARFCN to get the frequency of.

    Returns:
        The frequency of the given NR-ARFCN, in MHz.

    Raises:
        ValueError: If the NR-ARFCN is not valid.
    """

    table = tables_data('freq_nrarfcn')

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