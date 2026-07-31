"""Tests for the copier_python_template package."""

from copier_python_template import __version__


def test_version() -> None:
    """The package version should match the expected release."""
    assert __version__ == "0.1.0"
