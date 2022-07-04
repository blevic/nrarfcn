def get_frequency(nrarfcn: int) -> float:
    """Gets the frequency of a given NR-ARFCN, in MHz.

    Args:
        nrarfcn: The NR-ARFCN to get the frequency of.

    Returns:
        The frequency of the given NR-ARFCN, in MHz.

    Raises:
        ValueError: If the NR-ARFCN is not valid.
    """

    freq_nr_table = [
        {
            'F_min_MHz': 0,
            'F_max_MHz': 3000,
            'DF_global_kHz': 5,
            'Fref_offs_MHz': 0,
            'Nref_offs': 0,
            'Nref_min': 0,
            'Nref_max': 599999
        },
        {
            'F_min_MHz': 3000,
            'F_max_MHz': 24250,
            'DF_global_kHz': 15,
            'Fref_offs_MHz': 3000,
            'Nref_offs': 600000,
            'Nref_min': 600000,
            'Nref_max': 2016666
        },
        {
            'F_min_MHz': 24250,
            'F_max_MHz': 100000,
            'DF_global_kHz': 60,
            'Fref_offs_MHz': 24250.08,
            'Nref_offs': 2016667,
            'Nref_min': 2016667,
            'Nref_max': 3279165
        }
    ]

    if type(nrarfcn) is not int:
        raise ValueError('NR-ARFCN must be an integer.')

    if nrarfcn < 0 or nrarfcn > 3279165:
        raise ValueError('NR-ARFCN must be between 0 and 3279165.')

    for row in freq_nr_table:
        if row['Nref_min'] <= nrarfcn <= row['Nref_max']:
            freq_kHz = int(row['Fref_offs_MHz']*1000) + row['DF_global_kHz'] * (nrarfcn - row['Nref_offs'])
            freq_MHz = freq_kHz / 1000
            return freq_MHz

    raise ValueError('NR-ARFCN is not valid.')
