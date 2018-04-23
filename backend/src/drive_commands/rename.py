"""
Rename a resource within Google Drive.
"""
from typing import List, NamedTuple

from googleapiclient import discovery, http

from backend.src.google_apis import drive_api


# ---------------------------------------------------------------------
# Single resource (immediate execution)
# ---------------------------------------------------------------------

def resource(resource_id: drive_api.ResourceID,
             new_name: str, *,
             drive_service: discovery.Resource = None) -> None:
    """
    Rename specific resource.
    """
    command = request(resource_id=resource_id,
                      new_name=new_name,
                      drive_service=drive_service)
    command.execute()


# ---------------------------------------------------------------------
# Batch (immediate execution)
# ---------------------------------------------------------------------

class BatchArgument(NamedTuple):
    resource_id: drive_api.ResourceID
    new_name: drive_api.ResourceID


def batch(arguments: List[BatchArgument], *,
          drive_service: discovery.Resource = None) -> None:
    """
    Batch rename multiple resources.
    """
    requests = [request(resource_id=argument.resource_id,
                        new_name=argument.new_name,
                        drive_service=drive_service)
                for argument in arguments]
    drive_api.batch_command(requests=requests,
                            drive_service=drive_service)


# ---------------------------------------------------------------------
# Generate request (delayed execution)
# ---------------------------------------------------------------------

def request(resource_id: drive_api.ResourceID,
            new_name: str, *,
            drive_service: discovery.Resource = None) -> http.HttpRequest:
    """
    Generate request to rename specific resource.
    """
    if drive_service is None:
        drive_service = drive_api.build_service()
    file_metadata = {
        'name': new_name,
    }
    return drive_service \
        .files() \
        .update(fileId=resource_id, body=file_metadata)
