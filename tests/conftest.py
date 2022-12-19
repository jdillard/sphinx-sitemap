import pytest
from sphinx.testing.path import path

pytest_plugins = "sphinx.testing.fixtures"
# Exclude 'roots' dirs for pytest test collector
collect_ignore = ["roots"]


def pytest_configure(config):
    # before Sphinx 3.3.0, the `sphinx` marker is not registered by
    # the extension (but by Sphinx's internal pytest config)
    config.addinivalue_line("markers", "sphinx")


@pytest.fixture(scope="session")
def rootdir():
    return path(__file__).parent.abspath() / "roots"
