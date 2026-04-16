from typing import List

from nrarfcn.api.lte import LTE_DEFAULT_RELEASE, get_lte_earfcn_table, lte_earfcn_for_frequency, validate_lte_frequency


def get_lte_earfcn_by_frequency(frequency: float, release_3gpp: int = LTE_DEFAULT_RELEASE) -> List[int]:
    """Lists the possible LTE EARFCNs for a given frequency in MHz.

    Args:
        frequency: The frequency to get the LTE EARFCNs of, in MHz.
        release_3gpp: The 3GPP release to use for table lookup. LTE defaults to Rel-19.

    Returns:
        A numerically sorted list of LTE EARFCNs for the given frequency. Empty list if no LTE EARFCN matches.

    Raises:
        ValueError: If the frequency is not an int and not a float, or out of range.
    """
    validate_lte_frequency(frequency)
    table = get_lte_earfcn_table(release_3gpp)
    earfcns = []

    for row in table.data:
        dl_earfcn = lte_earfcn_for_frequency(
            frequency,
            table.get_cell(row, 'f_dl_low'),
            table.get_cell(row, 'dl_offset'),
            table.get_cell(row, 'dl_first'),
            table.get_cell(row, 'dl_last'),
        )
        if dl_earfcn is not None and dl_earfcn not in earfcns:
            earfcns.append(dl_earfcn)

        ul_earfcn = lte_earfcn_for_frequency(
            frequency,
            table.get_cell(row, 'f_ul_low'),
            table.get_cell(row, 'ul_offset'),
            table.get_cell(row, 'ul_first'),
            table.get_cell(row, 'ul_last'),
        )
        if ul_earfcn is not None and ul_earfcn not in earfcns:
            earfcns.append(ul_earfcn)

    return sorted(earfcns)
