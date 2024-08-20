Advanced Configuration
======================

.. _configuration_customizing_url_scheme:

Customizing the URL Scheme
^^^^^^^^^^^^^^^^^^^^^^^^^^

:confval:`sitemap_url_scheme` defaults to ``{lang}{version}{link}``, where ``{lang}`` and ``{version}`` get set by :confval:`language` and :confval:`version` in **conf.py**.

.. important:: As of Sphinx version 5, ``language`` defaults to ``"en"``, if that
   makes the default scheme produce the incorrect URL, then change the default behavior.

To change the default behavior, set the value of :confval:`sitemap_url_scheme` in **conf.py** to the
desired format. For example:

.. code-block:: python

   sitemap_url_scheme = "{link}"

Or for nested deployments, something like:

.. code-block:: python

   sitemap_url_scheme = "{version}{lang}subdir/{link}"

.. note:: The extension automatically appends trailing slashes to both the ``language`` and ``version`` values.
   You can also omit values from the scheme for desired behavior.


.. _configuration_changing_filename:

Changing the Filename
^^^^^^^^^^^^^^^^^^^^^

Set :confval:`sitemap_filename` in **conf.py** to the desired filename, for example:

.. code-block:: python

   sitemap_filename = "sitemap.xml"

Version Support
^^^^^^^^^^^^^^^

:confval:`version` specifies the version of the sitemap.
For multi-version sitemaps, generate a sitemap per version and then manually add each to a `sitemapindex.xml`_ file.

Tagged Releases
~~~~~~~~~~~~~~~

For a tagged release deploy strategy where the ``latest`` gets created from head of the branch and versions get created from tagged commits, check to see if the current commit matches the release tag regex and set :confval:`version` accordingly.

.. code-block:: python

   # check if the current commit is tagged as a release (vX.Y.Z) and set the version
   GIT_TAG_OUTPUT = subprocess.check_output(["git", "tag", "--points-at", "HEAD"])
   current_tag = GIT_TAG_OUTPUT.decode().strip()
   if re.match(r"^v(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)$", current_tag):
       version = current_tag
   else:
       version = "latest"

.. tip:: Set the canonical URL in the theme layout of all versions to the latest version of that page, for example:

   .. code-block:: html

      <link rel="canonical" href="https://my-site.com/docs/latest/index.html"/>

.. _configuration_supporting_multiple_languages:

Language Support
^^^^^^^^^^^^^^^^

:confval:`language` specifies the primary language. Any alternative languages get detected using the contents of :confval:`locale_dirs`.

For example, with a primary language of **en**, and **es** and **fr** as detected translations, the sitemap look like this:

.. code-block:: xml

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

Use :confval:`sitemap_locales` to manually specify a list of locales to include in the sitemap:

.. code-block:: python

   sitemap_locales = ['en', 'es']

The end result looks something like the following for each language/version build:

.. code-block:: xml

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

To generate the primary language with no alternatives, set :confval:`sitemap_locales` to ``[None]``:

.. code-block:: python

   sitemap_locales = [None]

For multilingual sitemaps, generate a sitemap per language and then manually add each to a `sitemapindex.xml`_ file.

.. _configuration_excluding_pages:

Excluding Pages
^^^^^^^^^^^^^^^

To exclude a set of pages, add each page's path to ``sitemap_exclude``:

.. code-block:: python

   sitemap_excludes = [
       "search.html",
       "genindex.html",
   ]

.. _configuration_lastmod:

Adding Last Modification Date
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To add the date of the last page modification set ``sitemap_lastmod`` a string
representing the last modification date.

.. code-block:: python

   sitemap_lastmod = "2024-08-13"
   # or
   import datetime
   sitemap_lastmod = f"{datetime.datetime.now():%Y-%m-%d}"

.. _sitemapindex.xml: https://support.google.com/webmasters/answer/75712?hl=en
.. _sitemaps.org: https://www.sitemaps.org/protocol.html
