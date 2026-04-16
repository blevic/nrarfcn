from nrarfcn.api.lte import LTE_DEFAULT_RELEASE, get_lte_earfcn_table, lte_frequency_for_earfcn, validate_lte_earfcn


def get_frequency_by_lte_earfcn(earfcn: int, release_3gpp: int = LTE_DEFAULT_RELEASE) -> float:
    """Gets the frequency of a given LTE EARFCN, in MHz.

    Args:
        earfcn: The LTE EARFCN to get the frequency of.
        release_3gpp: The 3GPP release to use for table lookup. LTE defaults to Rel-19.

    Returns:
        The frequency of the given LTE EARFCN, in MHz.

    Raises:
        ValueError: If the LTE EARFCN is not valid.
    """
    validate_lte_earfcn(earfcn)
    table = get_lte_earfcn_table(release_3gpp)

    for row in table.data:
        dl_frequency = lte_frequency_for_earfcn(
            earfcn,
            table.get_cell(row, 'f_dl_low'),
            table.get_cell(row, 'dl_offset'),
            table.get_cell(row, 'dl_first'),
            table.get_cell(row, 'dl_last'),
        )
        if dl_frequency is not None:
            return dl_frequency

        ul_frequency = lte_frequency_for_earfcn(
            earfcn,
            table.get_cell(row, 'f_ul_low'),
            table.get_cell(row, 'ul_offset'),
            table.get_cell(row, 'ul_first'),
            table.get_cell(row, 'ul_last'),
        )
        if ul_frequency is not None:
            return ul_frequency

    raise ValueError('LTE EARFCN is not valid.')
