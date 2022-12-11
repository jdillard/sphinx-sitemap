import os

from setuptools import setup

import sphinx_sitemap

long_description = open(
    "README.rst" if os.path.exists("README.rst") else "README.md"
).read()

setup(
    name="sphinx-sitemap",
    description="Sitemap generator for Sphinx",
    long_description=long_description,
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Topic :: Documentation :: Sphinx",
        "Programming Language :: Python :: 3",
        "Framework :: Sphinx :: Extension",
    ],
    version=sphinx_sitemap.__version__,
    author="Jared Dillard",
    author_email="jared.dillard@gmail.com",
    install_requires=["six", "sphinx >= 1.2"],
    url="https://github.com/jdillard/sphinx-sitemap",
    license="MIT",
    packages=["sphinx_sitemap"],
)
