from typing import Callable, Dict, List

from googleapiclient import discovery, errors, http

from backend.src.google_apis import authentication

# --------------------------------------------------------------
# Data types
# --------------------------------------------------------------

ResourceID = str

BatchCallback = Callable[[str, Dict, errors.HttpError], None]


# --------------------------------------------------------------
# Core commands
# --------------------------------------------------------------


def build_service() -> discovery.Resource:
    """
    Instantiate Google Drive service with correct credentials and API keys.
    """
    return discovery.build("drive", "v3", http=authentication.get_auth())


def batch_command(
    *,
    callback: BatchCallback = None,
    requests: List[http.HttpRequest],
    drive_service: discovery.Resource = None,
) -> None:
    """
    Execute batch command.

    If you want the batch command to return a value, the callback must append
    its result to a list within the calling function's closure.
    """
    if drive_service is None:
        drive_service = build_service()

    batch = drive_service.new_batch_http_request(callback=callback)
    for request in requests:
        batch.add(request)
    batch.execute()
