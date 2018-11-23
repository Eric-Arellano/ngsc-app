"""
Locate and return a file or folder ID for the specified targets.
"""
from typing import List, Optional

from googleapiclient import discovery

from backend.src.data import mime_types
from backend.src.google_apis import drive_api


# -----------------------------------------------------
# Find ID
# -----------------------------------------------------


def resource(
    resource_name: str,
    *,
    parent_folder_id: drive_api.ResourceID,
    mime_type: Optional[str] = None,
    exact_match: bool = True,
    drive_service: Optional[discovery.Resource] = None,
) -> Optional[drive_api.ResourceID]:
    """
    Helper for finding files and folders
    """
    if drive_service is None:
        drive_service = drive_api.build_service()
    query = f"'{parent_folder_id}' in parents"
    query += (
        f" and name='{resource_name}'"
        if exact_match
        else f" and name contains '{resource_name}'"
    )
    if mime_type:
        query += f" and mimeType='application/vnd.google-apps.{mime_type}'"
    results = (
        drive_service.files()
        .list(q=query, pageSize=2, fields="nextPageToken, files(id)")
        .execute()
    )
    files = results.get("files", [])
    if len(files) != 1:  # empty or ambiguous results -> failure
        return None
    resource_id: drive_api.ResourceID = files[0]["id"]
    return resource_id


# -----------------------------------------------------
# Find ID (Recursive)
# -----------------------------------------------------


def parent_folder_for_path(
    path: str,
    *,
    root_folder_id: drive_api.ResourceID,
    drive_service: discovery.Resource,
) -> Optional[drive_api.ResourceID]:
    """
    If path is nested, find actual parent; else return original parent.
    """
    path_list = path.split("/")
    if len(path_list) == 1:
        return root_folder_id
    path_without_child = path_list[:-1]
    return recursive_resource(
        path=path_without_child,
        parent_folder_id=root_folder_id,
        mime_type=mime_types.folder,
        drive_service=drive_service,
    )


def recursive_resource(
    *,
    path: List[str],
    parent_folder_id: drive_api.ResourceID,
    mime_type: Optional[str] = None,
    exact_match: bool = True,
    drive_service: Optional[discovery.Resource] = None,
) -> Optional[drive_api.ResourceID]:
    if len(path) == 1:
        return resource(
            resource_name=path[0],
            parent_folder_id=parent_folder_id,
            mime_type=mime_type,
            exact_match=exact_match,
            drive_service=drive_service,
        )
    new_path = path[1:]
    new_parent_id = resource(
        resource_name=path[0],
        parent_folder_id=parent_folder_id,
        exact_match=exact_match,
        drive_service=drive_service,
    )
    if new_parent_id is None:
        raise OSError(
            f"Could not find resource ID for {path[0]} with parent_folder_id={parent_folder_id} "
            f"and full path={path}."
        )
    return recursive_resource(
        path=new_path,
        parent_folder_id=new_parent_id,
        mime_type=mime_type,
        exact_match=exact_match,
        drive_service=drive_service,
    )


# -----------------------------------------------------
# Find attributes
# -----------------------------------------------------\


def parent_folder(
    resource_id: drive_api.ResourceID,
    *,
    drive_service: Optional[discovery.Resource] = None,
) -> drive_api.ResourceID:
    """
    Find parent folder ID for resource.
    """
    parents = parent_folder_list(resource_id=resource_id, drive_service=drive_service)
    return parents[0]


def parent_folder_list(
    resource_id: drive_api.ResourceID,
    *,
    drive_service: Optional[discovery.Resource] = None,
) -> List[drive_api.ResourceID]:
    """
    Find all parent folder IDs for resource.
    """
    if drive_service is None:
        drive_service = drive_api.build_service()
    result = drive_service.files().get(fileId=resource_id, fields="parents").execute()
    parent_ids: List[drive_api.ResourceID] = result["parents"]
    return parent_ids


def name(
    resource_id: drive_api.ResourceID,
    *,
    drive_service: Optional[discovery.Resource] = None,
) -> str:
    """
    Find the original name of the resource.
    """
    if drive_service is None:
        drive_service = drive_api.build_service()
    result = drive_service.files().get(fileId=resource_id, fields="name").execute()
    name: str = result["name"]
    return name
