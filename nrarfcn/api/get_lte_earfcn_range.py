from typing import Union

from nrarfcn.api.lte import LTE_DEFAULT_RELEASE, get_lte_channel_range


def get_lte_earfcn_range(band: Union[str, int], direction='', release_3gpp: int = LTE_DEFAULT_RELEASE) -> tuple:
    """Gets the LTE EARFCN range for a given band.

    Args:
        band: The LTE band to get the range for, e.g. 'B12'.
        direction: 'dl' or 'ul' to get the downlink or uplink range. If not specified, 'dl' is used.
        release_3gpp: The 3GPP release to use for table lookup. LTE defaults to Rel-19.

    Returns:
        A tuple with the min LTE EARFCN and max LTE EARFCN for the given band and direction.

    Raises:
        ValueError: If the given band is not a valid LTE band.
    """
    return get_lte_channel_range(band, direction, release_3gpp)
