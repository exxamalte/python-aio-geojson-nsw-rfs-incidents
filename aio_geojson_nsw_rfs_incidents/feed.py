"""NSW Rural Fire Service Incidents feed."""

from __future__ import annotations

from datetime import datetime
import logging

from aio_geojson_client.feed import GeoJsonFeed
from aiohttp import ClientSession
from geojson import FeatureCollection

from .consts import URL
from .feed_entry import NswRuralFireServiceIncidentsFeedEntry

_LOGGER = logging.getLogger(__name__)


class NswRuralFireServiceIncidentsFeed(
    GeoJsonFeed[NswRuralFireServiceIncidentsFeedEntry]
):
    """NSW Rural Fire Services Incidents feed."""

    def __init__(
        self,
        websession: ClientSession,
        home_coordinates: tuple[float, float],
        filter_radius: float | None = None,
        filter_categories: list[str] | None = None,
    ):
        """Initialise this service."""
        super().__init__(websession, home_coordinates, URL, filter_radius=filter_radius)
        self._filter_categories = filter_categories

    def __repr__(self):
        """Return string representation of this feed."""
        return f"<{self.__class__.__name__}(home={self._home_coordinates}, url={self._url}, radius={self._filter_radius}, categories={self._filter_categories})>"

    def _new_entry(
        self, home_coordinates: tuple[float, float], feature, global_data: dict
    ) -> NswRuralFireServiceIncidentsFeedEntry:
        """Generate a new entry."""
        return NswRuralFireServiceIncidentsFeedEntry(home_coordinates, feature)

    def _filter_entries(
        self, entries: list[NswRuralFireServiceIncidentsFeedEntry]
    ) -> list[NswRuralFireServiceIncidentsFeedEntry]:
        """Filter the provided entries."""
        filtered_entries = super()._filter_entries(entries)
        if self._filter_categories:
            filtered_entries = list(
                filter(
                    lambda entry: entry.category in self._filter_categories,
                    filtered_entries,
                )
            )
        return filtered_entries

    def _extract_last_timestamp(
        self, feed_entries: list[NswRuralFireServiceIncidentsFeedEntry]
    ) -> datetime | None:
        """Determine latest (newest) entry from the filtered feed."""
        if feed_entries:
            dates = sorted(
                filter(None, [entry.publication_date for entry in feed_entries]),
                reverse=True,
            )
            return dates[0]
        return None

    def _extract_from_feed(self, feed: FeatureCollection) -> dict | None:
        """Extract global metadata from feed."""
        return None
