"""
Locate and return a file or folder ID for the specified targets.
"""
from typing import Optional

from backend.src.data import mime_types
from backend.src.google_apis import drive_api

ResourceID = str


def gdoc(file_name: str, *,
         parent_folder_id: ResourceID,
         exact_match: bool = True) -> ResourceID:
    """
    Find a Google Doc with given name and parent.
    """
    return _find_resource(name=file_name,
                          mime_type=mime_types.gdoc,
                          parent_folder_id=parent_folder_id,
                          exact_match=exact_match)


def gsheet(file_name: str, *,
           parent_folder_id: ResourceID,
           exact_match: bool = True) -> ResourceID:
    """
    Find a Google Sheet with given name and parent.
    """
    return _find_resource(name=file_name,
                          mime_type=mime_types.gsheets,
                          parent_folder_id=parent_folder_id,
                          exact_match=exact_match)


def gslides(file_name: str, *,
            parent_folder_id: ResourceID,
            exact_match: bool = True) -> ResourceID:
    """
    Find a Google Slides with given name and parent.
    """
    return _find_resource(name=file_name,
                          mime_type=mime_types.gslides,
                          parent_folder_id=parent_folder_id,
                          exact_match=exact_match)


def gform(file_name: str, *,
          parent_folder_id: ResourceID,
          exact_match: bool = True) -> ResourceID:
    """
    Find a Google Form with given name and parent.
    """
    return _find_resource(name=file_name,
                          mime_type=mime_types.gform,
                          parent_folder_id=parent_folder_id,
                          exact_match=exact_match)


def file(file_name: str, *,
         parent_folder_id: ResourceID,
         mime_type: str = None,
         exact_match: bool = True) -> Optional[ResourceID]:
    """
    Find file.
    """
    return _find_resource(name=file_name,
                          parent_folder_id=parent_folder_id,
                          mime_type=mime_type,
                          exact_match=exact_match)


def folder(folder_name: str, *,
           parent_folder_id: ResourceID,
           exact_match: bool = True) -> Optional[ResourceID]:
    """
    Find folder.
    """
    return _find_resource(name=folder_name,
                          parent_folder_id=parent_folder_id,
                          mime_type=mime_types.folder,
                          exact_match=exact_match)


def _find_resource(name: str, *,
                   parent_folder_id: ResourceID,
                   mime_type: str = None,
                   exact_match: bool = True) -> Optional[ResourceID]:
    """
    Helper for finding files and folders
    """
    query = f"'{parent_folder_id}' in parents"
    query += f" and name='{name}'" \
        if exact_match \
        else f" and name contains '{name}'"
    if mime_type:
        query += f" and mimeType='application/vnd.google-apps.{mime_type}'"
    service = drive_api.build_service()
    results = service \
        .files() \
        .list(q=query,
              pageSize=10,
              fields="nextPageToken, files(id)") \
        .execute()
    items = results.get('files', [])
    if len(items) != 1:  # empty or ambiguous results -> failure
        return None
    return items[0]['id']
