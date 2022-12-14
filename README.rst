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

Configuring
-----------

Set the value of `html_baseurl`_ in your Sphinx **conf.py** to the current
base URL of your documentation. For example:

.. code-block:: python

   html_baseurl = 'https://my-site.com/docs/'

After the HTML build is done, **sphinx-sitemap** will output the location of the
sitemap::

    sitemap.xml was generated for URL https://my-site.com/docs/ in /path/to/_build/sitemap.xml

**Tip:** Make sure to confirm the accuracy of the sitemap after installs and
upgrades.

Customizing the URL Scheme
^^^^^^^^^^^^^^^^^^^^^^^^^^

The default URL format is ``{lang}{version}{link}``. ``{lang}`` and ``{version}`` are controlled
by the `language`_ and `version`_ config variables.

**Note:** As of Sphinx version 5, the ``language`` config value defaults to ``"en"``, if that
makes the default scheme produce the incorrect url, then change the default behavior.

To change the default behavior, set the value of ``sitemap_url_scheme`` in **conf.py** to the
desired format. For example:

.. code-block:: python

   sitemap_url_scheme = "{link}"

Or for nested deployments, something like:

.. code-block:: python

   sitemap_url_scheme = "{version}{lang}subdir/{link}"

**Note:** The extension is currently opinionated, in that it automatically
appends trailing slashes to both the ``language`` and ``version`` values. You
can also omit values from the scheme for desired behavior.

Changing the Filename
^^^^^^^^^^^^^^^^^^^^^

Set ``sitemap_filename`` in **conf.py** to the desired filename, for example:

.. code-block:: python

   sitemap_filename = "sitemap.xml"

Versioning Configuration
^^^^^^^^^^^^^^^^^^^^^^^^

For multiversion sitemaps, it is required to generate a sitemap per version and
then manually add their locations to a `sitemapindex`_ file.

The extension will look at the `version`_ config value for the current version
being built, so make sure that is set.

**Note:** When using multiple versions, it is best practice to set the canonical
URL in the theme layout of all versions to the latest version of that page::

    <link rel="canonical" href="https://my-site.com/docs/latest/index.html"/>

Multilingual Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^

For multilingual sitemaps, generate a sitemap per language/locale and then manually
add their locations to a `sitemapindex`_ file.

The primary language is set by the `language`_ config value. Alternative languages
are either manually set by ``sitemap_locales`` option or auto-detected by the
extension from the `locale_dirs`_ config value, so make sure one of those is set.

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

Getting the Most out of the Sitemap
-----------------------------------

#. Add a **robots.txt** file in the **source** directory which contains a link to
   the sitemap or sitemapindex. For example::

     User-agent: *

     Sitemap: https://my-site.com/docs/sitemap.xml

   Then, add **robots.txt** to the `html_extra_path`_ config value:

   .. code-block:: python

     html_extra_path = ['robots.txt']

#. Submit the sitemap or sitemapindex to the appropriate search engine tools.

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
.. _html_baseurl: https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-html_baseurl
.. _html_extra_path: http://www.sphinx-doc.org/en/master/usage/configuration.html#confval-html_extra_path
.. _language: https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-language
.. _LICENSE: LICENSE
.. _locale_dirs: https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-locale_dirs
.. _sitemapindex: https://support.google.com/webmasters/answer/75712?hl=en
.. _sitemaps.org: https://www.sitemaps.org/protocol.html
.. _Sphinx: http://sphinx-doc.org/
.. _version: https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-version

.. |PyPI version| image:: https://img.shields.io/pypi/v/sphinx-sitemap.svg
   :target: https://pypi.python.org/pypi/sphinx-sitemap
.. |Conda Forge| image:: https://img.shields.io/conda/vn/conda-forge/sphinx-sitemap.svg
   :target: https://anaconda.org/conda-forge/sphinx-sitemap
.. |Downloads| image:: https://pepy.tech/badge/sphinx-sitemap/month
    :target: https://pepy.tech/project/sphinx-sitemap
.. |Code style: Black| image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/psf/black
.. |Parallel Safe| image:: https://img.shields.io/badge/parallel%20safe-False-red
