from typing import Union
from nrarfcn.tables import DEFAULT_RELEASE, get_table


def get_duplex_mode(band: Union[str, int], release_3gpp: int = DEFAULT_RELEASE) -> str:
    """Gets the duplex mode for a given band.

    Args:
        band: The band to get the duplex mode for.
        release_3gpp: The 3GPP release to use for table lookup.

    Returns:
        The duplex mode for the given band -- TDD, FDD, SDL or SUL.

    Raises:
        ValueError: If the given band is not valid.
    """
    if isinstance(band, int):
        band = 'n' + str(band)
    elif not isinstance(band, str):
        raise ValueError("Band must be a string or integer.")

    table_fr1 = get_table('bands_fr1', release_3gpp)
    table_fr2 = get_table('bands_fr2', release_3gpp)

    for table in [table_fr1, table_fr2]:
        for row in table.data:
            if band == table.get_cell(row, 'band'):
                return table.get_cell(row, 'duplex_mode')

    raise ValueError(f"Band {band} not in table.")
