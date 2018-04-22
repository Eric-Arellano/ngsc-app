"""
Create an empty file or folder into the specified targets.
"""
from typing import List

from googleapiclient import discovery, http

from backend.src.data import mime_types
from backend.src.google_apis import drive_api


# ---------------------------------------------------------------------
# Single resource
# ---------------------------------------------------------------------

def gdoc(file_name: str, *,
         parent_folder_id: drive_api.ResourceID,
         drive_service: discovery.Resource = None) -> drive_api.ResourceID:
    """
    Create an empty Google Doc.
    """
    return _resource(name=file_name,
                     mime_type=mime_types.gdoc,
                     parent_folder_id=parent_folder_id,
                     drive_service=drive_service)


def gsheet(file_name: str, *,
           parent_folder_id: drive_api.ResourceID,
           drive_service: discovery.Resource = None) -> drive_api.ResourceID:
    """
    Create an empty Google Sheet.
    """
    return _resource(name=file_name,
                     mime_type=mime_types.gsheets,
                     parent_folder_id=parent_folder_id,
                     drive_service=drive_service)


def gslides(file_name: str, *,
            parent_folder_id: drive_api.ResourceID,
            drive_service: discovery.Resource = None) -> drive_api.ResourceID:
    """
    Create an empty Google Slides presentation.
    """
    return _resource(name=file_name,
                     mime_type=mime_types.gslides,
                     parent_folder_id=parent_folder_id,
                     drive_service=drive_service)


def gform(file_name: str, *,
          parent_folder_id: drive_api.ResourceID,
          drive_service: discovery.Resource = None) -> drive_api.ResourceID:
    """
    Create an empty Google Form.
    """
    return _resource(name=file_name,
                     mime_type=mime_types.gform,
                     parent_folder_id=parent_folder_id,
                     drive_service=drive_service)


def file(file_name: str, *,
         mime_type: str,
         parent_folder_id: drive_api.ResourceID,
         drive_service: discovery.Resource = None) -> drive_api.ResourceID:
    """
    Create an empty file.
    """
    return _resource(name=file_name,
                     mime_type=mime_type,
                     parent_folder_id=parent_folder_id,
                     drive_service=drive_service)


def folder(folder_name: str, *,
           parent_folder_id: drive_api.ResourceID,
           drive_service: discovery.Resource = None) -> drive_api.ResourceID:
    """
    Create an empty folder.
    """
    return _resource(name=folder_name,
                     mime_type=mime_types.folder,
                     parent_folder_id=parent_folder_id,
                     drive_service=drive_service)


def _resource(name: str, *,
              mime_type: str,
              parent_folder_id: drive_api.ResourceID,
              drive_service: discovery.Resource = None) -> drive_api.ResourceID:
    """
    Create Google Drive file with specific MIME type.
    """
    request = _resource_request(name,
                                mime_type=mime_type,
                                parent_folder_id=parent_folder_id,
                                drive_service=drive_service)
    resource = request.execute()
    return resource.get('id')


# ---------------------------------------------------------------------
# Batch
# ---------------------------------------------------------------------

def batch_gdoc(targets: List[drive_api.NameAndParent], *,
               drive_service: discovery.Resource = None) -> List[drive_api.ResourceID]:
    """
    Batch create empty Google Docs.
    """
    return _batch_resource(targets=targets,
                           mime_type=mime_types.gdoc,
                           drive_service=drive_service)


def batch_gsheet(targets: List[drive_api.NameAndParent], *,
                 drive_service: discovery.Resource = None) -> List[drive_api.ResourceID]:
    """
    Batch create empty Google Sheets.
    """
    return _batch_resource(targets=targets,
                           mime_type=mime_types.gsheets,
                           drive_service=drive_service)


def batch_gslides(targets: List[drive_api.NameAndParent], *,
                  drive_service: discovery.Resource = None) -> List[drive_api.ResourceID]:
    """
    Batch create empty Google Slides presentations.
    """
    return _batch_resource(targets=targets,
                           mime_type=mime_types.gslides,
                           drive_service=drive_service)


def batch_gform(targets: List[drive_api.NameAndParent], *,
                drive_service: discovery.Resource = None) -> List[drive_api.ResourceID]:
    """
    Batch create empty Google Forms.
    """
    return _batch_resource(targets=targets,
                           mime_type=mime_types.gform,
                           drive_service=drive_service)


