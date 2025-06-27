Getting the Most out of the Sitemap
===================================

Search Engine Optimization
--------------------------

Using robots.txt
^^^^^^^^^^^^^^^^

Add a **robots.txt** file in the **source** directory which has a link to the ``sitemap.xml`` or ``sitemapindex.xml`` file. For example::

  User-agent: *

  Sitemap: https://my-site.com/docs/sitemap.xml

Then, add **robots.txt** to :confval:`html_extra_path` in **conf.py**:

.. code-block:: python

  html_extra_path = ['robots.txt']

Submit Sitemap to Search Engines
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Submit the ``sitemap.xml`` or ``sitemapindex.xml`` to the appropriate search engine tools.

Site Search Optimization
------------------------

Site search crawlers can also take advantage of sitemaps as starting points for crawling.

Examples:

- `Algolia`_

.. _Algolia: https://www.algolia.com/doc/tools/crawler/apis/configuration/sitemaps/

.. _rag-ingestion:

RAG (Retrieval-Augmented Generation) Ingestion
-----------------------------------------------

The sitemap can be used as a structured data source for RAG systems to efficiently discover and ingest documentation content.

- **Comprehensive Discovery**: The sitemap provides a complete list of all documentation pages, ensuring no content is missed during ingestion
- **Incremental Updates**: Use the ``<lastmod>`` timestamps to identify recently updated content and refresh only those embeddings in your RAG system.
