"""
Rename a file or folder for the specified targets.
"""
from backend.src.google_apis import drive_api

ResourceID = str


def file(file_id: ResourceID, new_name: str) -> None:
    """
    Rename file.
    """
    _rename_resource(resource_id=file_id, new_name=new_name)


def folder(folder_id: ResourceID, new_name: str) -> None:
    """
    Rename folder.
    """
    _rename_resource(resource_id=folder_id, new_name=new_name)


def _rename_resource(resource_id: ResourceID, new_name: str) -> None:
    """
    Rename resource helper.
    """
    service = drive_api.build_service()
    file_metadata = {
        'name': new_name,
    }
    service \
        .files() \
        .update(fileId=resource_id, body=file_metadata) \
        .execute()
