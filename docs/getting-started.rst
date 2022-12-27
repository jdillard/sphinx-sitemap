Getting Started
===============

Installation
------------

Directly install via ``pip`` by using::

    pip install sphinx-sitemap

Or with ``conda`` via ``conda-forge``::

    conda install -c conda-forge sphinx-sitemap

Useage
------

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
