"""Test for the NSW Rural Fire Service Incidents GeoJSON general setup."""
from aio_geojson_nsw_rfs_incidents import __version__


def test_version():
    """Test for version tag."""
    assert __version__ is not None
