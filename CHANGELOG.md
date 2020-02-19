Changelog
=========

latest
------

*Release date: TBD*

* Add `sitemap_url_scheme` config value that allows the url scheme to be
  customized with a default of `{version}{lang}{link}` [#22](https://github.com/jdillard/sphinx-sitemap/issues/22).

1.1.0
-----

*Release date: 2019-12-12*

* Add support for `DirectoryHTMLBuilder`.
* Remove unused `HTMLTranslator` import.
* Make `version` and `language` config values each optional.
* Add license to **setup.py**.
* Mark unsafe for parallel reading.

1.0.2
-----

*Release date: 2019-02-09*

* Add `html_baseurl` config value if it doesn't exist for sphinx versions prior
  to 1.8.0.

1.0.1
-----

*Release date: 2019-01-17*

* Fix for `AttributeError: No such config value: html_baseurl` on versions of
  sphinx older than 1.8.0.

1.0.0
-----

*Release date: 2019-01-17*

* Use native `html_baseurl` config value, instead of the custom `site_url`. It
  checks for both for backwards compatiability.
* Add support for multiple languages.

0.3.1
-----

*Release date: 2018-03-04*

* Add instructions on maintaining PyPI version to the docs

0.3.0
-----

*Release date: 2018-03-04*

* Remove unessecary `HTMLTranslator`.
* Improve documentation

0.2
--

*Release date: 2017-11-28*

* Fix PyPI description

0.1
---

*Release date: 2017-11-28*

* Initial Release
