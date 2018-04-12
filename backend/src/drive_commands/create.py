"""
Create an empty file or folder into the specified targets.
"""

from backend.src.google_apis.authentication import build_drive_service
from backend.src.data import folder_ids

FileID = str


def file(file_name: str,
         parent_folder_id: FileID = folder_ids.drive_playground) -> FileID:
    """
    Create an empty file.
    """
    # TODO: Change mime_type to allow multiple different mime types not just 'document'
    return _create_resource(name=file_name, mime_type='document', parent_folder_id=parent_folder_id)


def folder(folder_name: str,
           parent_folder_id: FileID = folder_ids.drive_playground) -> FileID:
    """
    Create an empty folder.
    """
    return _create_resource(name=folder_name, mime_type='folder', parent_folder_id=parent_folder_id)


def _create_resource(name: str,
                     mime_type: str,
                     parent_folder_id: FileID) -> FileID:
    """
    Create Google Drive file with specific MIME type.
    """
    service = build_drive_service()
    file_metadata = {
        'name': name,
        'mimeType': f'application/vnd.google-apps.{mime_type}',
        'parents': [parent_folder_id]
    }
    resource = service \
        .files() \
        .create(body=file_metadata, fields='id') \
        .execute()
    return resource.get('id')
