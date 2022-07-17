from typing import List
from nrarfcn.tables.bands_fr1 import table_bands_fr1
from nrarfcn.tables.bands_fr2 import table_bands_fr2


def get_bands_by_frequency(frequency: float) -> List[str]:
    """Lists the possible 5G-NR bands of a given frequency in MHz.

    Args:
        frequency: The frequency to get the bands of, in MHz.

    Returns:
        A list of the 5G-NR bands that the given frequency is in. Empty list if not in any NR band.

    Raises:
        ValueError: If the frequency is not an int and not a float, or out of NR-ARFCN defined range.
    """

    if not isinstance(frequency, float) and not isinstance(frequency, int):
        raise ValueError('Frequency must be a float or an integer.')

    if frequency < 0 or frequency > 100_000:
        raise ValueError('Frequency must be between 0 and 100,000 (MHz).')

    bands = []

    table = table_bands_fr1()

    for row in table.data:
        ul_min = table.get_cell(row, 'f_ul_low')
        ul_max = table.get_cell(row, 'f_ul_high')
        dl_min = table.get_cell(row, 'f_dl_low')
        dl_max = table.get_cell(row, 'f_dl_high')
        ul_exists = not isinstance(ul_min, str) and not isinstance(ul_max, str)
        dl_exists = not isinstance(dl_min, str) and not isinstance(dl_max, str)
        condition_ul = ul_exists and ul_min <= frequency <= ul_max
        condition_dl = dl_exists and dl_min <= frequency <= dl_max

        if condition_ul or condition_dl:
            bands.append(table.get_cell(row, 'band'))

    table = table_bands_fr2()

    for row in table.data:
        ul_dl_min = table.get_cell(row, 'f_ul_low')
        ul_dl_max = table.get_cell(row, 'f_ul_high')
        fr2_tdd_condition = ul_dl_min and ul_dl_min <= frequency <= ul_dl_max

        if fr2_tdd_condition:
            bands.append(table.get_cell(row, 'band'))

    return bands
