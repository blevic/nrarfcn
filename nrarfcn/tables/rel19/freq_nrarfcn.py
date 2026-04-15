from nrarfcn.tables.Table import Table


def table_freq_nrarfcn() -> Table:
    table_id = 'freq_nrarfcn'
    table_release_3gpp = 19
    table_ts = '3GPP TS 38.104 V19.4.0'
    table_name = 'Table 5.4.2.1-1: NR-ARFCN parameters for the global frequency raster'
    table_header = ['f_min', 'f_max', 'df_global', 'f_ref_offs', 'n_ref_offs', 'n_ref_min', 'n_ref_max']
    table_data = [
        [0, 3000, 5, 0, 0, 0, 599999],
        [3000, 24250, 15, 3000, 600000, 600000, 2016666],
        [24250, 100000, 60, 24250.08, 2016667, 2016667, 3279165]
    ]

    return Table(table_id, table_release_3gpp, table_ts, table_name, table_header, table_data)
