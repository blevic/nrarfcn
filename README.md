# 5G NR-ARFCN calculator
<p align="left">
  <a href='https://pypi.org/project/nrarfcn/'>
    <img src='https://img.shields.io/pypi/v/nrarfcn' alt='PyPi Version' />
  </a>
  <a href='https://pypi.org/project/nrarfcn/'>
    <img src='https://img.shields.io/pypi/dm/nrarfcn' alt='Downloads/Month' />
  </a>
  </a>
    <a href='https://github.com/blevic/nrarfcn/actions/workflows/package-tests.yml'>
    <img src='https://github.com/blevic/nrarfcn/actions/workflows/package-tests.yml/badge.svg?branch=main' alt='Package Tests' />
  </a>
  <a href='https://nrarfcn.readthedocs.io/en/latest/?badge=latest'>
    <img src='https://readthedocs.org/projects/nrarfcn/badge/?version=latest' alt='Documentation Status' />
  </a>
</p>

[``nrarfcn``](https://github.com/blevic/nrarfcn): a 5G NR-ARFCN calculator, as a Python package.

This is a Python package that calculates the frequency for a given NR-ARFCN, the NR-ARFCN for a given frequency, and related NR band information. 3GPP **Rel-17** remains the default table release, and **Rel-18** / **Rel-19** can be selected with the optional `release_3gpp` argument.

It follows [3GPP TS 38.104](https://portal.3gpp.org/desktopmodules/Specifications/SpecificationDetails.aspx?specificationId=3202): v17.6.0 by default, with v18.13.0 and v19.4.0 available when requested.

### Documentation

[``nrarfcn``](https://github.com/blevic/nrarfcn) is documented on: [nrarfcn.rtfd.io](https://nrarfcn.rtfd.io/).

### Installation

```bash
pip install nrarfcn
```

### Usage

```python
>>> import nrarfcn as nr

>>> nr.get_frequency(620000)
3300.0

>>> nr.get_nrarfcn(27500.0)
2070832

>>> nr.get_bands_by_frequency(1850.0)
['n2', 'n3', 'n25']

>>> nr.get_bands_by_nrarfcn(2564083)
['n263']

>>> nr.get_duplex_mode('n71')
'FDD'

>>> nr.get_nrarfcn_range('n25', direction='ul')
(370000, 383000)

>>> nr.get_frequency_range('n100', direction='dl')
(919.4, 925)

>>> nr.get_frequency_by_gscn(2156)
862.85

>>> nr.get_gscn_by_frequency(4405.440)
8475

>>> nr.get_gscn_range('n92')
(3584, 3787)

>>> nr.get_frequency_range('n110', release_3gpp=19)
(1432, 1435)
```

### Contributing

Every contribution is welcome. Make any requests, raise any issues, create pull requests, or directly contact me on [github.com/blevic/nrarfcn](https://github.com/blevic/nrarfcn). I'll be happy to help.

### Author

By the way, hi there! I'm Breno. Follow me on github: [@blevic](https://github.com/blevic).

### License

This software is licensed under the [MIT license](https://github.com/blevic/nrarfcn/blob/main/LICENSE).
