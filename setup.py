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
        'Topic :: Documentation :: Sphinx',
        'Programming Language :: Python :: 3',
        'Framework :: Sphinx :: Extension',
      ],
    version=__version__,
    author='Jared Dillard',
    author_email='jared.dillard@gmail.com',
    install_requires=['six', 'sphinx >= 1.2'],
    url="https://github.com/jdillard/sphinx-sitemap",
    license='MIT',
    download_url="https://github.com/jdillard/sphinx-sitemap/archive/v2.2.1.tar.gz",
    packages=['sphinx_sitemap'],
 )
