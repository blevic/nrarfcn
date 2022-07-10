from nrarfcn.tables import tables_data

def get_nrarfcn(frequency: float) -> int:
    """Gets the NR-ARFCN of a given frequency in MHz.

    Args:
        frequency: The frequency to get the NR-ARFCN of, in MHz.

    Returns:
        The NR-ARFCN of the given frequency.

    Raises:
        ValueError: If the frequency is not valid.
    """

    table = tables_data('freq_nrarfcn')

    if not isinstance(frequency, float) and not isinstance(frequency, int):
        raise ValueError('Frequency must be a float or an integer.')

    if frequency < 0 or frequency > 100_000:
        raise ValueError('Frequency must be between 0 and 100,000 (MHz).')

    for row in table.data:
        if table.get_cell(row, 'F_min_MHz') <= frequency <= table.get_cell(row, 'F_max_MHz'):
            f_offset = table.get_cell(row, 'Fref_offs_MHz')
            delta_f = table.get_cell(row, 'DF_global_kHz')
            n_offset = table.get_cell(row, 'Nref_offs')
            nrarfcn = n_offset + (frequency - f_offset) * 1000. / delta_f
            return min(round(nrarfcn), 3_279_165)

    raise ValueError('Frequency is not valid.')
