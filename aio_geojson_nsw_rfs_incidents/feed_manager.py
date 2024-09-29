"""Feed Manager for NSW Rural Fire Service Incidents feed."""

from __future__ import annotations

from collections.abc import Awaitable, Callable

from aio_geojson_client.feed_manager import FeedManagerBase
from aio_geojson_client.status_update import StatusUpdate
from aiohttp import ClientSession

from .feed import NswRuralFireServiceIncidentsFeed


class NswRuralFireServiceIncidentsFeedManager(FeedManagerBase):
    """Feed Manager for NSW Rural Fire Services Incidents feed."""

    def __init__(
        self,
        websession: ClientSession,
        generate_callback: Callable[[str], Awaitable[None]],
        update_callback: Callable[[str], Awaitable[None]],
        remove_callback: Callable[[str], Awaitable[None]],
        coordinates: tuple[float, float],
        filter_radius: float | None = None,
        filter_categories: list[str] | None = None,
        status_callback: Callable[[StatusUpdate], Awaitable[None]] | None = None,
    ):
        """Initialize the NSW Rural Fire Services Feed Manager."""
        feed = NswRuralFireServiceIncidentsFeed(
            websession,
            coordinates,
            filter_radius=filter_radius,
            filter_categories=filter_categories,
        )
        super().__init__(
            feed,
            generate_callback,
            update_callback,
            remove_callback,
            status_async_callback=status_callback,
        )
