from xml.etree import ElementTree as etree

import pytest

@pytest.mark.sphinx('html', freshenv=True)
def test_config_error(app, status, warning):
    app.build()
    assert 'sitemap.xml' not in app.outdir.listdir()
    # not `endswith` because of ANSI coloration
    assert 'Sitemap not built.' in warning.getvalue()

@pytest.mark.xfail(reason="need to setup a document-less project (is that even possible?)")
@pytest.mark.sphinx(
    'html', testoot="nodocs", freshenv=True,
    confoverrides={'html_baseurl': 'https://example.org/docs/'}
)
def test_no_documents(app, status, warning):
    app.build()
    assert 'sitemap.xml' not in app.outdir.listdir()
    assert warning.getvalue() == 'No pages generated for sitemap.xml'

@pytest.mark.sphinx(
    'html', freshenv=True,
    confoverrides={'html_baseurl': 'https://example.org/docs/'}
)
def test_simple(app, status, warning):
    app.build()
    assert 'sitemap.xml' in app.outdir.listdir()
    doc = etree.parse(app.outdir / 'sitemap.xml')
    urls = {e.text for e in doc.findall('.//{http://www.sitemaps.org/schemas/sitemap/0.9}loc')}

    assert urls == {
        f'https://example.org/docs/{d}.html'
        for d in ['index', 'foo', 'bar', 'corge', 'grault', 'quux',
                  'qux', 'genindex', 'search']
    }
    assert not warning.getvalue()

@pytest.mark.sphinx(
    'html', freshenv=True,
    confoverrides={'html_baseurl': 'https://example.org/docs/'}
)
def test_parallel(app, status, warning):
    app.parallel = 2
    app.build()
    assert 'sitemap.xml' in app.outdir.listdir()
    doc = etree.parse(app.outdir / 'sitemap.xml')
    urls = {e.text for e in doc.findall('.//{http://www.sitemaps.org/schemas/sitemap/0.9}loc')}

    assert urls == {
        f'https://example.org/docs/{d}.html'
        for d in ['index', 'foo', 'bar', 'corge', 'grault', 'quux',
                  'qux', 'genindex', 'search']
    }
    assert not warning.getvalue()
