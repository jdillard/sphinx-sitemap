# Contributing

Thank you for your interest in contributing to **sphinx-sitemap**!

## Process for contributing

You will need to set up a development environment to make and test your changes
before submitting them.

### Setting up a dev environment

You need to add **sphinx-sitemap** as a
[third party extension](http://www.sphinx-doc.org/en/master/ext/thirdparty.html).

1. If your project doesn't have an extensions directory, create `exts` and
   point **conf.py** to it:

   ```sys.path.append(os.path.abspath('../exts'))```

2. Copy `sphinx_sitemap` as a directory in your project's extensions
   directory, and rename it to `sphinx_sitemap_dev`.

3. Add `sphinx_sitemap_dev` to **extensions**, or change `sphinx_sitemap` to
   `sphinx_sitemap_dev` if you already have the extension installed via `pip`,
   in **conf.py**:

   ```extensions = ['sphinx_sitemap_dev']```

You can now make changes to `sphinx_sitemap_dev`.

### Testing your changes

1. Run `pep8` on `sphinx_sitemap_dev`:

   ```pep8 sphinx_sitemap_dev```