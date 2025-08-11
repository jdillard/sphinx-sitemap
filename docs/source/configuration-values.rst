Project Configuration Values
============================

A list of of possible configuration values to configure in **conf.py**:

.. confval:: sitemap_url_scheme

   - **Type**: string
   - **Default**: ``'{lang}{version}{link}'``
   - **Description**: The scheme used for URL structure.
     See :ref:`configuration_customizing_url_scheme` for more information.

   .. versionadded:: 2.0.0

.. confval:: sitemap_filename

   - **Type**: string
   - **Default**: ``'sitemap.xml'``
   - **Description**: The filename used for the sitemap.
     See :ref:`configuration_changing_filename` for more information.

   .. versionadded:: 2.2.0

.. confval:: sitemap_locales

   - **Type**: list of strings
   - **Default**: ``[]`` (empty list)
   - **Description**: The list of locales to include in the sitemap.
     See :ref:`configuration_supporting_multiple_languages` for more information.

   .. versionadded:: 2.2.0

.. confval:: sitemap_excludes

   - **Type**: list of strings
   - **Default**: ``[]`` (empty list)
   - **Description**: The list of pages to exclude from the sitemap.
     Supports wildcard patterns.
     See :ref:`configuration_excluding_pages` for more information.

   .. versionadded:: 2.6.0

   .. versionchanged:: 2.8.0
      Added support for glob patterns using Unix-style wildcards.

.. confval:: sitemap_show_lastmod

   - **Type**: boolean
   - **Default**: ``False``
   - **Description**: Add ``<lastmod>`` to sitemap based on last updated time according to Git for each page.
     See :ref:`configuration_lastmod` for more information.

   .. versionadded:: 2.7.0
