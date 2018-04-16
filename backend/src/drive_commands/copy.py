"""
Copy a file or folder from source into the specified targets.
"""
from backend.src.google_apis import drive_api

ResourceID = str


def file(origin_file_id: ResourceID,
         copy_name: str,
         parent_folder_id: ResourceID) -> ResourceID:
    """
    Copy the file into targets.

    Should maintain permissions and file metadata.
    """
    service = drive_api.build_service()
    file_metadata = {
        'name': copy_name,
        'parents': [parent_folder_id]
    }
    resource = service \
        .files() \
        .copy(fileId=origin_file_id, body=file_metadata, fields='id') \
        .execute()
    return resource.get('id')
