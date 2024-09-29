"""NSW Rural Fire Service Incidents constants."""

ATTR_CATEGORY = "category"
ATTR_DESCRIPTION = "description"
ATTR_GUID = "guid"
ATTR_PUB_DATE = "pubDate"
ATTR_TITLE = "title"

ATTRIBUTION = "State of New South Wales (NSW Rural Fire Service)"

CUSTOM_ATTRIBUTE = "custom_attribute"

REGEXP_ATTR_COUNCIL_AREA = f"COUNCIL AREA: (?P<{CUSTOM_ATTRIBUTE}>[^<]+) <br"
REGEXP_ATTR_FIRE = f"FIRE: (?P<{CUSTOM_ATTRIBUTE}>[^<]+) <br"
REGEXP_ATTR_LOCATION = f"LOCATION: (?P<{CUSTOM_ATTRIBUTE}>[^<]+) <br"
REGEXP_ATTR_RESPONSIBLE_AGENCY = (
    f"RESPONSIBLE AGENCY: (?P<{CUSTOM_ATTRIBUTE}>[^<]+) <br"
)
REGEXP_ATTR_SIZE = f"SIZE: (?P<{CUSTOM_ATTRIBUTE}>[^<]+) <br"
REGEXP_ATTR_STATUS = f"STATUS: (?P<{CUSTOM_ATTRIBUTE}>[^<]+) <br"
REGEXP_ATTR_TYPE = f"TYPE: (?P<{CUSTOM_ATTRIBUTE}>[^<]+) <br"

URL = "https://www.rfs.nsw.gov.au/feeds/majorIncidents.json"

VALID_CATEGORIES = ["Emergency Warning", "Watch and Act", "Advice", "Not Applicable"]
