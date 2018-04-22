"""
Copy a file or folder from source into the specified targets.
"""
import textwrap
import time
from typing import NamedTuple

from googleapiclient import discovery

from backend.src.drive_commands import find, move, rename
from backend.src.google_apis import drive_api

ResourceID = str


def file(*,
         origin_file_id: ResourceID,
         new_name: str,
         target_parent_folder_id: ResourceID,
         drive_service: discovery.Resource = None) -> ResourceID:
    """
    Copy the file into targets.

    Should maintain permissions and file metadata.
    """
    if drive_service is None:
        drive_service = drive_api.build_service()
    file_metadata = {
        'name': new_name,
        'parents': [target_parent_folder_id]
    }
    resource = drive_service \
        .files() \
        .copy(fileId=origin_file_id, body=file_metadata, fields='id') \
        .execute()
    return resource.get('id')


class SheetAndForm(NamedTuple):
    sheet: ResourceID
    form: ResourceID


def linked_sheet_and_form(*,
                          origin_sheet_id: ResourceID,
                          origin_form_id: ResourceID,
                          origin_parent_folder_id: ResourceID = None,
                          new_sheet_name: str,
                          new_form_name: str,
                          target_parent_folder_id: ResourceID,
                          drive_service: discovery.Resource = None,
                          initial_form_search_delay: int = 10,
                          timeout: int = 45) -> SheetAndForm:
    """
    Copy both the spreadsheet and its accompanying form.

    This is because when you copy a spreadsheet linked to a form, the form will automatically be copied as well.
    So, this command will find that copied form, rename it, and move to the same parent.

    Because the form is not created instantly, uses a timeout mechanism to search multiple times.
    """
    if drive_service is None:
        drive_service = drive_api.build_service()
    if origin_parent_folder_id is None:
        origin_parent_folder_id = find.parent_folder(origin_form_id)
    original_form_name = find.name(origin_form_id)
    sheet = file(origin_file_id=origin_sheet_id,
                 target_parent_folder_id=target_parent_folder_id,
                 new_name=new_sheet_name,
                 drive_service=drive_service)

    def find_form_copy(time_delay: int, total_time_elapsed: int = 0) -> ResourceID:
        time.sleep(time_delay)
        copy_id = find.gform(file_name=f'Copy of {original_form_name}',
                             parent_folder_id=origin_parent_folder_id,
                             drive_service=drive_service)
        updated_time_elapsed = total_time_elapsed + time_delay
        time_remaining = timeout - updated_time_elapsed
        if copy_id is None and time_remaining <= timeout:
            print(textwrap.dedent(f'''
                Form copy of {original_form_name} not found. 
                Trying again, this time waiting {time_delay*2} seconds.
                Will timeout in {time_remaining} seconds.'''))
            return find_form_copy(time_delay * 2, total_time_elapsed=updated_time_elapsed)
        return copy_id

    form_copy_id = find_form_copy(initial_form_search_delay)  # use time delay to make sure form created
    rename.file(file_id=form_copy_id,
                new_name=new_form_name,
                drive_service=drive_service)
    move.file(origin_file_id=form_copy_id,
              target_folder_id=target_parent_folder_id,
              drive_service=drive_service)
    return SheetAndForm(sheet=sheet, form=form_copy_id)
