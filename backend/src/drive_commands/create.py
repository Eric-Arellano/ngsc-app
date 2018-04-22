"""
Create an empty file or folder into the specified targets.
"""
from googleapiclient import discovery

from backend.src.data import mime_types
from backend.src.google_apis import drive_api

FileID = str


def gdoc(file_name: str, *,
         parent_folder_id: FileID,
         drive_service: discovery.Resource = None) -> FileID:
    """
    Create an empty Google Doc.
    """
    return _resource(name=file_name,
                     mime_type=mime_types.gdoc,
                     parent_folder_id=parent_folder_id,
                     drive_service=drive_service)


def gsheet(file_name: str, *,
           parent_folder_id: FileID,
           drive_service: discovery.Resource = None) -> FileID:
    """
    Create an empty Google Sheet.
    """
    return _resource(name=file_name,
                     mime_type=mime_types.gsheets,
                     parent_folder_id=parent_folder_id,
                     drive_service=drive_service)


def gslides(file_name: str, *,
            parent_folder_id: FileID,
            drive_service: discovery.Resource = None) -> FileID:
    """
    Create an empty Google Slides presentation.
    """
    return _resource(name=file_name,
                     mime_type=mime_types.gslides,
                     parent_folder_id=parent_folder_id,
                     drive_service=drive_service)


def gform(file_name: str, *,
          parent_folder_id: FileID,
          drive_service: discovery.Resource = None) -> FileID:
    """
    Create an empty Google Form.
    """
    return _resource(name=file_name,
                     mime_type=mime_types.gform,
                     parent_folder_id=parent_folder_id,
                     drive_service=drive_service)


def file(file_name: str, *,
         mime_type: str,
         parent_folder_id: FileID,
         drive_service: discovery.Resource = None) -> FileID:
    """
    Create an empty file.
    """
    return _resource(name=file_name,
                     mime_type=mime_type,
                     parent_folder_id=parent_folder_id,
                     drive_service=drive_service)


def folder(folder_name: str, *,
           parent_folder_id: FileID,
           drive_service: discovery.Resource = None) -> FileID:
    """
    Create an empty folder.
    """
    return _resource(name=folder_name,
                     mime_type=mime_types.folder,
                     parent_folder_id=parent_folder_id,
                     drive_service=drive_service)


def _resource(name: str, *,
              mime_type: str,
              parent_folder_id: FileID,
              drive_service: discovery.Resource = None) -> FileID:
    """
    Create Google Drive file with specific MIME type.
    """
    if drive_service is None:
        drive_service = drive_api.build_service()
    file_metadata = {
        'name': name,
        'mimeType': f'application/vnd.google-apps.{mime_type}',
        'parents': [parent_folder_id]
    }
    resource = drive_service \
        .files() \
        .create(body=file_metadata, fields='id') \
        .execute()
    return resource.get('id')
