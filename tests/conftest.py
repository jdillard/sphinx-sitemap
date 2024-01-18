from pathlib import Path

import pytest
import sphinx

pytest_plugins = "sphinx.testing.fixtures"
# Exclude 'roots' dirs for pytest test collector
collect_ignore = ["roots"]


def pytest_configure(config):
    # before Sphinx 3.3.0, the `sphinx` marker is not registered by
    # the extension (but by Sphinx's internal pytest config)
    config.addinivalue_line("markers", "sphinx")


@pytest.fixture(scope="session")
def rootdir():
    if sphinx.version_info[:2] < (7, 2):
        from sphinx.testing.path import path

        return path(__file__).parent.abspath() / "roots"

    return Path(__file__).resolve().parent / "roots"
