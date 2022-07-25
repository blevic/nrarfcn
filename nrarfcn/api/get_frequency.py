from nrarfcn.tables.freq_nrarfcn import table_freq_nrarfcn


def get_frequency(nrarfcn: int) -> float:
    """Gets the frequency of a given NR-ARFCN, in MHz.

    Args:
        nrarfcn: The NR-ARFCN to get the frequency of.

    Returns:
        The frequency of the given NR-ARFCN, in MHz.

    Raises:
        ValueError: If the NR-ARFCN is not valid.
    """

    table = table_freq_nrarfcn()

    if not isinstance(nrarfcn, int):
        raise ValueError('NR-ARFCN must be an integer.')

    if nrarfcn < 0 or nrarfcn > 3_279_165:
        raise ValueError('NR-ARFCN must be between 0 and 3,279,165.')

    for row in table.data:
        if table.get_cell(row, 'n_ref_min') <= nrarfcn <= table.get_cell(row, 'n_ref_max'):
            f_offset = int(table.get_cell(row, 'f_ref_offs') * 1000)
            delta_f = table.get_cell(row, 'df_global')
            n_offset = table.get_cell(row, 'n_ref_offs')
            freq_khz = f_offset + delta_f * (nrarfcn - n_offset)
            freq_mhz = freq_khz / 1000
            return round(freq_mhz, 3)

    raise ValueError('NR-ARFCN is not valid.')
