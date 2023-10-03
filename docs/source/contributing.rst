Contributing
============

You will need to set up a development environment to make and test your changes
before submitting them.

Local development
-----------------

#. Clone the `sphinx-sitemap repository`_.

#. Create and activate a virtual environment:

   .. code-block:: console

      python3 -m venv .venv
      source .venv/bin/activate

#. Install development dependencies:

   .. code-block:: console

      pip3 install -r dev-requirements.txt

#. Install pre-commit Git hook scripts:

   .. code-block:: console

      pre-commit install

Install a local copy of the extension
-------------------------------------

Add **sphinx-sitemap** as a `third party extension`_.

#. If your project doesn't have an extensions directory, create ``_exts`` and
   point **conf.py** to it:

   .. code-block:: python

      sys.path.append(os.path.abspath('../_exts'))

#. Copy ``sphinx_sitemap`` as a directory in your project's extensions
   directory, and rename it to ``sphinx_sitemap_dev``.

#. Add ``sphinx_sitemap_dev`` to :confval:`extensions`, or if already installed via ``pip``, change ``sphinx_sitemap`` to ``sphinx_sitemap_dev`` in **conf.py**:

   .. code-block:: python

      extensions = ['sphinx_sitemap_dev']

You can now make changes to ``sphinx_sitemap_dev``.

Testing changes
---------------

Run ``tox`` before committing changes.

Current contributors
--------------------

Thanks to all who have contributed!
The people that have improved the code:

.. contributors:: jdillard/sphinx-sitemap
   :avatars:
   :limit: 100
   :exclude: pre-commit-ci[bot]
   :order: ASC


.. _sphinx-sitemap repository: https://github.com/jdillard/sphinx-sitemap
.. _third party extension: http://www.sphinx-doc.org/en/master/ext/thirdparty.html
