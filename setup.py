from setuptools import setup
import os

long_description = open('README.rst' if os.path.exists('README.rst') else 'README.md').read()
exec(compile(
    open('sphinx_sitemap/version.py').read(), 'sphinx_sitemap/version.py', 'exec'))

setup(
    name='sphinx-sitemap',
    description='Sitemap generator for Sphinx',
    long_description=long_description,
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Topic :: Documentation',
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
      ],
    version=__version__,
    author='Jared Dillard',
    author_email='jared.dillard@gmail.com',
    install_requires=['six', 'sphinx >= 1.2'],
    url="https://github.com/jdillard/sphinx-sitemap",
    download_url="https://github.com/jdillard/sphinx-sitemap/archive/0.1.tar.gz",
    packages=['sphinx_sitemap'],
 )
