from typing import List

from nrarfcn.api.lte import LTE_DEFAULT_RELEASE, frequency_range_contains, get_lte_bands_table, validate_lte_frequency


def get_lte_bands_by_frequency(frequency: float, release_3gpp: int = LTE_DEFAULT_RELEASE) -> List[str]:
    """Lists the possible LTE bands of a given frequency in MHz.

    Args:
        frequency: The frequency to get the bands of, in MHz.
        release_3gpp: The 3GPP release to use for table lookup. LTE defaults to Rel-19.

    Returns:
        A list of LTE bands that include the given frequency. Empty list if not in any LTE band.

    Raises:
        ValueError: If the frequency is not an int and not a float, or out of range.
    """
    validate_lte_frequency(frequency)
    table = get_lte_bands_table(release_3gpp)
    bands = []

    for row in table.data:
        ul_condition = frequency_range_contains(
            frequency,
            table.get_cell(row, 'f_ul_low'),
            table.get_cell(row, 'f_ul_high'),
        )
        dl_condition = frequency_range_contains(
            frequency,
            table.get_cell(row, 'f_dl_low'),
            table.get_cell(row, 'f_dl_high'),
        )

        if ul_condition or dl_condition:
            bands.append(table.get_cell(row, 'band'))

    return bands
