Contributing
============

Thank you for your interest in contributing to **sphinx-sitemap**!

You will need to set up a development environment to make and test your changes
before submitting them.

Setting up a dev environment
----------------------------

You need to add **sphinx-sitemap** as a `third party extension`_.

#. If your project doesn't have an extensions directory, create ``_exts`` and
   point **conf.py** to it:

   .. code-block:: python

      sys.path.append(os.path.abspath('../_exts'))

#. Copy ``sphinx_sitemap`` as a directory in your project's extensions
   directory, and rename it to ``sphinx_sitemap_dev``.

#. Add ``sphinx_sitemap_dev`` to :confval:`extensions`, or change ``sphinx_sitemap`` to
   ``sphinx_sitemap_dev`` if you already have the extension installed via ``pip``,
   in **conf.py**:

   .. code-block:: python

      extensions = ['sphinx_sitemap_dev']

You can now make changes to ``sphinx_sitemap_dev``.

Testing your changes
--------------------

#. Run ``pycodestyle`` on ``sphinx_sitemap_dev``::

     pycodestyle sphinx_sitemap_dev


.. _third party extension: http://www.sphinx-doc.org/en/master/ext/thirdparty.html
