Sphinx Sitemap Generator Extension
==================================

A `Sphinx`_ extension to silently generate a `sitemaps.org`_ compliant sitemap for
the HTML version of your Sphinx Documentation.

|Build Status| |PyPI version| |License: MIT|

Installing
----------

Directly install via pip by using::

    pip install sphinx-sitemap

Add ``sphinx_sitemap`` to the `extensions`_ array in your Sphinx **conf.py**.
For example::

    extensions = ['sphinx_sitemap']

Set the value of `html_baseurl`_ in your Sphinx **conf.py** to the current
base URL of your documentation with a trailing slash. For example::

    html_baseurl = 'https://my-site.com/docs/'

Multilingual Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^

For multilingual sitemaps, you have to generate a sitemap per language/locale
and then manually add their locations to a `sitemapindex`_ file.

The extension will look at the `language`_ config value for the current language
being built, and the `locale_dirs`_ value for the directory for alternate languages,
so make sure those are set.

**Note:** The extension is currently opinionated, in that it will also use the
`version`_ config value in the generated URL. Setting it to ``latest`` is appropriate
for most use cases.

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
  
Getting the Most out of the Sitemap
-----------------------------------

#. Add a **robots.txt** file in the **source** directory which contains a link to
   the sitemap or sitemapindex. For example::

     User-agent: *

     Sitemap: https://my-site.com/docs/sitemap.xml
   
  
   Then, add **robots.txt** to the `html_extra_path`_ config value::

     html_extra_path = ['robots.txt']
     
#. Submit the sitemap or sitemapindex to the appropriate search engine tools.

See Who Is Using It
-------------------

You can use `GitHub search`_ or `libraries.io`_ to see who is using **sphinx-sitemap**.

Contributing
------------

Pull Requests welcome! See `CONTRIBUTING`_ for instructions on how best to contribute.

Maintaining PyPI Version
------------------------

These are the steps, to be run by the maintainer, for making a new Python package release.

#. Rev versions in **sphinx_sitemap/version.py** and **setup.py**.
#. Update **CHANGELOG.md**
#. Create a tag and push to GitHub::

       git tag -a vX.Y.Z -m "Release vX.Y.Z"
       git push --tags origin master

#. Create latest distribution locally::

       python setup.py sdist
       
#. Upload to the test pypi.org repository::

       twine upload --repository-url https://test.pypi.org/legacy/ dist/*
       
#. Upload to the production pypi.org repository::

       twine upload dist/*

License
-------

**sphinx-sitemap** is made available under a **MIT license**; see `LICENSE`_ for
details.

Originally based on the sitemap generator in the `guzzle_sphinx_theme`_ project,
also licensed under the MIT license.

.. _CONTRIBUTING: CONTRIBUTING.md
.. _extensions: https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-extensions
.. _GitHub search: https://github.com/search?utf8=%E2%9C%93&q=sphinx-sitemap+extension%3Atxt&type=
.. _guzzle_sphinx_theme: https://github.com/guzzle/guzzle_sphinx_theme
.. _html_baseurl: https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-html_baseurl
.. _html_extra_path: http://www.sphinx-doc.org/en/master/usage/configuration.html#confval-html_extra_path
.. _language: https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-language
.. _libraries.io: https://libraries.io/pypi/sphinx-sitemap
.. _LICENSE: LICENSE
.. _locale_dirs: https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-locale_dirs
.. _sitemapindex: https://support.google.com/webmasters/answer/75712?hl=en
.. _sitemaps.org: https://www.sitemaps.org/protocol.html
.. _Sphinx: http://sphinx-doc.org/
.. _version: https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-version

.. |Build Status| image:: https://travis-ci.org/jdillard/sphinx-sitemap.svg?branch=master
   :target: https://travis-ci.org/jdillard/sphinx-sitemap
.. |PyPI version| image:: https://img.shields.io/pypi/v/sphinx-sitemap.svg
   :target: https://pypi.python.org/pypi/sphinx-sitemap
.. |License: MIT| image:: https://img.shields.io/badge/License-MIT-blue.svg
   :target: https://github.com/jdillard/sphinx-sitemap/blob/master/LICENSE
