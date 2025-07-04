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
def test_parallel(app, status, warning):
    app.parallel = 2
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
    assert not warning.getvalue()
