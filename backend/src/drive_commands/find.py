"""
Locate and return a file or folder ID for the specified targets.
"""
from typing import Optional

from backend.src.google_apis import drive_api

ResourceID = str


def file(file_name: str) -> Optional[ResourceID]:
    """
    Find file.
    """
    return _find_resource(file_name)


def folder(folder_name: str) -> Optional[ResourceID]:
    """
    Find folder.
    """
    return _find_resource(folder_name)


# TODO: Connect Mimetype, Parameterize query, Return error message if too many results.
def _find_resource(resource_name: str) -> Optional[ResourceID]:
    """
    Helper for finding files and folders
    """
    service = drive_api.build_service()
    results = service \
        .files() \
        .list(q="name='Leads Training' and '1F6LJ7Ws9S9YEzGvTZoRqIt23Tl60C6TI' in parents",
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
