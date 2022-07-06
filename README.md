# 5G NR-ARFCN calculator

[``nrarfcn``](https://github.com/blevic/nrarfcn): your NR-ARFCN calculator, as a Python package.

### What is it?

This is a Python package that calculates the frequency for a given NR-ARFCN, the NR-ARFCN for a given frequency, and related NR band information.

It follows 3GPP [TS 38.104](https://portal.3gpp.org/desktopmodules/Specifications/SpecificationDetails.aspx?specificationId=3202), "_5G; NR; Base Station (BS) radio transmission and reception_".

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

>>> nr.get_bands_by_frequency(617.0)
['n71']
```

### Contributing

Make any requests, raise any issues, create pull requests, or directly contact me on [github.com/blevic/nrarfcn](https://github.com/blevic/nrarfcn). I'll be happy to help.

### Author

By the way, hi there! I'm Breno. Follow me on github: [@blevic](https://github.com/blevic).

### License

This software is licensed under the [MIT license](LICENSE).