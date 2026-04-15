from nrarfcn.tables.Table import Table


def table_freq_nrarfcn() -> Table:
    table_id = 'freq_nrarfcn'
    table_release_3gpp = 17
    table_ts = "3GPP TS 38.104 V17.6.0"
    table_name = "Table 5.4.2.1-1: NR-ARFCN parameters for the global frequency raster"
    table_header = ['f_min', 'f_max', 'df_global', 'f_ref_offs', 'n_ref_offs', 'n_ref_min', 'n_ref_max']
    table_data = [
        [0, 3_000, 5, 0, 0, 0, 599_999],
        [3_000, 24_250, 15, 3_000, 600_000, 600_000, 2_016_666],
        [24_250, 100_000, 60, 24_250.08, 2_016_667, 2_016_667, 3_279_165]
    ]

    return Table(table_id, table_release_3gpp, table_ts, table_name, table_header, table_data)
