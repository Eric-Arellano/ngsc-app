from googleapiclient import discovery

from backend.src.google_apis import authentication


def build_service() -> discovery.Resource:
    """
    Instantiate Google Drive service with correct credentials and API keys.
    """
    return discovery.build('drive', 'v3', http=authentication.get_auth())
