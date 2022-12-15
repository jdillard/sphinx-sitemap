# Maintaining PyPI Version

These are the steps, to be run by the maintainer, for making a new Python
package release.

1. Rev `__version__` in **sphinx_sitemap/\_\_init\_\_.py**.
2. Update **CHANGELOG.md**
3. Create a tag and push to GitHub:

       git tag -a vX.Y.Z -m "Release vX.Y.Z"
       git push --tags origin master

4. Build the latest distribution locally:

       python -m build

5. Upload to the test pypi.org repository:

       twine upload --repository-url https://test.pypi.org/legacy/ dist/*

6. Upload to the production pypi.org repository:

       twine upload dist/*
