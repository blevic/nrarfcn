Public API
==========

The public functions are available from the top-level ``nrarfcn`` package.

Release selection
-----------------

3GPP Rel-17 is used by default for NR. To use another supported NR
release, pass ``release_3gpp`` to any API function. LTE/E-UTRA APIs use
Rel-19 by default.

.. code:: python

   >>> import nrarfcn as nr
   >>> nr.get_frequency_range('n110', release_3gpp=19)
   (1432, 1435)
   >>> nr.get_frequency_by_lte_earfcn(300)
   2140.0

Functions
---------

.. currentmodule:: nrarfcn

.. autofunction:: get_frequency

.. autofunction:: get_nrarfcn

.. autofunction:: get_bands_by_frequency

.. autofunction:: get_bands_by_nrarfcn

.. autofunction:: get_duplex_mode

.. autofunction:: get_nrarfcn_range

.. autofunction:: get_frequency_range

.. autofunction:: get_gscn_by_frequency

.. autofunction:: get_frequency_by_gscn

.. autofunction:: get_gscn_range

.. autofunction:: get_frequency_by_lte_earfcn

.. autofunction:: get_lte_earfcn_by_frequency

.. autofunction:: get_lte_bands_by_frequency

.. autofunction:: get_band_by_lte_earfcn

.. autofunction:: get_lte_earfcn_range
