Sphinx Sitemap Generator Extension
==================================

A `Sphinx`_ extension to silently generate a sitemaps.org compliant sitemap for
the HTML version of your Sphinx Documentation.

|Build Status| |PyPI version| |License: MIT|

Installing
----------

Directly install via pip by using::

    pip install sphinx_sitemap

Set the value of **site_url** in your Sphinx **conf.py** to the current base URL
of your documentation. For example::

    #site base url
    site_url = 'https://my-site.com/docs/'

Add ``sphinx_sitemap`` to the **extensions** array in your Sphinx **conf.py**.
For example::

    extensions = ['sphinx_sitemap']
    
See Who Is Using It
-------------------

You can use `GitHub search`_ to see who is using **sphinx-sitemap**.

Maintaining PyPI Version
------------------------

These are the steps for making a new Python package release.

#. Rev versions in **sphinx_sitemap/version.py** and **setup.py**.
#. Create a tag and push to GitHub::

       git tag -a vX.Y.Z -m "Release vX.Y.Z"
       git push --tags origin master

#. Upload the latest distribution::

       python setup.py sdist upload -r pypi

License
-------

sphinx-sitemap is made available under a MIT license; see LICENSE for details.

Originally based on the sitemap generator in the `guzzle_sphinx_theme`_ project
licensed under the MIT license.

.. _Sphinx: http://sphinx-doc.org/
.. _GitHub search: https://github.com/search?utf8=%E2%9C%93&q=sphinx-sitemap+extension%3Atxt&type=
.. _guzzle_sphinx_theme: https://github.com/guzzle/guzzle_sphinx_theme

.. |Build Status| image:: https://travis-ci.org/jdillard/sphinx-sitemap.svg?branch=master
   :target: https://travis-ci.org/jdillard/sphinx-sitemap
.. |PyPI version| image:: https://img.shields.io/pypi/v/sphinx-sitemap.svg
   :target: https://pypi.python.org/pypi/sphinx-sitemap
.. |License: MIT| image:: https://img.shields.io/badge/License-MIT-blue.svg
   :target: https://github.com/jdillard/sphinx-sitemap/blob/master/LICENSE
