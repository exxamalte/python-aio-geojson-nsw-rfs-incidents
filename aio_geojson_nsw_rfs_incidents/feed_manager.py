"""Feed Manager for NSW Rural Fire Service Incidents feed."""
from aio_geojson_client.feed_manager import FeedManagerBase
from aiohttp import ClientSession

from .feed import NswRuralFireServiceIncidentsFeed


class NswRuralFireServiceIncidentsFeedManager(FeedManagerBase):
    """Feed Manager for NSW Rural Fire Services Incidents feed."""

    def __init__(self,
                 websession: ClientSession,
                 generate_callback,
                 update_callback,
                 remove_callback,
                 coordinates,
                 filter_radius=None,
                 filter_categories=None):
        """Initialize the NSW Rural Fire Services Feed Manager."""
        feed = NswRuralFireServiceIncidentsFeed(
            websession,
            coordinates,
            filter_radius=filter_radius,
            filter_categories=filter_categories)
        super().__init__(feed,
                         generate_callback,
                         update_callback,
                         remove_callback)
