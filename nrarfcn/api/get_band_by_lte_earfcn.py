from nrarfcn.api.lte import LTE_DEFAULT_RELEASE, get_lte_earfcn_table, validate_lte_earfcn


def get_band_by_lte_earfcn(earfcn: int, release_3gpp: int = LTE_DEFAULT_RELEASE) -> str:
    """Gets the LTE band of a given EARFCN.

    Args:
        earfcn: The LTE EARFCN to get the band of.
        release_3gpp: The 3GPP release to use for table lookup. LTE defaults to Rel-19.

    Returns:
        The LTE band of the given EARFCN.

    Raises:
        ValueError: If the LTE EARFCN is not valid.
    """
    validate_lte_earfcn(earfcn)
    table = get_lte_earfcn_table(release_3gpp)

    for row in table.data:
        dl_first = table.get_cell(row, 'dl_first')
        dl_last = table.get_cell(row, 'dl_last')
        ul_first = table.get_cell(row, 'ul_first')
        ul_last = table.get_cell(row, 'ul_last')
        in_dl_range = not isinstance(dl_first, str) and dl_first <= earfcn <= dl_last
        in_ul_range = not isinstance(ul_first, str) and ul_first <= earfcn <= ul_last

        if in_dl_range or in_ul_range:
            return table.get_cell(row, 'band')

    raise ValueError('LTE EARFCN is not valid.')
