from typing import Union
from nrarfcn.tables.bands_fr1 import table_bands_fr1
from nrarfcn.tables.bands_fr2 import table_bands_fr2


def get_frequency_range(band: Union[str, int], direction='') -> tuple:
    """Gets the frequency range for a given band, in MHz.

    Args:
        band: The band to get the range for, e.g. 'n12'.
        direction: 'dl' or 'ul' to get the range for the downlink or uplink. If not specified, 'dl' is used,
            except if the band is uplink only.

    Returns:
        A tuple with the min frequency in MHz and max frequency in MHz for the given band and direction

    Raises:
        ValueError: If the given band is not a valid band.
    """
    table_fr1 = table_bands_fr1()
    table_fr2 = table_bands_fr2()

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

    for table in tables:
        for row in table.data:
            if table.get_cell(row, 'band') == band:
                if (direction == '' and table.get_cell(row, 'f_dl_low') == 'N/A') or direction == 'ul':
                    ul_min = table.get_cell(row, 'f_ul_low')
                    ul_max = table.get_cell(row, 'f_ul_high')
                    return ul_min, ul_max
                elif direction == 'dl' or direction == '':
                    dl_min = table.get_cell(row, 'f_dl_low')
                    dl_max = table.get_cell(row, 'f_dl_high')
                    return dl_min, dl_max
                else:
                    raise ValueError(f"Invalid direction again.")

    raise ValueError(f"Could not find band {band} in any table.")
