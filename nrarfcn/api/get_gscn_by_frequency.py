from nrarfcn.tables.gscn_parameters import table_gscn_parameters


def get_gscn_by_frequency(freq: float) -> int:
    """Gets the GSCN (Global Synchronization Channel Number) of a given frequency in MHz.

    Args:
        freq: The frequency to get the GSCN of.

    Returns:
        The GSCN of the given frequency, in MHz, or the closest GSCN to the given frequency.

    Raises:
        ValueError: If the given frequency is invalid
    """
    if not isinstance(freq, float) and not isinstance(freq, int):
        raise ValueError("Frequency must be a float or an integer")

    if freq < 0 or freq > 100_000:
        raise ValueError("Frequency must be between 0 and 100,000 (MHz)")

    table = table_gscn_parameters()

    for row in table.data:
        if table.get_cell(row, 'f_min') <= freq <= table.get_cell(row, 'f_max'):
            if table.get_cell(row, 'm_set') == {}:
                n = round((freq - table.get_cell(row, 'f_offs'))/table.get_cell(row, 'n_coeff'))
                return int(table.get_cell(row, 'g_offs') + n)
            else:
                n_round_gap = table.get_cell(row, 'm_coeff') * sum(table.get_cell(row, 'm_set'))/len(table.get_cell(row, 'm_set'))
                n = round((freq - n_round_gap) / table.get_cell(row, 'n_coeff'))
                m = min((abs(freq - (n * table.get_cell(row, 'n_coeff') + m_candidate * table.get_cell(row, 'm_coeff'))), m_candidate) for m_candidate in table.get_cell(row, 'm_set'))[1]
                return int(table.get_cell(row, 'g_offs') + n * table.get_cell(row, 'g_n_coeff') + m * table.get_cell(row, 'g_m_coeff'))

    raise ValueError("Expected to have found a frequency in the table, but didn't")
