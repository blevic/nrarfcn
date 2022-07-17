from typing import Union
from nrarfcn.tables.applicable_nrarfcn_fr1 import table_applicable_nrarfcn_fr1
from nrarfcn.tables.applicable_nrarfcn_fr2 import table_applicable_nrarfcn_fr2


def get_nrarfcn_range(band: Union[str, int], direction='') -> tuple:
    """Gets the NR-ARFCN range for a given band.

    Args:
        band: The band to get the range for, e.g. 'n12'.
        direction: 'dl' or 'ul' to get the range for the downlink or uplink. If not specified, 'dl' is used,
            except if the band is uplink only.

    Returns:
        A tuple with the min NR-ARFCN and max NR-ARFCN for the given band and direction

    Raises:
        ValueError: If the given band is not a valid band.
    """
    table_fr1 = table_applicable_nrarfcn_fr1()
    table_fr2 = table_applicable_nrarfcn_fr2()

    valid_bands = table_fr1.get_column('band') + table_fr2.get_column('band')

    if isinstance(band, int):
        band = 'n' + str(band)

    if not isinstance(band, str) or not band or band[0] != 'n':
        raise ValueError("The band must be an integer or a string starting with 'n': 12, 'n12', 101, 'n101', etc.")

    if band not in valid_bands:
        raise ValueError(f'Invalid band: {band}.')

    if direction not in ['', 'dl', 'ul']:
        raise ValueError(f"Invalid direction: {direction}. Must be 'dl', 'ul' or default value (empty string).")

    tables = [table_fr1, table_fr2]
    band_rows = []

    for table in tables:
        for row in table.data:
            if table.get_cell(row, 'band') == band:
                if (direction == '' and table.get_cell(row, 'dl_first') == 'N/A') or direction == 'ul':
                    ul_min = table.get_cell(row, 'ul_first')
                    ul_max = table.get_cell(row, 'ul_last')
                    band_rows.append((ul_min, ul_max))
                elif direction == 'dl' or direction == '':
                    dl_min = table.get_cell(row, 'dl_first')
                    dl_max = table.get_cell(row, 'dl_last')
                    band_rows.append((dl_min, dl_max))
                else:
                    raise ValueError(f"Invalid direction again.")

    min_nrarfcn = min(band_rows, key=lambda x: x[0])[0]
    max_nrarfcn = max(band_rows, key=lambda x: x[1])[1]

    return min_nrarfcn, max_nrarfcn
