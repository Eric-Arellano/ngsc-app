"""
Create an empty file or folder into the specified targets.
"""

from backend.src.google_apis.authentication import build_drive_service


# files created in Scripts/Drive playground
def file(file_name: str, parent_folder_id: str = '1QOsOQq3FMYfpXau6v3ubem5wrC97yWwo'):
    """
    Create an empty file.
    """
    # TODO: Change mime_type to allow multiple different mime types not just 'document'
    return _create_helper(name=file_name, mime_type='document', parent_folder_id=parent_folder_id)


# currently is Scripts/Drive playground
def folder(folder_name: str, parent_folder_id: str = '1QOsOQq3FMYfpXau6v3ubem5wrC97yWwo'):
    """
    Create an empty folder.
    """
    return _create_helper(name=folder_name, mime_type='folder', parent_folder_id=parent_folder_id)


def _create_helper(name: str, mime_type: str, parent_folder_id: str = '1QOsOQq3FMYfpXau6v3ubem5wrC97yWwo'):
    service = build_drive_service()
    file_metadata = {
        'name': name,
        'mimeType': f'application/vnd.google-apps.{mime_type}',
        'parents': [parent_folder_id]
    }
    new_folder = service.files().create(body=file_metadata,
                                        fields='id').execute()
    return 'Folder ID: %s' % new_folder.get('id')
