"""
Copy a file (not folder) from source into the specified targets.
"""
import textwrap
import time
from typing import List, NamedTuple, Optional

from googleapiclient import discovery, http

from backend.src.data import mime_types
from backend.src.drive_commands import find, move, rename
from backend.src.google_apis import drive_api


# ---------------------------------------------------------------------
# Single resource (delayed execution)
# ---------------------------------------------------------------------


def file(
    *,
    origin_file_id: drive_api.ResourceID,
    new_name: str,
    target_parent_folder_id: drive_api.ResourceID,
    drive_service: Optional[discovery.Resource] = None,
) -> drive_api.ResourceID:
    """
    Copy the file into targets.

    Should maintain permissions and file metadata.
    """
    command = request(
        origin_file_id=origin_file_id,
        new_name=new_name,
        target_parent_folder_id=target_parent_folder_id,
        drive_service=drive_service,
    )
    result = command.execute()
    new_id: drive_api.ResourceID = result.get("id")
    return new_id


# ---------------------------------------------------------------------
# Batch (immediate execution)
# ---------------------------------------------------------------------


class BatchArgument(NamedTuple):
    origin_resource_id: drive_api.ResourceID
    new_name: str
    target_folder_id: drive_api.ResourceID


def batch(
    arguments: List[BatchArgument],
    *,
    include_output: bool = True,
    drive_service: Optional[discovery.Resource] = None,
) -> List[drive_api.ResourceID]:
    """
    Batch copy Google Drive files.

    Returns list of IDs in order of passed names.
    """
    result = []  # callback will append resulting IDs in order

    def batch_response(request_id, response, exception) -> None:
        nonlocal result
        result.append(response.get("id"))

    requests = [
        request(
            origin_file_id=argument.origin_resource_id,
            new_name=argument.new_name,
            target_parent_folder_id=argument.target_folder_id,
            drive_service=drive_service,
        )
        for argument in arguments
    ]
    kwargs = {"requests": requests, "drive_service": drive_service}
    if include_output:
        kwargs["callback"] = batch_response
    drive_api.batch_command(**kwargs)
    return result


# ---------------------------------------------------------------------
# Generate request (delayed execution)
# ---------------------------------------------------------------------


def request(
    *,
    origin_file_id: drive_api.ResourceID,
    new_name: str,
    target_parent_folder_id: drive_api.ResourceID,
    drive_service: Optional[discovery.Resource] = None,
) -> http.HttpRequest:
    """
    Generate request to copy the file into targets.

    Should maintain permissions and file metadata.
    """
    if drive_service is None:
        drive_service = drive_api.build_service()
    file_metadata = {"name": new_name, "parents": [target_parent_folder_id]}
    return drive_service.files().copy(
        fileId=origin_file_id, body=file_metadata, fields="id"
    )


# ---------------------------------------------------------------------
# Linked sheet and form
# ---------------------------------------------------------------------


class SheetAndForm(NamedTuple):
    sheet: drive_api.ResourceID
    form: drive_api.ResourceID


def linked_sheet_and_form(
    *,
    origin_sheet_id: drive_api.ResourceID,
    origin_form_id: drive_api.ResourceID,
    origin_parent_folder_id: Optional[drive_api.ResourceID] = None,
    new_sheet_name: str,
    new_form_name: str,
    target_parent_folder_id: drive_api.ResourceID,
    drive_service: Optional[discovery.Resource] = None,
    initial_form_search_delay: int = 10,
    timeout: int = 45,
) -> SheetAndForm:
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
    copied_sheet_id = file(
        origin_file_id=origin_sheet_id,
        target_parent_folder_id=target_parent_folder_id,
        new_name=new_sheet_name,
        drive_service=drive_service,
    )

    def find_copied_form(
        time_delay: int, total_time_elapsed: int = 0
    ) -> drive_api.ResourceID:
        time.sleep(time_delay)
        copy_id = find.resource(
            resource_name=f"Copy of {original_form_name}",
            parent_folder_id=origin_parent_folder_id,
            mime_type=mime_types.gform,
            drive_service=drive_service,
        )
        updated_time_elapsed = total_time_elapsed + time_delay
        time_remaining = timeout - updated_time_elapsed
        if copy_id is None:
            if time_remaining > timeout:
                raise OSError(
                    "Cannot find the copied form. Check that it was created in Google Drive."
                )
            print(
                textwrap.dedent(
                    f"""\
                Copy of the form {original_form_name} not found yet.
                Trying again, this time waiting {time_delay*2} seconds.
                Will timeout in {time_remaining} seconds."""
                )
            )
            return find_copied_form(
                time_delay * 2, total_time_elapsed=updated_time_elapsed
            )
        return copy_id

    # use time delay to make sure form created
    copied_form_id = find_copied_form(initial_form_search_delay)

    drive_api.batch_command(
        requests=[
            rename.request(
                resource_id=copied_form_id,
                new_name=new_form_name,
                drive_service=drive_service,
            ),
            move.request(
                origin_resource_id=copied_form_id,
                target_folder_id=target_parent_folder_id,
                drive_service=drive_service,
            ),
        ],
        drive_service=drive_service,
    )
    return SheetAndForm(sheet=copied_sheet_id, form=copied_form_id)
