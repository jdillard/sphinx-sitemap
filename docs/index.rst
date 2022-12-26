Sphinx-sitemap
==============

A `Sphinx`_ extension to generate multi-version and multi-language
`sitemaps.org`_ compliant sitemaps for the HTML version of your Sphinx
documentation.

|PyPI version| |Conda Forge| |Downloads| |Parallel Safe| |GitHub Stars|

Install
-------

Directly install via ``pip`` by using::

    pip install sphinx-sitemap

Or with ``conda`` via ``conda-forge``::

    conda install -c conda-forge sphinx-sitemap

Use
---

Add ``sphinx_sitemap`` to :confval:`extensions` in your Sphinx **conf.py**.
For example:

.. code-block:: python

   extensions = ['sphinx_sitemap']

Set the value of :confval:`html_baseurl` in your Sphinx **conf.py** to the current
base URL of your documentation. For example:

.. code-block:: python

   html_baseurl = 'https://my-site.com/docs/'

After the HTML finishes building, **sphinx-sitemap** will output the location of the sitemap::

    sitemap.xml was generated for URL https://my-site.com/docs/ in /path/to/_build/sitemap.xml

.. tip:: Make sure to confirm the accuracy of the sitemap after installs and upgrades.


See :doc:`configuration` for more information about how to use **sphinx-sitemap**.

.. toctree::
   :maxdepth: 2

   configuration
   seo
   configuration-values
   contributing
   changelog


.. _sitemaps.org: https://www.sitemaps.org/protocol.html
.. _Sphinx: http://sphinx-doc.org/

.. |PyPI version| image:: https://img.shields.io/pypi/v/sphinx-sitemap.svg
   :target: https://pypi.python.org/pypi/sphinx-sitemap
   :alt: Latest PyPi Version
.. |Conda Forge| image:: https://img.shields.io/conda/vn/conda-forge/sphinx-sitemap.svg
   :target: https://anaconda.org/conda-forge/sphinx-sitemap
   :alt: Latest Conda Forge version
.. |Downloads| image:: https://pepy.tech/badge/sphinx-sitemap/month
    :target: https://pepy.tech/project/sphinx-sitemap
    :alt: PyPi Downloads per month
.. |Parallel Safe| image:: https://img.shields.io/badge/parallel%20safe-true-brightgreen
   :target: #
   :alt: Parallel read/write safe
.. |GitHub Stars| image:: https://img.shields.io/github/stars/jdillard/sphinx-sitemap?style=social
   :target: https://github.com/jdillard/sphinx-sitemap
   :alt: GitHub Repo stars