def batch_file(targets: List[drive_api.NameAndParent], *,
               mime_type: str,
               drive_service: discovery.Resource = None) -> List[drive_api.ResourceID]:
    """
    Batch create empty files.
    """
    return _batch_resource(targets=targets,
                           mime_type=mime_type,
                           drive_service=drive_service)


def batch_folder(targets: List[drive_api.NameAndParent], *,
                 drive_service: discovery.Resource = None) -> List[drive_api.ResourceID]:
    """
    Batch create empty folders.
    """
    return _batch_resource(targets=targets,
                           mime_type=mime_types.folder,
                           drive_service=drive_service)


def _batch_resource(targets: List[drive_api.NameAndParent], *,
                    mime_type: str,
                    drive_service: discovery.Resource = None) -> List[drive_api.ResourceID]:
    """
    Batch create Google Drive file with specific MIME type.

    Returns list of IDs in order of passed names.
    """
    result = []  # callback will append resulting IDs in order

    def batch_response(request_id, response, exception) -> None:
        nonlocal result
        result.append(response.get('id'))

    requests = [_resource_request(name=target.name,
                                  mime_type=mime_type,
                                  parent_folder_id=target.parent_folder_id,
                                  drive_service=drive_service)
                for target in targets]
    drive_api.batch_command(callback=batch_response,
                            requests=requests,
                            drive_service=drive_service)
    return result


# ---------------------------------------------------------------------
# Generate request (allows delayed execution)
# ---------------------------------------------------------------------

def gdoc_request(file_name: str, *,
                 parent_folder_id: drive_api.ResourceID,
                 drive_service: discovery.Resource = None) -> http.HttpRequest:
    """
    Generate request to create new Google doc.
    """
    return _resource_request(name=file_name,
                             mime_type=mime_types.gdoc,
                             parent_folder_id=parent_folder_id,
                             drive_service=drive_service)


def gsheet_request(file_name: str, *,
                   parent_folder_id: drive_api.ResourceID,
                   drive_service: discovery.Resource = None) -> http.HttpRequest:
    """
    Generate request to create new Google sheet.
    """
    return _resource_request(name=file_name,
                             mime_type=mime_types.gsheets,
                             parent_folder_id=parent_folder_id,
                             drive_service=drive_service)


def gslides_request(file_name: str, *,
                    parent_folder_id: drive_api.ResourceID,
                    drive_service: discovery.Resource = None) -> http.HttpRequest:
    """
    Generate request to create new Google slides presentation.
    """
    return _resource_request(name=file_name,
                             mime_type=mime_types.gslides,
                             parent_folder_id=parent_folder_id,
                             drive_service=drive_service)


def gform_request(file_name: str, *,
                  parent_folder_id: drive_api.ResourceID,
                  drive_service: discovery.Resource = None) -> http.HttpRequest:
    """
    Generate request to create new Google form.
    """
    return _resource_request(name=file_name,
                             mime_type=mime_types.gform,
                             parent_folder_id=parent_folder_id,
                             drive_service=drive_service)


def file_request(file_name: str, *,
                 mime_type: str,
                 parent_folder_id: drive_api.ResourceID,
                 drive_service: discovery.Resource = None) -> http.HttpRequest:
    """
    Generate request to create new file.
    """
    return _resource_request(name=file_name,
                             mime_type=mime_type,
                             parent_folder_id=parent_folder_id,
                             drive_service=drive_service)


def folder_request(folder_name: str, *,
                   parent_folder_id: drive_api.ResourceID,
                   drive_service: discovery.Resource = None) -> http.HttpRequest:
    """
    Generate request to create new folder.
    """
    return _resource_request(name=folder_name,
                             mime_type=mime_types.folder,
                             parent_folder_id=parent_folder_id,
                             drive_service=drive_service)


def _resource_request(name: str, *,
                      mime_type: str,
                      parent_folder_id: drive_api.ResourceID,
                      drive_service: discovery.Resource = None) -> http.HttpRequest:
    """
    Generate request to create new resource.
    """
    if drive_service is None:
        drive_service = drive_api.build_service()
    file_metadata = {
        'name': name,
        'mimeType': f'application/vnd.google-apps.{mime_type}',
        'parents': [parent_folder_id]
    }
    return drive_service \
        .files() \
        .create(body=file_metadata, fields='id')
