from nrarfcn.api.get_bands_by_frequency import get_bands_by_frequency
from nrarfcn.api.get_frequency import get_frequency


def get_bands_by_nrarfcn(nrarfcn: int) -> list:
    """Gets the bands of a given NR-ARFCN.

    Args:
        nrarfcn: The NR-ARFCN to get the bands of.

    Returns:
        The bands of the given NR-ARFCN.

    Raises:
        ValueError: If the NR-ARFCN is not valid.
    """

    if not isinstance(nrarfcn, int):
        raise ValueError('NR-ARFCN must be an integer.')

    if nrarfcn < 0 or nrarfcn > 3_279_165:
        raise ValueError('NR-ARFCN must be between 0 and 3,279,165.')

    bands = []
    for band in get_bands_by_frequency(get_frequency(nrarfcn)):
        bands.append(band)

    return bands
