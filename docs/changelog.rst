Changelog
=========

2.4.0
-----

*Release date: TBD*

* Add ReadTheDocs docs
  `#45 <https://github.com/jdillard/sphinx-sitemap/pull/45>`_
* General code clean up
  `#46 <https://github.com/jdillard/sphinx-sitemap/pull/46>`_
* Add support for parallel mode
  `#47 <https://github.com/jdillard/sphinx-sitemap/pull/47>`_
* Add tests for ``dirhtml`` builder
  `#48 <https://github.com/jdillard/sphinx-sitemap/pull/48>`_
* Add vale support for docs
  `#49 <https://github.com/jdillard/sphinx-sitemap/pull/49>`_
* Fix wheel includes so they don't include docs and tests
  `#51 <https://github.com/jdillard/sphinx-sitemap/pull/51>`_

2.3.0
-----

*Release date: 2022-12-21*

* Clean up how package versions are handled
* Install pre-commit with ``isort``, ``black``, and ``flake8``
  `#35 <https://github.com/jdillard/sphinx-sitemap/pull/35>`_
* Improve the wording of the README to help with issues upgrading to Sphinx 5
  `#36 <https://github.com/jdillard/sphinx-sitemap/pull/36>`_
* Follow correct format for multilingual sitemaps
  `#38 <https://github.com/jdillard/sphinx-sitemap/pull/38>`_
* Update the build process
  `#39 <https://github.com/jdillard/sphinx-sitemap/pull/39>`_
* Add testing infrastructure
  `#41 <https://github.com/jdillard/sphinx-sitemap/pull/41>`_
  `#42 <https://github.com/jdillard/sphinx-sitemap/pull/42>`_
* Use logging for all logging messages
  `#40 <https://github.com/jdillard/sphinx-sitemap/pull/40>`_

2.2.1
-----

*Release date: 2022-11-11*

* Fix :confval:`sitemap_url_scheme` default value in **README** file
  `#32 <https://github.com/jdillard/sphinx-sitemap/pull/32>`_
* Clean up package classifiers
* Add **LICENSE** to source distributions
  `#27 <https://github.com/jdillard/sphinx-sitemap/pull/27>`_
* Add Conda Forge badge to **README** file

2.2.0
------

*Release date: 2020-08-05*

* Add ``parallel_write_safe`` flag and set to `False`
  `#20 <https://github.com/jdillard/sphinx-sitemap/issues/20>`_.
* Add :confval:`sitemap_locales` that creates an allow list of locales
  `#25 <https://github.com/jdillard/sphinx-sitemap/pull/25>`_.
* Add :confval:`sitemap_filename` that allows for custom sitemap name
  `#26 <https://github.com/jdillard/sphinx-sitemap/pull/26>`_.

2.1.0
-----

*Release date: 2020-02-22*

* Make sure the regional variants for the ``hreflang`` attribute are valid
  `#19 <https://github.com/jdillard/sphinx-sitemap/issues/19>`_.

2.0.0
-----

*Release date: 2020-02-19*

* Add :confval:`sitemap_url_scheme` that allows the URL scheme to be
  customized with a default of ``{version}{lang}{link}``
  `#22 <https://github.com/jdillard/sphinx-sitemap/issues/22>`_.

  .. note:: This has the potential to be a breaking change depending on
     how the ``version`` and ``language`` values are set. **Confirm the accuracy
     of the sitemap after upgrading**.

1.1.0
-----

*Release date: 2019-12-12*

* Add support for ``DirectoryHTMLBuilder``.
* Remove unused ``HTMLTranslator`` import.
* Make ``version`` and ``language`` each optional.
* Add license to **setup.py**.
* Mark unsafe for parallel reading.

1.0.2
-----

*Release date: 2019-02-09*

* Add ``html_baseurl`` if it doesn't exist for sphinx versions prior
  to 1.8.0.

1.0.1
-----

*Release date: 2019-01-17*

* Fix for ``AttributeError: No such config value: html_baseurl`` on versions of
  sphinx older than 1.8.0.

1.0.0
-----

*Release date: 2019-01-17*

* Use native ``html_baseurl``, instead of the custom ``site_url``. It
  checks for both for backwards compatibility.
* Add support for multiple languages.

0.3.1
-----

*Release date: 2018-03-04*

* Add instructions on maintaining PyPI version to the docs

0.3.0
-----

*Release date: 2018-03-04*

* Remove unnecessary ``HTMLTranslator``.
* Improve documentation

0.2
---

*Release date: 2017-11-28*

* Fix PyPI description

0.1
---

*Release date: 2017-11-28*

* Initial Release
