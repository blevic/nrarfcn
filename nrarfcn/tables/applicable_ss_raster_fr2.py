from nrarfcn.tables.Table import Table


def table_applicable_ss_raster_fr2() -> Table:
    table_id = 'applicable_ss_raster_fr2'
    table_release_3gpp = 17
    table_ts = "3GPP TS 38.104 V17.6.0"
    table_name = "Table 5.4.3.3-2: Applicable SS raster entries per operating band (FR2)"
    table_header = ['band', 'scs', 'block_pattern', 'gscn_first', 'step_size', 'gscn_last', 'note']

    table_3_120 = {24156 + 6*n - 3 * ((n+5)//18) for n in range(0, 137 + 1)}
    table_3_480 = {24162 + 24*n - 12 * ((n+4)//18) for n in range(0, 33 + 1)}

    table_data = [
        ['n257', 120, 'D', 22388, 1, 22558, {}],
        ['n257', 240, 'E', 22390, 2, 22556, {}],
        ['n258', 120, 'D', 22257, 1, 22443, {}],
        ['n258', 240, 'E', 22258, 2, 22442, {}],
        ['n259', 120, 'D', 23140, 1, 23369, {}],
        ['n259', 240, 'E', 23142, 2, 23368, {}],
        ['n260', 120, 'D', 22995, 1, 23166, {}],
        ['n260', 240, 'E', 22996, 2, 23164, {}],
        ['n261', 120, 'D', 22446, 1, 22492, {}],
        ['n261', 240, 'E', 22446, 2, 22490, {}],
        ['n262', 120, 'D', 23586, 1, 23641, {}],
        ['n262', 240, 'E', 23588, 2, 23640, {}],
        ['n263', 120, 'D', 0, 0, 0, table_3_120],
        ['n263', 480, 'F', 0, 0, 0, table_3_480],
        ['n263', 960, 'G', 24162, 6, 24954, {}]
    ]

    return Table(table_id, table_release_3gpp, table_ts, table_name, table_header, table_data)
