from typing import Optional, Union
from nrarfcn.api.lte import get_lte_duplex_mode, is_lte_band, lte_release
from nrarfcn.tables import DEFAULT_RELEASE, get_table


def get_duplex_mode(band: Union[str, int], release_3gpp: Optional[int] = None) -> str:
    """Gets the duplex mode for a given band.

    Args:
        band: The band to get the duplex mode for. NR bands use 'n', LTE bands use 'B'.
        release_3gpp: The 3GPP release to use for table lookup. NR defaults to Rel-17; LTE defaults to Rel-19.

    Returns:
        The duplex mode for the given band.

    Raises:
        ValueError: If the given band is not valid.
    """
    if is_lte_band(band):
        return get_lte_duplex_mode(band, lte_release(release_3gpp))

    release_3gpp = DEFAULT_RELEASE if release_3gpp is None else release_3gpp

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
