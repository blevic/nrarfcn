from nrarfcn.tables.Table import Table


def table_bands_fr2() -> Table:
    table_id = 'bands_fr2'
    table_release_3gpp = 17
    table_ts = "3GPP TS 38.104 V17.6.0"
    table_name = "Table 5.2-2: NR operating bands in FR2"
    table_header = ['band', 'f_ul_low', 'f_ul_high', 'f_dl_low', 'f_dl_high', 'duplex_mode']
    table_data = [
        ['n257', 26500, 29500, 26500, 29500, 'TDD'],
        ['n258', 24250, 27500, 24250, 27500, 'TDD'],
        ['n259', 39500, 43500, 39500, 43500, 'TDD'],
        ['n260', 37000, 40000, 37000, 40000, 'TDD'],
        ['n261', 27500, 28350, 27500, 28350, 'TDD'],
        ['n262', 47200, 48200, 47200, 48200, 'TDD'],
        ['n263', 57000, 71000, 57000, 71000, 'TDD'],
    ]

    return Table(table_id, table_release_3gpp, table_ts, table_name, table_header, table_data)
