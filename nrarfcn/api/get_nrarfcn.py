from nrarfcn.tables import DEFAULT_RELEASE, get_table


def get_nrarfcn(frequency: float, release_3gpp: int = DEFAULT_RELEASE) -> int:
    """Gets the NR-ARFCN of a given frequency in MHz.

    Args:
        frequency: The frequency to get the NR-ARFCN of, in MHz.
        release_3gpp: The 3GPP release to use for table lookup.

    Returns:
        The NR-ARFCN of the given frequency.

    Raises:
        ValueError: If the frequency is not valid.
    """

    table = get_table('freq_nrarfcn', release_3gpp)

    if not isinstance(frequency, float) and not isinstance(frequency, int):
        raise ValueError('Frequency must be a float or an integer.')

    if frequency < 0 or frequency > 100_000:
        raise ValueError('Frequency must be between 0 and 100,000 (MHz).')

    for row in table.data:
        if table.get_cell(row, 'f_min') <= frequency <= table.get_cell(row, 'f_max'):
            f_offset = table.get_cell(row, 'f_ref_offs')
            delta_f = table.get_cell(row, 'df_global')
            n_offset = table.get_cell(row, 'n_ref_offs')
            nrarfcn = n_offset + (frequency - f_offset) * 1000. / delta_f
            return min(round(nrarfcn), 3_279_165)

    raise ValueError('Frequency is not valid.')
