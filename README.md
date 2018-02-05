# Sphinx Sitemap Generator Extension

*[Sphinx](http://sphinx-doc.org/) extension to silently generate a sitemaps.org compliant sitemap for the HTML version of your Sphinx Documentation.*

[![Build Status](https://travis-ci.org/jdillard/sphinx-sitemap.svg?branch=master)](https://travis-ci.org/jdillard/sphinx-sitemap)
[![PyPI version](https://img.shields.io/pypi/v/sphinx-sitemap.svg)](https://pypi.python.org/pypi/sphinx-sitemap)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://github.com/jdillard/sphinx-sitemap/blob/master/LICENSE)

## Installing

Directly install via pip by using:

    pip install sphinx_sitemap

Set the value of **site_url** in your Sphinx **conf.py** to the current base URL of your documentation. For example:

    #site base url
    site_url = 'https://my-site.com/docs/'

Add `sphinx_sitemap` to the **extensions** array in your Sphinx **conf.py**. For example:

    extensions = ['sphinx_sitemap']
    
> **Note:** sphinx-sitemap supports Sphinx 1.2 and later, and Python 2.7, 3.3, and 3.4.

## License

sphinx-sitemap is made available under a MIT license; see LICENSE for details.

Originally based on the sitemap generator in the [guzzle_sphinx_theme](https://github.com/guzzle/guzzle_sphinx_theme) project licensed under the MIT license.
