# nrarfcn
Your NR-ARFCN calculator, as a Python package.

### What is it?

This is a Python package that calculates the frequency for a given NR-ARFCN, and related information.

It follows 3GPP [TS 38.104](https://portal.3gpp.org/desktopmodules/Specifications/SpecificationDetails.aspx?specificationId=3202), table 5.4.2.1-1: "_NR-ARFCN parameters for the global frequency raster_"

### How do I install it?

```bash
pip install nrarfcn
```

### How do I use it?

```python
>>> from nrarfcn import get_frequency, get_nrarfcn

>>> get_frequency(620000)
3300.0

>>> get_nrarfcn(27500.0)
2070832
```

### Contributing

Make any requests, raise any issues, create pull requests, or directly contact me on [github.com/blevic/nrarfcn](https://github.com/blevic/nrarfcn). I'll be happy to help.

### Author

By the way, hi there! I'm Breno. Follow me on github: [@blevic](https://github.com/blevic).

### License

This software is licensed under the [MIT license](LICENSE).