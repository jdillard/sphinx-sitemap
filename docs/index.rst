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

Set the value of `html_baseurl`_ in your Sphinx **conf.py** to the current
base URL of your documentation. For example:

.. code-block:: python

   html_baseurl = 'https://my-site.com/docs/'

After the HTML build is done, **sphinx-sitemap** will output the location of the
sitemap::

    sitemap.xml was generated for URL https://my-site.com/docs/ in /path/to/_build/sitemap.xml

.. tip:: Make sure to confirm the accuracy of the sitemap after installs and upgrades.


See :doc:`configuration` for more information about how to use **sphinx-sitemap**.

.. toctree::
   :maxdepth: 1

   configuration
   seo
   contributing
   changelog


.. _extensions: https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-extensions
.. _html_baseurl: https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-html_baseurl
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
