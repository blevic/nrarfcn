from nrarfcn.tables.Table import Table


def table_gscn_parameters() -> Table:
    table_id = 'gscn_parameters'
    table_release_3gpp = 17
    table_ts = "3GPP TS 38.104 V17.6.0"
    table_name = "Table 5.4.3.1-1: GSCN parameters for the global frequency raster"
    table_header = ['f_min', 'f_max',
                    'n_min', 'n_max', 'm_set', 'f_offs', 'n_coeff', 'm_coeff',
                    'g_offs', 'g_n_coeff', 'g_m_coeff',
                    'gscn_min', 'gscn_max']
    table_data = [
        [0, 3000,
         1, 2499, {1, 3, 5}, 0, 1.200, 0.050,
         -1.5, 3, 0.5,
         2, 7498],
        [3000, 24250,
         0, 14756, {}, 3000, 1.44, 0,
         7499, 1, 0,
         7499, 22255],
        [24250, 100000,
         0, 4383, {}, 24250.08, 17.28, 0,
         22256, 1, 0,
         22256, 26639]
    ]

    return Table(table_id, table_release_3gpp, table_ts, table_name, table_header, table_data)
