import pytest
from os import path

pytest_plugins = "sphinx.testing.fixtures"
# Exclude 'roots' dirs for pytest test collector
collect_ignore = ["roots"]


def pytest_configure(config):
    # before Sphinx 3.3.0, the `sphinx` marker is not registered by
    # the extension (but by Sphinx's internal pytest config)
    config.addinivalue_line("markers", "sphinx")


@pytest.fixture(scope="session")
def rootdir():
    current_script_path = path.abspath(__file__)
    parent_directory = path.abspath(path.dirname(current_script_path))
    return parent_directory / "roots"
