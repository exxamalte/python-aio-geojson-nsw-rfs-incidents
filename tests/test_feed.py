"""Test for the NSW Rural Fire Service Incidents GeoJSON feed."""
import datetime

import aiohttp
import pytest
from aio_geojson_client.consts import UPDATE_OK

from aio_geojson_nsw_rfs_incidents.consts import ATTRIBUTION
from aio_geojson_nsw_rfs_incidents.feed import NswRuralFireServiceIncidentsFeed
from tests.utils import load_fixture


@pytest.mark.asyncio
async def test_update_ok(aresponses, event_loop):
    """Test updating feed is ok."""
    home_coordinates = (-31.0, 151.0)
    aresponses.add(
        "www.rfs.nsw.gov.au",
        "/feeds/majorIncidents.json",
        "get",
        aresponses.Response(text=load_fixture("incidents-1.json"), status=200),
        match_querystring=True,
    )

    async with aiohttp.ClientSession(loop=event_loop) as websession:

        feed = NswRuralFireServiceIncidentsFeed(websession, home_coordinates)
        assert (
            repr(feed) == "<NswRuralFireServiceIncidentsFeed("
            "home=(-31.0, 151.0), "
            "url=https://www.rfs.nsw.gov.au"
            "/feeds/majorIncidents.json, "
            "radius=None, categories=None)>"
        )
        status, entries = await feed.update()
        assert status == UPDATE_OK
        assert entries is not None
        assert len(entries) == 4

        feed_entry = entries[0]
        assert feed_entry.title == "Title 1"
        assert feed_entry.category == "Category 1"
        assert feed_entry.external_id == "1234"
        assert feed_entry.coordinates == (-37.2345, 149.1234)
        assert round(abs(feed_entry.distance_to_home - 714.4), 1) == 0
        assert repr(feed_entry) == "<NswRuralFireServiceIncidents" "FeedEntry(id=1234)>"
        assert feed_entry.publication_date == datetime.datetime(
            2018, 9, 21, 6, 30, tzinfo=datetime.timezone.utc
        )
        assert feed_entry.location == "Location 1"
        assert feed_entry.council_area == "Council 1"
        assert feed_entry.status == "Status 1"
        assert feed_entry.type == "Type 1"
        assert feed_entry.fire
        assert feed_entry.size == "10 ha"
        assert feed_entry.responsible_agency == "Agency 1"
        assert feed_entry.attribution == ATTRIBUTION

        feed_entry = entries[1]
        assert feed_entry is not None
        assert feed_entry.title == "Title 2"
        assert feed_entry.category == "Category 2"
        assert not feed_entry.fire

        feed_entry = entries[2]
        assert feed_entry.title == "Title 3"
        assert feed_entry.category is None

        feed_entry = entries[3]
        assert feed_entry.title == "Badja Forest Rd, Countegany"
        assert feed_entry.geometries is not None
        assert len(feed_entry.geometries) == 4
        assert round(abs(feed_entry.distance_to_home - 578.5), 1) == 0


@pytest.mark.asyncio
async def test_update_ok_with_categories(aresponses, event_loop):
    """Test updating feed is ok, filtered by category."""
    home_coordinates = (-31.0, 151.0)
    aresponses.add(
        "www.rfs.nsw.gov.au",
        "/feeds/majorIncidents.json",
        "get",
        aresponses.Response(text=load_fixture("incidents-1.json"), status=200),
        match_querystring=True,
    )

    async with aiohttp.ClientSession(loop=event_loop) as websession:

        feed = NswRuralFireServiceIncidentsFeed(
            websession, home_coordinates, filter_categories=["Category 1"]
        )
        assert (
            repr(feed) == "<NswRuralFireServiceIncidentsFeed("
            "home=(-31.0, 151.0), "
            "url=https://www.rfs.nsw.gov.au"
            "/feeds/majorIncidents.json, "
            "radius=None, categories=['Category 1'])>"
        )
        status, entries = await feed.update()
        assert status == UPDATE_OK
        assert entries is not None
        assert len(entries) == 1

        feed_entry = entries[0]
        assert feed_entry is not None
        assert feed_entry.title == "Title 1"
        assert feed_entry.category == "Category 1"
        assert repr(feed_entry) == "<NswRuralFireServiceIncidents" "FeedEntry(id=1234)>"


@pytest.mark.asyncio
async def test_empty_feed(aresponses, event_loop):
    """Test updating feed is ok when feed does not contain any entries."""
    home_coordinates = (-41.2, 174.7)
    aresponses.add(
        "www.rfs.nsw.gov.au",
        "/feeds/majorIncidents.json",
        "get",
        aresponses.Response(text=load_fixture("incidents-2.json"), status=200),
        match_querystring=True,
    )

    async with aiohttp.ClientSession(loop=event_loop) as websession:

        feed = NswRuralFireServiceIncidentsFeed(websession, home_coordinates)
        assert (
            repr(feed) == "<NswRuralFireServiceIncidentsFeed("
            "home=(-41.2, 174.7), "
            "url=https://www.rfs.nsw.gov.au"
            "/feeds/majorIncidents.json, "
            "radius=None, categories=None)>"
        )
        status, entries = await feed.update()
        assert status == UPDATE_OK
        assert entries is not None
        assert len(entries) == 0
        assert feed.last_timestamp is None
