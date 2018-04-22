"""
Locate and return a file or folder ID for the specified targets.
"""
from typing import List, Optional

from googleapiclient import discovery

from backend.src.data import mime_types
from backend.src.google_apis import drive_api

ResourceID = str


# -----------------------------------------------------
# Find ID
# -----------------------------------------------------

def gdoc(file_name: str, *,
         parent_folder_id: ResourceID,
         exact_match: bool = True,
         drive_service: discovery.Resource = None) -> ResourceID:
    """
    Find a Google Doc with given name and parent.
    """
    return _resource(resource_name=file_name,
                     mime_type=mime_types.gdoc,
                     parent_folder_id=parent_folder_id,
                     exact_match=exact_match,
                     drive_service=drive_service)


def gsheet(file_name: str, *,
           parent_folder_id: ResourceID,
           exact_match: bool = True,
           drive_service: discovery.Resource = None) -> ResourceID:
    """
    Find a Google Sheet with given name and parent.
    """
    return _resource(resource_name=file_name,
                     mime_type=mime_types.gsheets,
                     parent_folder_id=parent_folder_id,
                     exact_match=exact_match,
                     drive_service=drive_service)


def gslides(file_name: str, *,
            parent_folder_id: ResourceID,
            exact_match: bool = True,
            drive_service: discovery.Resource = None) -> ResourceID:
    """
    Find a Google Slides with given name and parent.
    """
    return _resource(resource_name=file_name,
                     mime_type=mime_types.gslides,
                     parent_folder_id=parent_folder_id,
                     exact_match=exact_match,
                     drive_service=drive_service)


def gform(file_name: str, *,
          parent_folder_id: ResourceID,
          exact_match: bool = True,
          drive_service: discovery.Resource = None) -> ResourceID:
    """
    Find a Google Form with given name and parent.
    """
    return _resource(resource_name=file_name,
                     mime_type=mime_types.gform,
                     parent_folder_id=parent_folder_id,
                     exact_match=exact_match,
                     drive_service=drive_service)


def file(file_name: str, *,
         parent_folder_id: ResourceID,
         mime_type: str = None,
         exact_match: bool = True,
         drive_service: discovery.Resource = None) -> Optional[ResourceID]:
    """
    Find file.
    """
    return _resource(resource_name=file_name,
                     parent_folder_id=parent_folder_id,
                     mime_type=mime_type,
                     exact_match=exact_match,
                     drive_service=drive_service)


def folder(folder_name: str, *,
           parent_folder_id: ResourceID,
           exact_match: bool = True,
           drive_service: discovery.Resource = None) -> Optional[ResourceID]:
    """
    Find folder.
    """
    return _resource(resource_name=folder_name,
                     parent_folder_id=parent_folder_id,
                     mime_type=mime_types.folder,
                     exact_match=exact_match,
                     drive_service=drive_service)


def _resource(resource_name: str, *,
              parent_folder_id: ResourceID,
              mime_type: str = None,
              exact_match: bool = True,
              drive_service: discovery.Resource = None) -> Optional[ResourceID]:
    """
    Helper for finding files and folders
    """
    if drive_service is None:
        drive_service = drive_api.build_service()
    query = f"'{parent_folder_id}' in parents"
    query += f" and name='{resource_name}'" \
        if exact_match \
        else f" and name contains '{resource_name}'"
    if mime_type:
        query += f" and mimeType='application/vnd.google-apps.{mime_type}'"
    results = drive_service \
        .files() \
        .list(q=query,
              pageSize=2,
              fields="nextPageToken, files(id)") \
        .execute()
    files = results.get('files', [])
    if len(files) != 1:  # empty or ambiguous results -> failure
        return None
    return files[0]['id']


# -----------------------------------------------------
# Find attributes
# -----------------------------------------------------

def parent_folder(resource_id: ResourceID, *,
                  drive_service: discovery.Resource = None) -> ResourceID:
    """
    Find parent folder ID for resource.
    """
    parents = parent_folder_list(resource_id=resource_id, drive_service=drive_service)
    return parents[0]


def parent_folder_list(resource_id: ResourceID, *,
                       drive_service: discovery.Resource = None) -> List[ResourceID]:
    """
    Find all parent folder IDs for resource.
    """
    if drive_service is None:
        drive_service = drive_api.build_service()
    result = drive_service \
        .files() \
        .get(fileId=resource_id, fields='parents') \
        .execute()
    return result['parents']


def name(resource_id: ResourceID, *,
         drive_service: discovery.Resource = None) -> str:
    """
    Find the original name of the resource.
    """
    if drive_service is None:
        drive_service = drive_api.build_service()
    result = drive_service \
        .files() \
        .get(fileId=resource_id, fields='name') \
        .execute()
    return result['name']
