"""
Move a file or folder from source into the specified targets.
"""

from backend.src.google_apis import drive_api

ResourceID = str


def file(origin_file_id: ResourceID,
         target_folder_id: ResourceID) -> None:
    """
    Move file.
    """
    _move_resource(origin_resource_id=origin_file_id,
                   target_folder_id=target_folder_id)


def folder(origin_folder_id: ResourceID,
           target_folder_id: ResourceID) -> None:
    """
    Move folder.
    """
    _move_resource(origin_resource_id=origin_folder_id,
                   target_folder_id=target_folder_id)


def _move_resource(origin_resource_id: ResourceID,
                   target_folder_id: ResourceID) -> None:
    """
    Move file helper.
    """
    service = drive_api.build_service()
    file_metadata = service.files().get(fileId=origin_resource_id,
                                        fields='parents').execute()
    previous_parents = ",".join(file_metadata.get('parents'))
    service.files().update(fileId=origin_resource_id,
                           addParents=target_folder_id,
                           removeParents=previous_parents,
                           fields='id, parents').execute()
