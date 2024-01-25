"""NSW Rural Fire Service Incidents feed entry."""
from __future__ import annotations

import calendar
import logging
import re
from datetime import datetime
from time import strptime

import pytz
from aio_geojson_client.feed_entry import FeedEntry
from geojson import Feature

from .consts import (
    ATTR_CATEGORY,
    ATTR_DESCRIPTION,
    ATTR_GUID,
    ATTR_PUB_DATE,
    ATTR_TITLE,
    ATTRIBUTION,
    CUSTOM_ATTRIBUTE,
    REGEXP_ATTR_COUNCIL_AREA,
    REGEXP_ATTR_FIRE,
    REGEXP_ATTR_LOCATION,
    REGEXP_ATTR_RESPONSIBLE_AGENCY,
    REGEXP_ATTR_SIZE,
    REGEXP_ATTR_STATUS,
    REGEXP_ATTR_TYPE,
)

_LOGGER = logging.getLogger(__name__)


class NswRuralFireServiceIncidentsFeedEntry(FeedEntry):
    """NSW Rural Fire Service Incidents feed entry."""

    def __init__(self, home_coordinates: tuple[float, float], feature: Feature):
        """Initialise this service."""
        super().__init__(home_coordinates, feature)

    @property
    def attribution(self) -> str | None:
        """Return the attribution of this entry."""
        return ATTRIBUTION

    @property
    def title(self) -> str:
        """Return the title of this entry."""
        return self._search_in_properties(ATTR_TITLE)

    @property
    def category(self) -> str:
        """Return the category of this entry."""
        return self._search_in_properties(ATTR_CATEGORY)

    @property
    def external_id(self) -> str:
        """Return the external id of this entry."""
        return self._search_in_properties(ATTR_GUID)

    @property
    def publication_date(self) -> datetime:
        """Return the publication date of this entry."""
        publication_date = self._search_in_properties(ATTR_PUB_DATE)
        if publication_date:
            # Parse the date. Example: 15/09/2018 9:31:00 AM
            date_struct = strptime(publication_date, "%d/%m/%Y %I:%M:%S %p")
            publication_date = datetime.fromtimestamp(
                calendar.timegm(date_struct), tz=pytz.utc
            )
        return publication_date

    @property
    def description(self) -> str:
        """Return the description of this entry."""
        return self._search_in_properties(ATTR_DESCRIPTION)

    def _search_in_description(self, regexp):
        """Find a sub-string in the entry's description."""
        if self.description:
            match = re.search(regexp, self.description)
            if match:
                return match.group(CUSTOM_ATTRIBUTE)
        return None

    @property
    def location(self) -> str:
        """Return the location of this entry."""
        return self._search_in_description(REGEXP_ATTR_LOCATION)

    @property
    def council_area(self) -> str:
        """Return the council area of this entry."""
        return self._search_in_description(REGEXP_ATTR_COUNCIL_AREA)

    @property
    def status(self) -> str:
        """Return the status of this entry."""
        return self._search_in_description(REGEXP_ATTR_STATUS)

    @property
    def type(self) -> str:
        """Return the type of this entry."""
        return self._search_in_description(REGEXP_ATTR_TYPE)

    @property
    def fire(self) -> bool:
        """Return if this entry represents a fire or not."""
        return self._search_in_description(REGEXP_ATTR_FIRE) == "Yes"

    @property
    def size(self) -> str:
        """Return the size of this entry."""
        return self._search_in_description(REGEXP_ATTR_SIZE)

    @property
    def responsible_agency(self) -> str:
        """Return the responsible agency of this entry."""
        return self._search_in_description(REGEXP_ATTR_RESPONSIBLE_AGENCY)
