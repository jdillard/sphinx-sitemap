Getting the Most out of the Sitemap
===================================

Using robots.txt
----------------

Add a **robots.txt** file in the **source** directory which contains a link to the **sitemap.xml** or **sitemapindex.xml** file. For example::

  User-agent: *

  Sitemap: https://my-site.com/docs/sitemap.xml

Then, add **robots.txt** to :confval:`html_extra_path` in **conf.py**:

.. code-block:: python

  html_extra_path = ['robots.txt']

Submit Sitemap to Search Engines
--------------------------------

Submit the **sitemap.xml** or **sitemapindex.xml** to the appropriate search engine tools.
