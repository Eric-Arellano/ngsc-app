"""
Move a file or folder from source into the specified targets.
"""
from googleapiclient import discovery

from backend.src.drive_commands import find
from backend.src.google_apis import drive_api

ResourceID = str


def file(*,
         origin_file_id: ResourceID,
         target_folder_id: ResourceID,
         drive_service: discovery.Resource = None) -> None:
    """
    Move file.
    """
    _move_resource(origin_resource_id=origin_file_id,
                   target_folder_id=target_folder_id,
                   drive_service=drive_service)


def folder(*,
           origin_folder_id: ResourceID,
           target_folder_id: ResourceID,
           drive_service: discovery.Resource = None) -> None:
    """
    Move folder.
    """
    _move_resource(origin_resource_id=origin_folder_id,
                   target_folder_id=target_folder_id,
                   drive_service=drive_service)


def _move_resource(*,
                   origin_resource_id: ResourceID,
                   target_folder_id: ResourceID,
                   drive_service: discovery.Resource = None) -> None:
    """
    Move resource helper.
    """
    if drive_service is not None:
        drive_service = drive_api.build_service()
    previous_parents = find.parent_folder_list(resource_id=origin_resource_id)
    previous_parents_formatted = ', '.join(previous_parents)
    drive_service \
        .files() \
        .update(fileId=origin_resource_id,
                addParents=target_folder_id,
                removeParents=previous_parents_formatted,
                fields='id, parents') \
        .execute()
