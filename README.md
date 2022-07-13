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
</p>

[``nrarfcn``](https://github.com/blevic/nrarfcn): a 5G NR-ARFCN calculator, as a Python package.

### What is it?

This is a Python package that calculates the frequency for a given NR-ARFCN, the NR-ARFCN for a given frequency, and related NR band information, according to 3GPP **Rel-17**.

It follows [3GPP TS 38.104](https://portal.3gpp.org/desktopmodules/Specifications/SpecificationDetails.aspx?specificationId=3202) v17.6.0: "_5G; NR; Base Station (BS) radio transmission and reception_".

### How do I install it?

```bash
pip install nrarfcn
```

### How do I use it?

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
```

### Contributing

Make any requests, raise any issues, create pull requests, or directly contact me on [github.com/blevic/nrarfcn](https://github.com/blevic/nrarfcn). I'll be happy to help.

### Author

By the way, hi there! I'm Breno. Follow me on github: [@blevic](https://github.com/blevic).

### License

This software is licensed under the [MIT license](https://github.com/blevic/nrarfcn/blob/main/LICENSE).
