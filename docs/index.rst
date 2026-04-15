Welcome to nrarfcn's documentation!
===================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   nrarfcn.api
   nrarfcn.tables

nrarfcn
===========

A 5G NR-ARFCN calculator, as a Python package.

3GPP Rel-17 is the default table release. Rel-18 and Rel-19 can be selected with the optional ``release_3gpp`` argument.

Visit the project `homepage <https://github.com/blevic/nrarfcn/>`__.

Installation
~~~~~~~~~~~~

.. code:: bash

   pip install nrarfcn

Usage
~~~~~
.. code:: python

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

Documentation
~~~~~~~~~~~~~

Find complete documentation on:
`nrarfcn.rtfd.io <https://nrarfcn.rtfd.io/>`__.


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
