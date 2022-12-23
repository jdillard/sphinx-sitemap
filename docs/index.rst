Sphinx-sitemap
==============

A `Sphinx`_ extension to generate multiversion and multilanguage
`sitemaps.org`_ compliant sitemaps for the HTML version of your Sphinx
documentation.

|PyPI version| |Conda Forge| |Downloads| |Code style: Black| |Parallel Safe|

Install
-------

Directly install via ``pip`` by using::

    pip install sphinx-sitemap

Or with ``conda`` via ``conda-forge``::

    conda install -c conda-forge sphinx-sitemap

Use
---

Add ``sphinx_sitemap`` to the `extensions`_ array in your Sphinx **conf.py**.
For example:

.. code-block:: python

   extensions = ['sphinx_sitemap']

.. toctree::
   :maxdepth: 1

   configuration
   contributing
   changelog


.. _extensions: https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-extensions
.. _guzzle_sphinx_theme: https://github.com/guzzle/guzzle_sphinx_theme
.. _LICENSE: LICENSE
.. _sitemaps.org: https://www.sitemaps.org/protocol.html
.. _Sphinx: http://sphinx-doc.org/

.. |PyPI version| image:: https://img.shields.io/pypi/v/sphinx-sitemap.svg
   :target: https://pypi.python.org/pypi/sphinx-sitemap
.. |Conda Forge| image:: https://img.shields.io/conda/vn/conda-forge/sphinx-sitemap.svg
   :target: https://anaconda.org/conda-forge/sphinx-sitemap
.. |Downloads| image:: https://pepy.tech/badge/sphinx-sitemap/month
    :target: https://pepy.tech/project/sphinx-sitemap
.. |Code style: Black| image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/psf/black
.. |Parallel Safe| image:: https://img.shields.io/badge/parallel%20safe-False-red
   :target: #
