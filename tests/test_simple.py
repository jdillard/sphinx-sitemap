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
    """Tests basic HTML sitemap generation with all pages included."""
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
    """Tests sitemap generation with custom HTML file suffix (.htm)."""
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
    """Tests sitemap generation with DirectoryHTMLBuilder (clean URLs)."""
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
    """Tests exact string matching for sitemap exclusions (backward compatibility)."""
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


@pytest.mark.sphinx(
    "html",
    freshenv=True,
    confoverrides={
        "html_baseurl": "https://example.org/docs/",
        "language": "en",
        "sitemap_excludes": ["*index*.html", "search.html"],
    },
)
def test_wildcard_excludes(app, status, warning):
    """Tests that *index*.html wildcard pattern excludes both "index.html" and "genindex.html"."""
    app.warningiserror = True
    app.build()
    assert "sitemap.xml" in os.listdir(app.outdir)
    doc = etree.parse(app.outdir / "sitemap.xml")
    urls = {
        e.text
        for e in doc.findall(".//{http://www.sitemaps.org/schemas/sitemap/0.9}loc")
    }

    # *index*.html should exclude both "genindex.html" and "index.html"
    assert urls == {
        f"https://example.org/docs/en/{d}.html"
        for d in [
            "foo",
            "bar",
            "lorem",
            "ipsum",
            "dolor",
            "elitr",
        ]
    }


@pytest.mark.sphinx(
    "html",
    freshenv=True,
    confoverrides={
        "html_baseurl": "https://example.org/docs/",
        "language": "en",
        "sitemap_excludes": ["l*.html"],  # Excludes lorem.html but not other files
    },
)
def test_pattern_excludes(app, status, warning):
    """Tests that l*.html wildcard pattern excludes only "lorem.html"."""
    app.warningiserror = True
    app.build()
    assert "sitemap.xml" in os.listdir(app.outdir)
    doc = etree.parse(app.outdir / "sitemap.xml")
    urls = {
        e.text
        for e in doc.findall(".//{http://www.sitemaps.org/schemas/sitemap/0.9}loc")
    }

    # l*.html should exclude "lorem.html"
    assert urls == {
        f"https://example.org/docs/en/{d}.html"
        for d in [
            "index",
            "foo",
            "bar",
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
        "sitemap_prettify": True,
    },
)
def test_prettify(app, status, warning):
    """Tests that xml output is indented"""
    app.warningiserror = True
    app.build()
    assert "sitemap.xml" in os.listdir(app.outdir)
    with open(app.outdir / "sitemap.xml", "r") as fd:
        lines = fd.readlines()

    assert lines[0][0] == "<"
    assert lines[1][0] == "<"
    assert lines[2][0:3] == "  <"
