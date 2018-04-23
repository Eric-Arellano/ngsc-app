"""
Move a file or folder from source into the specified targets.
"""
from typing import List, NamedTuple

from googleapiclient import discovery, http

from backend.src.drive_commands import find
from backend.src.google_apis import drive_api


# ---------------------------------------------------------------------
# Single resource (immediate execution)
# ---------------------------------------------------------------------

def resource(*,
             origin_resource_id: drive_api.ResourceID,
             target_folder_id: drive_api.ResourceID,
             drive_service: discovery.Resource = None) -> None:
    """
    Move specific resource to new parent.
    """
    command = request(origin_resource_id=origin_resource_id,
                      target_folder_id=target_folder_id,
                      drive_service=drive_service)
    command.execute()


# ---------------------------------------------------------------------
# Batch (immediate execution)
# ---------------------------------------------------------------------

class BatchArgument(NamedTuple):
    origin_resource_id: drive_api.ResourceID
    target_folder_id: drive_api.ResourceID


def batch(arguments: List[BatchArgument], *,
          drive_service: discovery.Resource = None) -> None:
    """
    Batch move multiple resources.
    """
    requests = [request(origin_resource_id=argument.origin_resource_id,
                        target_folder_id=argument.target_folder_id,
                        drive_service=drive_service)
                for argument in arguments]
    drive_api.batch_command(requests=requests,
                            drive_service=drive_service)


# ---------------------------------------------------------------------
# Generate request (delayed execution)
# ---------------------------------------------------------------------

def request(*,
            origin_resource_id: drive_api.ResourceID,
            target_folder_id: drive_api.ResourceID,
            drive_service: discovery.Resource = None) -> http.HttpRequest:
    """
    Generate request to move specific resource.
    """
    if drive_service is None:
        drive_service = drive_api.build_service()
    previous_parents = find.parent_folder_list(resource_id=origin_resource_id)
    previous_parents_formatted = ', '.join(previous_parents)
    return drive_service \
        .files() \
        .update(fileId=origin_resource_id,
                addParents=target_folder_id,
                removeParents=previous_parents_formatted,
                fields='id, parents')
