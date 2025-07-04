import os
from xml.etree import ElementTree as etree

import pytest
from git import Repo


@pytest.fixture(autouse=True, scope="function")
def git_setup(app):
    repo = Repo.init(app.srcdir)
    repo.index.add(os.listdir(app.srcdir))
    repo.index.commit("test: creating git record for files")
    yield


@pytest.mark.sphinx(
    "html",
    freshenv=True,
    confoverrides={"html_baseurl": "https://example.org/docs/", "language": "en"},
)
def test_simple_html(app, status, warning):
    app.warningiserror = True
    app.build()
    assert "sitemap.xml" in os.listdir(app.outdir)
    doc = etree.parse(app.outdir / "sitemap.xml")
    urls = {
        e.text
        for e in doc.findall(".//{http://www.sitemaps.org/schemas/sitemap/0.9}loc")
    }

    assert urls == {
        f"https://example.org/docs/en/{d}.html"
        for d in [
            "index",
            "foo",
            "bar",
            "lorem",
            "ipsum",
            "dolor",
            "elitr",
            "genindex",
            "search",
        ]
    }


@pytest.mark.sphinx(
    "html",
    freshenv=True,
    confoverrides={
        "html_baseurl": "https://example.org/docs/",
        "language": "en",
        "html_file_suffix": ".htm",
    },
)
def test_html_file_suffix(app, status, warning):
    app.warningiserror = True
    app.build()
    assert "sitemap.xml" in os.listdir(app.outdir)
    doc = etree.parse(app.outdir / "sitemap.xml")
    urls = {
        e.text
        for e in doc.findall(".//{http://www.sitemaps.org/schemas/sitemap/0.9}loc")
    }

    assert urls == {
        f"https://example.org/docs/en/{d}.htm"
        for d in [
            "index",
            "foo",
            "bar",
            "lorem",
            "ipsum",
            "dolor",
            "elitr",
            "genindex",
            "search",
        ]
    }


@pytest.mark.sphinx(
    "dirhtml",
    freshenv=True,
    confoverrides={"html_baseurl": "https://example.org/docs/", "language": "en"},
)
def test_simple_dirhtml(app, status, warning):
    app.warningiserror = True
    app.build()
    assert "sitemap.xml" in os.listdir(app.outdir)
    doc = etree.parse(app.outdir / "sitemap.xml")
    urls = {
        e.text
        for e in doc.findall(".//{http://www.sitemaps.org/schemas/sitemap/0.9}loc")
    }

    assert urls == {
        f"https://example.org/docs/en/{d}"
        for d in [
            "",
            "foo/",
            "bar/",
            "lorem/",
            "ipsum/",
            "dolor/",
            "elitr/",
            "genindex/",
            "search/",
        ]
    }


@pytest.mark.sphinx(
    "html",
    freshenv=True,
    confoverrides={
        "html_baseurl": "https://example.org/docs/",
        "language": "en",
        "sitemap_excludes": ["search.html", "genindex.html"],
    },
)
def test_simple_excludes(app, status, warning):
    app.warningiserror = True
    app.build()
    assert "sitemap.xml" in os.listdir(app.outdir)
    doc = etree.parse(app.outdir / "sitemap.xml")
    urls = {
        e.text
        for e in doc.findall(".//{http://www.sitemaps.org/schemas/sitemap/0.9}loc")
    }

    assert urls == {
        f"https://example.org/docs/en/{d}.html"
        for d in [
            "index",
            "foo",
            "bar",
            "lorem",
            "ipsum",
            "dolor",
            "elitr",
        ]
    }
