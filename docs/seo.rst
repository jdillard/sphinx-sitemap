Getting the Most out of the Sitemap
===================================

#. Add a **robots.txt** file in the **source** directory which contains a link to
   the sitemap or sitemapindex. For example::

     User-agent: *

     Sitemap: https://my-site.com/docs/sitemap.xml

   Then, add **robots.txt** to the `html_extra_path`_ config value:

   .. code-block:: python

     html_extra_path = ['robots.txt']

#. Submit the sitemap or sitemapindex to the appropriate search engine tools.


.. _html_extra_path: http://www.sphinx-doc.org/en/master/usage/configuration.html#confval-html_extra_path
