"""
Remove a file or folder for the specified targets.
"""
from backend.src.google_apis import drive_api

ResourceID = str


def file(file_id: ResourceID) -> None:
    """
    Remove file.
    """
    _delete_resource(file_id)


def folder(folder_id: ResourceID) -> None:
    """
    Recursively remove entire folder.
    """
    _delete_resource(folder_id)


def _delete_resource(resource_id: ResourceID) -> None:
    """
    Helper for deleting files and folders
    """
    service = drive_api.build_service()
    service \
        .files() \
        .delete(fileId=resource_id) \
        .execute()
