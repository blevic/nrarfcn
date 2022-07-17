from typing import Union
from nrarfcn.tables.bands_fr1 import table_bands_fr1
from nrarfcn.tables.bands_fr2 import table_bands_fr2


def get_duplex_mode(band: Union[str, int]) -> str:
    """Gets the duplex mode for a given band.

    Args:
        band: The band to get the duplex mode for.

    Returns:
        The duplex mode for the given band -- TDD, FDD, SDL or SUL.

    Raises:
        ValueError: If the given band is not valid.
    """
    if isinstance(band, int):
        band = 'n' + str(band)
    elif not isinstance(band, str):
        raise ValueError("Band must be a string or integer.")

    table_fr1 = table_bands_fr1()
    table_fr2 = table_bands_fr2()

    for table in [table_fr1, table_fr2]:
        for row in table.data:
            if band == table.get_cell(row, 'band'):
                return table.get_cell(row, 'duplex_mode')

    raise ValueError(f"Band {band} not in table.")
