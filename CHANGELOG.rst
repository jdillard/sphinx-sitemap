.. vale off

Changelog
=========

2.6.0
-----

*Release date: 2024-04-28*

* |:wrench:| MAINT: Fix deprecated sphinx.testing.path
  `#83 <https://github.com/jdillard/sphinx-sitemap/pull/83>`_
* Drop test support for Python 3.7 and Sphinx 2, 3, and 4.
* |:sparkles:| NEW: Add sitemap_excludes configuration
  `#91 <https://github.com/jdillard/sphinx-sitemap/pull/91>`_

2.5.1
-----

*Release date: 2023-08-17*

* |:bug:| FIX: Fix Path use for Sphinx 7.2
  `#70 <https://github.com/jdillard/sphinx-sitemap/pull/70>`_
* |:bug:| FIX: Fix incremental building by preventing multiprocessing queue from being pickled with environment
  `#62 <https://github.com/jdillard/sphinx-sitemap/pull/62>`_
* |:wrench:| MAINT: Add docstrings and type hints
  `#61 <https://github.com/jdillard/sphinx-sitemap/pull/61>`_

2.5.0
-----

*Release date: 2023-01-28*

* |:books:| DOCS: Calculate version for sitemap based on current tag
  `#53 <https://github.com/jdillard/sphinx-sitemap/pull/53>`_
* |:test_tube:| TESTS: Add Sphinx 6 env to tox
  `#55 <https://github.com/jdillard/sphinx-sitemap/pull/55>`_
* |:sparkles:| NEW: Add support for Sphinx config "html_file_suffix"
  `#57 <https://github.com/jdillard/sphinx-sitemap/pull/57>`_
* |:books:| DOCS: Add site search optimization
  `#58 <https://github.com/jdillard/sphinx-sitemap/pull/58>`_

2.4.0
-----

*Release date: 2022-12-26*

* |:books:| DOCS: Add ReadTheDocs docs
  `#45 <https://github.com/jdillard/sphinx-sitemap/pull/45>`_
* |:wrench:| MAINT: General code clean up
  `#46 <https://github.com/jdillard/sphinx-sitemap/pull/46>`_
* |:sparkles:| NEW: Add support for parallel mode
  `#47 <https://github.com/jdillard/sphinx-sitemap/pull/47>`_
* |:test_tube:| TESTS: Add tests for ``dirhtml`` builder
  `#48 <https://github.com/jdillard/sphinx-sitemap/pull/48>`_
* |:test_tube:| TESTS: Add vale support for docs
  `#49 <https://github.com/jdillard/sphinx-sitemap/pull/49>`_
* |:bug:| FIX: Fix wheel includes so they don't include docs and tests
  `#51 <https://github.com/jdillard/sphinx-sitemap/pull/51>`_
* |:books:| DOCS: Add write-good and improve writing
  `#52 <https://github.com/jdillard/sphinx-sitemap/pull/52>`_

2.3.0
-----

*Release date: 2022-12-21*

* |:wrench:| MAINT: Clean up how package versions are handled
* |:test_tube:| TESTS: Install pre-commit with ``isort``, ``black``, and ``flake8``
  `#35 <https://github.com/jdillard/sphinx-sitemap/pull/35>`_
* |:books:| DOCS: Improve the wording of the README to help with issues upgrading to Sphinx 5
  `#36 <https://github.com/jdillard/sphinx-sitemap/pull/36>`_
* |:bug:| FIX: Follow correct format for multilingual sitemaps
  `#38 <https://github.com/jdillard/sphinx-sitemap/pull/38>`_
* |:wrench:| MAINT: Update the build process
  `#39 <https://github.com/jdillard/sphinx-sitemap/pull/39>`_
* |:test_tube:| TESTS: Add testing infrastructure
  `#41 <https://github.com/jdillard/sphinx-sitemap/pull/41>`_
  `#42 <https://github.com/jdillard/sphinx-sitemap/pull/42>`_
* |:wrench:| MAINT: Use logging for all logging messages
  `#40 <https://github.com/jdillard/sphinx-sitemap/pull/40>`_

2.2.1
-----

*Release date: 2022-11-11*

* |:books:| DOCS: Fix :confval:`sitemap_url_scheme` default value in **README** file
  `#32 <https://github.com/jdillard/sphinx-sitemap/pull/32>`_
* |:wrench:| MAINT: Clean up package classifiers
* |:wrench:| MAINT: Add **LICENSE** to source distributions
  `#27 <https://github.com/jdillard/sphinx-sitemap/pull/27>`_
* |:books:| DOCS: Add Conda Forge badge to **README** file

2.2.0
------

*Release date: 2020-08-05*

* |:wrench:| MAINT: Add ``parallel_write_safe`` flag and set to `False`
  `#20 <https://github.com/jdillard/sphinx-sitemap/issues/20>`_.
* |:sparkles:| Add :confval:`sitemap_locales` that creates an allow list of locales
  `#25 <https://github.com/jdillard/sphinx-sitemap/pull/25>`_.
* |:sparkles:| Add :confval:`sitemap_filename` that allows for custom sitemap name
  `#26 <https://github.com/jdillard/sphinx-sitemap/pull/26>`_.

2.1.0
-----

*Release date: 2020-02-22*

* |:bug:| FIX: Make sure the regional variants for the ``hreflang`` attribute are valid
  `#19 <https://github.com/jdillard/sphinx-sitemap/issues/19>`_.

2.0.0
-----

*Release date: 2020-02-19*

* |:sparkles:| NEW: Add :confval:`sitemap_url_scheme` that allows the URL scheme to be customized with a default of ``{version}{lang}{link}``
  `#22 <https://github.com/jdillard/sphinx-sitemap/issues/22>`_.

  .. note:: This has the potential to be a breaking change depending on how the ``version`` and ``language`` values are set. **Confirm the accuracy of the sitemap after upgrading**.

1.1.0
-----

*Release date: 2019-12-12*

* |:sparkles:| NEW: Add support for ``DirectoryHTMLBuilder``.
* |:wrench:| MAINT: Remove unused ``HTMLTranslator`` import.
* |:sparkles:| NEW: Make ``version`` and ``language`` each optional.
* |:wrench:| MAINT: Add license to **setup.py**.
* |:wrench:| MAINT: Mark unsafe for parallel reading.

1.0.2
-----

*Release date: 2019-02-09*

* |:wrench:| MAINT: Add ``html_baseurl`` if it doesn't exist for sphinx versions prior to 1.8.0.

1.0.1
-----

*Release date: 2019-01-17*

* |:bug:| FIX: Fix for ``AttributeError: No such config value: html_baseurl`` on versions of sphinx older than 1.8.0.

1.0.0
-----

*Release date: 2019-01-17*

* |:wrench:| MAINT: Use native ``html_baseurl``, instead of the custom ``site_url``. It checks for both for backwards compatibility.
* |:sparkles:| NEW: Add support for multiple languages.

0.3.1
-----

*Release date: 2018-03-04*

* |:books:| DOCS: Add instructions on maintaining PyPI version to the docs

0.3.0
-----

*Release date: 2018-03-04*

* |:wrench:| MAINT: Remove unnecessary ``HTMLTranslator``.
* |:books:| DOCS: Improve documentation

0.2
---

*Release date: 2017-11-28*

* |:wrench:| MAINT: Fix PyPI description

0.1
---

*Release date: 2017-11-28*

* Initial Release |:tada:|
