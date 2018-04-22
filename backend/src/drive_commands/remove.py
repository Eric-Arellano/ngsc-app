"""
Remove a file or folder for the specified targets.
"""
from googleapiclient import discovery

from backend.src.google_apis import drive_api

ResourceID = str


def file(file_id: ResourceID, *,
         drive_service: discovery.Resource = None) -> None:
    """
    Remove file.
    """
    _delete_resource(file_id, drive_service=drive_service)


def folder(folder_id: ResourceID, *,
           drive_service: discovery.Resource = None) -> None:
    """
    Recursively remove entire folder.
    """
    _delete_resource(folder_id, drive_service=drive_service)


def _delete_resource(resource_id: ResourceID, *,
                     drive_service: discovery.Resource = None) -> None:
    """
    Helper for deleting files and folders
    """
    if drive_service is not None:
        drive_service = drive_api.build_service()
    drive_service \
        .files() \
        .delete(fileId=resource_id) \
        .execute()
