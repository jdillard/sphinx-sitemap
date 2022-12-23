Advanced Configuration
======================

.. _config_customizing_url_scheme:

Customizing the URL Scheme
^^^^^^^^^^^^^^^^^^^^^^^^^^

The default URL format is ``{lang}{version}{link}``. ``{lang}`` and ``{version}`` are controlled
by the :confval:`language` and :confval:`version` config variables.

.. important:: As of Sphinx version 5, the ``language`` config value defaults to ``"en"``, if that
   makes the default scheme produce the incorrect url, then change the default behavior.

To change the default behavior, set the value of :confval:`sitemap_url_scheme` in **conf.py** to the
desired format. For example:

.. code-block:: python

   sitemap_url_scheme = "{link}"

Or for nested deployments, something like:

.. code-block:: python

   sitemap_url_scheme = "{version}{lang}subdir/{link}"

.. note:: The extension is currently opinionated, in that it automatically
   appends trailing slashes to both the ``language`` and ``version`` values. You
   can also omit values from the scheme for desired behavior.


.. _config_changing_filename:

Changing the Filename
^^^^^^^^^^^^^^^^^^^^^

Set :confval:`sitemap_filename` in **conf.py** to the desired filename, for example:

.. code-block:: python

   sitemap_filename = "sitemap.xml"

Supporting Multiple Versions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For multiversion sitemaps, it is required to generate a sitemap per version and
then manually add their locations to a `sitemapindex`_ file.

The extension will look at the :confval:`version` config value for the current version
being built, so make sure that is set.

.. note:: When using multiple versions, it is best practice to set the canonical
   URL in the theme layout of all versions to the latest version of that page::

     <link rel="canonical" href="https://my-site.com/docs/latest/index.html"/>

.. _config_supporting_multiple_languages:

Supporting Multiple Languages
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For multilingual sitemaps, generate a sitemap per language/locale and then manually
add their locations to a `sitemapindex`_ file.

The primary language is set by the :confval:`language` config value. Alternative languages
are either manually set by :confval:`sitemap_locales` option or auto-detected by the
extension from the :confval:`locale_dirs` config value, so make sure one of those is set.

``sitemap_locales`` configuration is to specify a list of locales to include in
the sitemap. For instance, if a third-party extension adds unsupported langauges to
**locale_dirs**, or to allow locales to reach a certain translated percentage before
making them public. For example, if the primary language is `en`, and a list with
`es` and `fr` translations specified, the sitemap look like this::

    <?xml version="1.0" encoding="utf-8"?>
      <urlset xmlns:xhtml="http://www.w3.org/1999/xhtml" xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
        <url>
          <loc>https://my-site.com/docs/en/index.html</loc>
          <xhtml:link href="https://my-site.com/docs/es/index.html" hreflang="es" rel="alternate"/>
          <xhtml:link href="https://my-site.com/docs/fr/index.html" hreflang="fr" rel="alternate"/>
          <xhtml:link href="https://my-site.com/docs/en/index.html" hreflang="en" rel="alternate"/>
        </url>
        <url>
            <loc>https://my-site.com/docs/en/about.html</loc>
            <xhtml:link href="https://my-site.com/docs/es/about.html" hreflang="es" rel="alternate"/>
            <xhtml:link href="https://my-site.com/docs/fr/about.html" hreflang="fr" rel="alternate"/>
            <xhtml:link href="https://my-site.com/docs/en/about.html" hreflang="en" rel="alternate"/>
        </url>
      </urlset>

When the sitemap locales are limited:

.. code-block:: python

   sitemap_locales = ['en', 'es']

The end result is something like the following for each language/version build::

  <?xml version="1.0" encoding="utf-8"?>
  <urlset xmlns:xhtml="http://www.w3.org/1999/xhtml" xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
    <url>
      <loc>https://my-site.com/docs/en/index.html</loc>
      <xhtml:link href="https://my-site.com/docs/es/index.html" hreflang="es" rel="alternate"/>
      <xhtml:link href="https://my-site.com/docs/en/index.html" hreflang="en" rel="alternate"/>
    </url>
    <url>
      <loc>https://my-site.com/docs/en/about.html</loc>
      <xhtml:link href="https://my-site.com/docs/es/about.html" hreflang="es" rel="alternate"/>
      <xhtml:link href="https://my-site.com/docs/en/about.html" hreflang="en" rel="alternate"/>
    </url>
  </urlset>

When the special value of ``[None]`` is set:

.. code-block:: python

   sitemap_locales = [None]

only the primary language is generated::

  <?xml version="1.0" encoding="utf-8"?>
  <urlset xmlns:xhtml="http://www.w3.org/1999/xhtml" xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
    <url>
      <loc>https://my-site.com/docs/en/index.html</loc>
    </url>
    <url>
      <loc>https://my-site.com/docs/en/about.html</loc>
    </url>
  </urlset>


.. _sitemapindex: https://support.google.com/webmasters/answer/75712?hl=en
.. _sitemaps.org: https://www.sitemaps.org/protocol.html
