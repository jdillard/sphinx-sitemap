from xml.etree import ElementTree as etree

import pytest


@pytest.mark.sphinx(
    "html",
    freshenv=True,
    confoverrides={"html_baseurl": "https://example.org/docs/", "language": "en"},
)
def test_simple_html(app, status, warning):
    app.warningiserror = True
    app.build()
    assert "sitemap.xml" in app.outdir.listdir()
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
    assert "sitemap.xml" in app.outdir.listdir()
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
    assert "sitemap.xml" in app.outdir.listdir()
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
