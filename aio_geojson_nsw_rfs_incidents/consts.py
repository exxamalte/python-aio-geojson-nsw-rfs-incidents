"""NSW Rural Fire Service Incidents constants."""

ATTR_CATEGORY = "category"
ATTR_DESCRIPTION = "description"
ATTR_GUID = "guid"
ATTR_PUB_DATE = "pubDate"
ATTR_TITLE = "title"

ATTRIBUTION = "State of New South Wales (NSW Rural Fire Service)"

CUSTOM_ATTRIBUTE = "custom_attribute"

REGEXP_ATTR_COUNCIL_AREA = "COUNCIL AREA: (?P<{}>[^<]+) <br".format(CUSTOM_ATTRIBUTE)
REGEXP_ATTR_FIRE = "FIRE: (?P<{}>[^<]+) <br".format(CUSTOM_ATTRIBUTE)
REGEXP_ATTR_LOCATION = "LOCATION: (?P<{}>[^<]+) <br".format(CUSTOM_ATTRIBUTE)
REGEXP_ATTR_RESPONSIBLE_AGENCY = "RESPONSIBLE AGENCY: (?P<{}>[^<]+) <br".format(
    CUSTOM_ATTRIBUTE
)
REGEXP_ATTR_SIZE = "SIZE: (?P<{}>[^<]+) <br".format(CUSTOM_ATTRIBUTE)
REGEXP_ATTR_STATUS = "STATUS: (?P<{}>[^<]+) <br".format(CUSTOM_ATTRIBUTE)
REGEXP_ATTR_TYPE = "TYPE: (?P<{}>[^<]+) <br".format(CUSTOM_ATTRIBUTE)

URL = "https://www.rfs.nsw.gov.au/feeds/majorIncidents.json"

VALID_CATEGORIES = ["Emergency Warning", "Watch and Act", "Advice", "Not Applicable"]
