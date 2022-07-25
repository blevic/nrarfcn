from typing import Union
from nrarfcn.tables.applicable_ss_raster_fr1 import table_applicable_ss_raster_fr1
from nrarfcn.tables.applicable_ss_raster_fr2 import table_applicable_ss_raster_fr2


def get_gscn_range(band: Union[str, int]) -> tuple:
    """Gets the GSCN range for a given band.

    Args:
        band: The band to get the range for, e.g. 'n12' or 12.

    Returns:
        A tuple with the min GSCN and max GSCN for the given band.

    Raises:
        ValueError: If the given band is not a valid band.
    """
    table_fr1 = table_applicable_ss_raster_fr1()
    table_fr2 = table_applicable_ss_raster_fr2()

    valid_bands = table_fr1.get_column('band') + table_fr2.get_column('band')

    if isinstance(band, int):
        band = 'n' + str(band)

    if not isinstance(band, str) or not band or band[0] != 'n':
        raise ValueError("The band must be an integer or a string starting with 'n': 12, 'n12', 101, 'n101', etc.")

    if band not in valid_bands:
        raise ValueError(f'Invalid band: {band}.')

    tables = [table_fr1, table_fr2]
    band_rows = []

    for table in tables:
        for row in table.data:
            if table.get_cell(row, 'band') == band:
                gscn_first = table.get_cell(row, 'gscn_first')
                gscn_last = table.get_cell(row, 'gscn_last')

                if gscn_first == 0 or gscn_last == 0:
                    gscn_first = min(table.get_cell(row, 'note'))
                    gscn_last = max(table.get_cell(row, 'note'))

                band_rows.append((gscn_first, gscn_last))

    min_gscn = min(band_rows, key=lambda x: x[0])[0]
    max_gscn = max(band_rows, key=lambda x: x[1])[1]

    return min_gscn, max_gscn
