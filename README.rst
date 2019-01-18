Sphinx Sitemap Generator Extension
==================================

A `Sphinx`_ extension to silently generate a `sitemaps.org`_ compliant sitemap for
the HTML version of your Sphinx Documentation.

|Build Status| |PyPI version| |License: MIT|

Installing
----------

Directly install via pip by using::

    pip install sphinx-sitemap

Add ``sphinx_sitemap`` to the **extensions** array in your Sphinx **conf.py**.
For example::

    extensions = ['sphinx_sitemap']

Set the value of **html_baseurl** in your Sphinx **conf.py** to the current
base URL of your documentation. For example::

    html_baseurl = 'https://my-site.com/docs/'

**Note:** `html_baseurl` was introduced in Sphinx 1.8.0. If you are using a
version prior to that you must set your base URL to `site_url` instead.

For multilingual sitemaps, you have to generate a sitemap per language/locale
and then manually add them to a `sitemapindex`_ file.

The extension will look at the `language` config value for the current language
being built, and `locale_dirs` for the directory of alternate languages.

**Note:** It is currently opinionated, in that it will also use the `version`
config value in the generated URL.

The end result is something like the following for each language/version build::

  <?xml version="1.0" encoding="utf-8"?>
  <urlset xmlns:xhtml="http://www.w3.org/1999/xhtml" xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
    <url>
      <loc>https://my-site.com/docs/en/latest/index.html</loc>
      <xhtml:link href="https://my-site.com/docs/es/latest/index.html" hreflang="es" rel="alternate"/>
      <xhtml:link href="https://my-site.com/docs/fr/latest/index.html" hreflang="fr" rel="alternate"/>
      <xhtml:link href="https://my-site.com/docs/en/latest/index.html" hreflang="en" rel="alternate"/>
    </url>
    <url>
      <loc>https://my-site.com/docs/en/latest/about.html</loc>
      <xhtml:link href="https://my-site.com/docs/es/latest/about.html" hreflang="es" rel="alternate"/>
      <xhtml:link href="https://my-site.com/docs/fr/latest/about.html" hreflang="fr" rel="alternate"/>
      <xhtml:link href="https://my-site.com/docs/en/latest/index.html" hreflang="en" rel="alternate"/>
    </url>
  </urlset>

See Who Is Using It
-------------------

You can use `GitHub search`_ to see who is using **sphinx-sitemap**.

Contributing
------------

Pull Requests welcome! See `CONTRIBUTING`_ for instructions on how best to contribute.

Maintaining PyPI Version
------------------------

These are the steps for making a new Python package release.

#. Rev versions in **sphinx_sitemap/version.py** and **setup.py**.
#. Update **CHANGELOG.md**
#. Create a tag and push to GitHub::

       git tag -a vX.Y.Z -m "Release vX.Y.Z"
       git push --tags origin master

#. Upload the latest distribution::

       python setup.py sdist upload -r pypi

License
-------

**sphinx-sitemap** is made available under a **MIT license**; see `LICENSE`_ for
details.

Originally based on the sitemap generator in the `guzzle_sphinx_theme`_ project,
also licensed under the MIT license.

.. _CONTRIBUTING: CONTRIBUTING.md
.. _GitHub search: https://github.com/search?utf8=%E2%9C%93&q=sphinx-sitemap+extension%3Atxt&type=
.. _guzzle_sphinx_theme: https://github.com/guzzle/guzzle_sphinx_theme
.. _LICENSE: LICENSE
.. _sitemapindex: https://support.google.com/webmasters/answer/75712?hl=en
.. _sitemaps.org: https://www.sitemaps.org/protocol.html
.. _Sphinx: http://sphinx-doc.org/

.. |Build Status| image:: https://travis-ci.org/jdillard/sphinx-sitemap.svg?branch=master
   :target: https://travis-ci.org/jdillard/sphinx-sitemap
.. |PyPI version| image:: https://img.shields.io/pypi/v/sphinx-sitemap.svg
   :target: https://pypi.python.org/pypi/sphinx-sitemap
.. |License: MIT| image:: https://img.shields.io/badge/License-MIT-blue.svg
   :target: https://github.com/jdillard/sphinx-sitemap/blob/master/LICENSE
