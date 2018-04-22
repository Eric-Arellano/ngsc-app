"""
Rename a file or folder for the specified targets.
"""
from googleapiclient import discovery

from backend.src.google_apis import drive_api

ResourceID = str


def file(file_id: ResourceID,
         new_name: str, *,
         drive_service: discovery.Resource = None) -> None:
    """
    Rename file.
    """
    _rename_resource(resource_id=file_id,
                     new_name=new_name,
                     drive_service=drive_service)


def folder(folder_id: ResourceID,
           new_name: str, *,
           drive_service: discovery.Resource = None) -> None:
    """
    Rename folder.
    """
    _rename_resource(resource_id=folder_id,
                     new_name=new_name,
                     drive_service=drive_service)


def _rename_resource(resource_id: ResourceID,
                     new_name: str, *,
                     drive_service: discovery.Resource = None) -> None:
    """
    Rename resource helper.
    """
    if drive_service is None:
        drive_service = drive_api.build_service()
    file_metadata = {
        'name': new_name,
    }
    drive_service \
        .files() \
        .update(fileId=resource_id, body=file_metadata) \
        .execute()
