Sphinx Sitemap Generator Extension
==================================

A `Sphinx`_ extension to generate multiversion and multilanguage
`sitemaps.org`_ compliant sitemaps for the HTML version of your Sphinx
documentation.

|PyPI version| |Conda Forge| |Downloads| |Code style: Black| |Parallel Safe|

Installing
----------

Directly install via pip by using::

    pip install sphinx-sitemap

Add ``sphinx_sitemap`` to the `extensions`_ array in your Sphinx **conf.py**.
For example:

.. code-block:: python

   extensions = ['sphinx_sitemap']

Contributing
------------

Pull Requests welcome! See `CONTRIBUTING`_ for instructions on how best to
contribute.

License
-------

**sphinx-sitemap** is made available under a **MIT license**; see `LICENSE`_ for
details.

Originally based on the sitemap generator in the `guzzle_sphinx_theme`_ project,
also licensed under the MIT license.

.. _CONTRIBUTING: CONTRIBUTING.md
.. _extensions: https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-extensions
.. _guzzle_sphinx_theme: https://github.com/guzzle/guzzle_sphinx_theme
.. _LICENSE: LICENSE
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
