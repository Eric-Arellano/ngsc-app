"""
Locate and return a file or folder ID for the specified targets.
"""
from typing import Optional

from backend.src.google_apis import drive_api

ResourceID = str


def file(file_name: str, *, parent_folder_id: ResourceID, mime_type: str = None) -> Optional[ResourceID]:
    """
    Find file.
    """
    return _find_resource(file_name, parent_folder_id=parent_folder_id, mime_type=mime_type)


def folder(folder_name: str, *, parent_folder_id: ResourceID, mime_type: str = None) -> Optional[ResourceID]:
    """
    Find folder.
    """
    return _find_resource(folder_name, parent_folder_id=parent_folder_id, mime_type=mime_type)


# TODO: Return error message if too many results.
def _find_resource(resource_name: str, *, parent_folder_id: ResourceID, mime_type: str = None) -> Optional[ResourceID]:
    """
    Helper for finding files and folders
    """
    query = f"name='{resource_name}' and '{parent_folder_id}' in parents"
    if mime_type:
        query += f" and mimeType='application/vnd.google-apps.{mime_type}'"
    service = drive_api.build_service()
    results = service \
        .files() \
        .list(q=query,
              pageSize=10,
              fields="nextPageToken, files(id, name)") \
        .execute()
    items = results.get('files', [])
    if not items:
        return None
    output = ''
    for item in items:
        output += f"{item['name']} {item['id']}"
    return output
