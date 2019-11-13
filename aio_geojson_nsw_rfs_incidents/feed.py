"""NSW Rural Fire Service Incidents feed."""
import logging
from typing import Optional

from aio_geojson_client.feed import GeoJsonFeed
from aiohttp import ClientSession

from .consts import URL
from .feed_entry import NswRuralFireServiceIncidentsFeedEntry

_LOGGER = logging.getLogger(__name__)


class NswRuralFireServiceIncidentsFeed(GeoJsonFeed):
    """NSW Rural Fire Services Incidents feed."""

    def __init__(self,
                 websession: ClientSession,
                 home_coordinates,
                 filter_radius=None,
                 filter_categories=None):
        """Initialise this service."""
        super().__init__(websession,
                         home_coordinates,
                         URL,
                         filter_radius=filter_radius)
        self._filter_categories = filter_categories

    def __repr__(self):
        """Return string representation of this feed."""
        return '<{}(home={}, url={}, radius={}, categories={})>'.format(
            self.__class__.__name__, self._home_coordinates, self._url,
            self._filter_radius, self._filter_categories)

    def _new_entry(self, home_coordinates, feature, global_data):
        """Generate a new entry."""
        return NswRuralFireServiceIncidentsFeedEntry(home_coordinates, feature)

    def _filter_entries(self, entries):
        """Filter the provided entries."""
        filtered_entries = super()._filter_entries(entries)
        if self._filter_categories:
            filtered_entries = list(filter(lambda entry:
                                    entry.category in self._filter_categories,
                                    filtered_entries))
        return filtered_entries

    def _extract_last_timestamp(self, feed_entries):
        """Determine latest (newest) entry from the filtered feed."""
        if feed_entries:
            dates = sorted(filter(
                None, [entry.publication_date for entry in feed_entries]),
                reverse=True)
            return dates[0]
        return None

    def _extract_from_feed(self, feed) -> Optional:
        """Extract global metadata from feed."""
        return None
