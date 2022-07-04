# nrarfcn
Your NR-ARFCN calculator, as a Python package.

#### What is it?

This is a Python package that calculates the frequency for a given NR-ARFCN, and related information.

It follows 3GPP [TS 38.104](https://portal.3gpp.org/desktopmodules/Specifications/SpecificationDetails.aspx?specificationId=3202), table 5.4.2.1-1: "_NR-ARFCN parameters for the global frequency raster_"

#### How do I install it?

```bash
pip install nrarfcn
```

#### How do I use it?

    >>> from nrarfcn.utils import get_frequency
    >>> get_frequency(620000)
    3300.0

#### License

This software is licensed under the [MIT license](LICENSE).