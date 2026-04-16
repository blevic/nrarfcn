from typing import Union

from nrarfcn.tables import get_table


LTE_DEFAULT_RELEASE = 19
LTE_EARFCN_MIN = 0
LTE_EARFCN_MAX = 262143
_FREQUENCY_TOLERANCE = 1e-6


def is_lte_band(band: Union[str, int]) -> bool:
    return isinstance(band, str) and len(band) > 1 and band[0] in ['B', 'b']


def normalize_lte_band(band: Union[str, int]) -> str:
    if isinstance(band, int):
        band = 'B' + str(band)
    elif isinstance(band, str) and band and band[0] == 'b':
        band = 'B' + band[1:]

    if not isinstance(band, str) or not band or band[0] != 'B':
        raise ValueError("The LTE band must be an integer or a string starting with 'B': 12, 'B12', 101, 'B101', etc.")

    return band


def lte_release(release_3gpp):
    return LTE_DEFAULT_RELEASE if release_3gpp is None else release_3gpp


def validate_lte_earfcn(earfcn: int):
    if not isinstance(earfcn, int):
        raise ValueError('LTE EARFCN must be an integer.')

    if earfcn < LTE_EARFCN_MIN or earfcn > LTE_EARFCN_MAX:
        raise ValueError('LTE EARFCN must be between 0 and 262,143.')


def validate_lte_frequency(frequency: float):
    if not isinstance(frequency, float) and not isinstance(frequency, int):
        raise ValueError('Frequency must be a float or an integer.')

    if frequency < 0 or frequency > 100_000:
        raise ValueError('Frequency must be between 0 and 100,000 (MHz).')


def validate_direction(direction: str):
    if direction not in ['', 'dl', 'ul']:
        raise ValueError(f"Invalid direction: {direction}. Must be 'dl', 'ul' or default value (empty string).")


def get_lte_bands_table(release_3gpp: int = LTE_DEFAULT_RELEASE):
    return get_table('lte_bands', release_3gpp)


def get_lte_earfcn_table(release_3gpp: int = LTE_DEFAULT_RELEASE):
    return get_table('lte_earfcn', release_3gpp)


def frequency_range_contains(frequency: float, low, high) -> bool:
    return not isinstance(low, str) and not isinstance(high, str) and low <= frequency <= high


def get_lte_duplex_mode(band: Union[str, int], release_3gpp: int = LTE_DEFAULT_RELEASE) -> str:
    band = normalize_lte_band(band)
    table = get_lte_bands_table(release_3gpp)

    for row in table.data:
        if band == table.get_cell(row, 'band'):
            return table.get_cell(row, 'duplex_mode')

    raise ValueError(f"Band {band} not in table.")


def get_lte_frequency_range(band: Union[str, int], direction='', release_3gpp: int = LTE_DEFAULT_RELEASE) -> tuple:
    band = normalize_lte_band(band)
    validate_direction(direction)
    table = get_lte_bands_table(release_3gpp)

    for row in table.data:
        if band == table.get_cell(row, 'band'):
            if direction == 'ul':
                return table.get_cell(row, 'f_ul_low'), table.get_cell(row, 'f_ul_high')
            return table.get_cell(row, 'f_dl_low'), table.get_cell(row, 'f_dl_high')

    raise ValueError(f'Invalid band: {band}.')


def get_lte_channel_range(band: Union[str, int], direction='', release_3gpp: int = LTE_DEFAULT_RELEASE) -> tuple:
    band = normalize_lte_band(band)
    validate_direction(direction)
    table = get_lte_earfcn_table(release_3gpp)

    for row in table.data:
        if band == table.get_cell(row, 'band'):
            if direction == 'ul':
                return table.get_cell(row, 'ul_first'), table.get_cell(row, 'ul_last')
            return table.get_cell(row, 'dl_first'), table.get_cell(row, 'dl_last')

    raise ValueError(f'Invalid band: {band}.')


def lte_frequency_for_earfcn(earfcn: int, f_low, offset, first, last):
    if isinstance(first, str) or not first <= earfcn <= last:
        return None

    frequency = f_low + 0.1 * (earfcn - offset)
    return round(frequency, 1)


def lte_earfcn_for_frequency(frequency: float, f_low, offset, first, last):
    if isinstance(first, str):
        return None

    earfcn_float = offset + (frequency - f_low) * 10
    earfcn = int(round(earfcn_float))
    if not first <= earfcn <= last:
        return None

    candidate_frequency = lte_frequency_for_earfcn(earfcn, f_low, offset, first, last)
    if abs(candidate_frequency - frequency) > _FREQUENCY_TOLERANCE:
        return None

    return earfcn
