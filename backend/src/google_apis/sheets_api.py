"""
Utilities for interfacing with Google Sheet's API.
"""

from googleapiclient import discovery

from backend.src.google_apis import authentication


def build_service() -> discovery.Resource:
    """
    Instantiate Google Sheets service with correct credentials and API keys.
    """
    discovery_url = "https://sheets.googleapis.com/$discovery/rest?" "version=v4"
    return discovery.build(
        "sheets",
        "v4",
        http=authentication.get_auth(),
        discoveryServiceUrl=discovery_url,
    )
