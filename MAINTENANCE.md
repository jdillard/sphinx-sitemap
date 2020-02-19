# Maintaining PyPI Version

These are the steps, to be run by the maintainer, for making a new Python
package release.

1. Rev versions in **sphinx_sitemap/version.py** and **setup.py**.
2. Update **CHANGELOG.md**
3. Create a tag and push to GitHub:

       git tag -a vX.Y.Z -m "Release vX.Y.Z"
       git push --tags origin master

4. Create latest distribution locally:

       python setup.py sdist

5. Upload to the test pypi.org repository:

       twine upload --repository-url https://test.pypi.org/legacy/ dist/*

6. Upload to the production pypi.org repository:

       twine upload dist/*