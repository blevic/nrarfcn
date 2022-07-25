from nrarfcn.tables.gscn_parameters import table_gscn_parameters


def get_frequency_by_gscn(gscn: int) -> float:
    """Gets the frequency of a given GSCN (Global Synchronization Channel Number), in MHz.

    Args:
        gscn: The GSCN to get the frequency of.

    Returns:
        The frequency of the given GSCN, in MHz.

    Raises:
        ValueError: If the given GSCN is invalid
    """
    if not isinstance(gscn, int):
        raise ValueError("GSCN must be an integer")

    if gscn < 2 or gscn > 26639:
        raise ValueError("GSCN must be between 2 and 26639")

    table = table_gscn_parameters()

    for row in table.data:
        if table.get_cell(row, 'gscn_min') <= gscn <= table.get_cell(row, 'gscn_max'):
            if table.get_cell(row, 'm_set') == {}:
                n = gscn - table.get_cell(row, 'g_offs')
                freq = table.get_cell(row, 'f_offs') + table.get_cell(row, 'n_coeff') * n
                return round(freq, 3)
            else:
                if gscn % 3 == 0:
                    n = gscn // table.get_cell(row, 'g_n_coeff')
                    m = 3
                elif gscn % 3 == 1:
                    n = gscn // table.get_cell(row, 'g_n_coeff')
                    m = 5
                elif gscn % 3 == 2:
                    n = (gscn + 1) // table.get_cell(row, 'g_n_coeff')
                    m = 1

                freq = table.get_cell(row, 'f_offs') + table.get_cell(row, 'n_coeff') * n + table.get_cell(row, 'm_coeff') * m
                return round(freq, 3)

    raise ValueError("Expected to have found a GSCN in the table, but didn't")
