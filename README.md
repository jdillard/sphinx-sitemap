# Sphinx Sitemap Generator Extension

*[Sphinx](http://sphinx-doc.org/) extension to silently generate a sitemaps.org compliant sitemap for the HTML version of your Sphinx Documentation.*

[![Build Status](https://travis-ci.org/jdillard/sphinx-sitemap.svg?branch=master)](https://travis-ci.org/jdillard/sphinx-sitemap)

## Installing

1. Add/set the value of **base_url** in your Sphinx **conf.py** to the current base URL of your documentation. For example, `https://my-site.com/docs/`.

2. Copy the **sphinx_sitemap** directory into your extensions directory or **sys.path**, then add `sphinx_sitemap` to the **extensions** array in your Sphinx **conf.py**.

> **Note:** sphinx-sitemap supports Sphinx 1.2 and later, and Python 2.7, 3.3, and 3.4.

## License

sphinx-sitemap is made available under a MIT license; see LICENSE for details.

Originally based on the sitemap generator in the [guzzle_sphinx_theme](https://github.com/guzzle/guzzle_sphinx_theme) project licensed under the MIT license.
