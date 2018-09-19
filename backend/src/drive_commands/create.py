"""
Create an empty file or folder into the specified targets.
"""
from typing import List, NamedTuple, Optional

from googleapiclient import discovery, http

from backend.src.data import mime_types
from backend.src.google_apis import drive_api


# ---------------------------------------------------------------------
# Single resource (immediate execution)
# ---------------------------------------------------------------------


def gdoc(
    file_name: str,
    *,
    parent_folder_id: drive_api.ResourceID,
    drive_service: discovery.Resource = None,
) -> drive_api.ResourceID:
    """
    Create an empty Google Doc.
    """
    return resource(
        name=file_name,
        mime_type=mime_types.gdoc,
        parent_folder_id=parent_folder_id,
        drive_service=drive_service,
    )


def gsheet(
    file_name: str,
    *,
    parent_folder_id: drive_api.ResourceID,
    drive_service: discovery.Resource = None,
) -> drive_api.ResourceID:
    """
    Create an empty Google Sheet.
    """
    return resource(
        name=file_name,
        mime_type=mime_types.gsheets,
        parent_folder_id=parent_folder_id,
        drive_service=drive_service,
    )


def gslides(
    file_name: str,
    *,
    parent_folder_id: drive_api.ResourceID,
    drive_service: discovery.Resource = None,
) -> drive_api.ResourceID:
    """
    Create an empty Google Slides presentation.
    """
    return resource(
        name=file_name,
        mime_type=mime_types.gslides,
        parent_folder_id=parent_folder_id,
        drive_service=drive_service,
    )


def gform(
    file_name: str,
    *,
    parent_folder_id: drive_api.ResourceID,
    drive_service: discovery.Resource = None,
) -> drive_api.ResourceID:
    """
    Create an empty Google Form.
    """
    return resource(
        name=file_name,
        mime_type=mime_types.gform,
        parent_folder_id=parent_folder_id,
        drive_service=drive_service,
    )


def folder(
    folder_name: str,
    *,
    parent_folder_id: drive_api.ResourceID,
    drive_service: discovery.Resource = None,
) -> drive_api.ResourceID:
    """
    Create an empty folder.
    """
    return resource(
        name=folder_name,
        mime_type=mime_types.folder,
        parent_folder_id=parent_folder_id,
        drive_service=drive_service,
    )


def resource(
    name: str,
    *,
    mime_type: str,
    parent_folder_id: drive_api.ResourceID,
    drive_service: discovery.Resource = None,
) -> drive_api.ResourceID:
    """
    Create Google Drive file with specific MIME type.
    """
    command = request(
        name,
        mime_type=mime_type,
        parent_folder_id=parent_folder_id,
        drive_service=drive_service,
    )
    result = command.execute()
    return result.get("id")


# ---------------------------------------------------------------------
# Batch (immediate execution)
# ---------------------------------------------------------------------


class BatchArgument(NamedTuple):
    name: str
    parent_folder_id: drive_api.ResourceID
    mime_type: Optional[str] = None


def batch_gdoc(
    arguments: List[BatchArgument],
    *,
    include_output: bool = True,
    drive_service: discovery.Resource = None,
) -> List[drive_api.ResourceID]:
    """
    Batch create empty Google Docs.
    """
    return batch(
        arguments=arguments,
        uniform_mime_type=mime_types.gdoc,
        include_output=include_output,
        drive_service=drive_service,
    )


def batch_gsheet(
    arguments: List[BatchArgument],
    *,
    include_output: bool = True,
    drive_service: discovery.Resource = None,
) -> List[drive_api.ResourceID]:
    """
    Batch create empty Google Sheets.
    """
    return batch(
        arguments=arguments,
        uniform_mime_type=mime_types.gsheets,
        include_output=include_output,
        drive_service=drive_service,
    )


def batch_gslides(
    arguments: List[BatchArgument],
    *,
    include_output: bool = True,
    drive_service: discovery.Resource = None,
) -> List[drive_api.ResourceID]:
    """
    Batch create empty Google Slides presentations.
    """
    return batch(
        arguments=arguments,
        uniform_mime_type=mime_types.gslides,
        include_output=include_output,
        drive_service=drive_service,
    )


def batch_gform(
    arguments: List[BatchArgument],
    *,
    include_output: bool = True,
    drive_service: discovery.Resource = None,
) -> List[drive_api.ResourceID]:
    """
    Batch create empty Google Forms.
    """
    return batch(
        arguments=arguments,
        uniform_mime_type=mime_types.gform,
        include_output=include_output,
        drive_service=drive_service,
    )


def batch_folder(
    arguments: List[BatchArgument],
    *,
    include_output: bool = True,
    drive_service: discovery.Resource = None,
) -> List[drive_api.ResourceID]:
    """
    Batch create empty folders.
    """
    return batch(
        arguments=arguments,
        uniform_mime_type=mime_types.folder,
        include_output=include_output,
        drive_service=drive_service,
    )


def batch(
    arguments: List[BatchArgument],
    *,
    uniform_mime_type: str = None,
    include_output: bool = True,
    drive_service: discovery.Resource = None,
) -> List[drive_api.ResourceID]:
    """
    Batch create Google Drive file with specific MIME type.

    Returns list of IDs in order of passed names.
    """
    # mime support
    if uniform_mime_type is None and any(
        argument.mime_type is None for argument in arguments
    ):
        raise ValueError("Invalid batch arguments. Every file must have a mime type.")
    else:
        arguments = [
            BatchArgument(
                name=argument.name,
                parent_folder_id=argument.parent_folder_id,
                mime_type=uniform_mime_type,
            )
            for argument in arguments
        ]

    result = []  # callback will append resulting IDs in order

    def batch_response(request_id, response, exception) -> None:
        nonlocal result
        result.append(response.get("id"))

    requests = [
        request(
            name=argument.name,  # type: ignore  # complains about mime_type being Optional
            mime_type=argument.mime_type,
            parent_folder_id=argument.parent_folder_id,
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


def gdoc_request(
    file_name: str,
    *,
    parent_folder_id: drive_api.ResourceID,
    drive_service: discovery.Resource = None,
) -> http.HttpRequest:
    """
    Generate request to create new Google doc.
    """
    return request(
        name=file_name,
        mime_type=mime_types.gdoc,
        parent_folder_id=parent_folder_id,
        drive_service=drive_service,
    )


def gsheet_request(
    file_name: str,
    *,
    parent_folder_id: drive_api.ResourceID,
    drive_service: discovery.Resource = None,
) -> http.HttpRequest:
    """
    Generate request to create new Google sheet.
    """
    return request(
        name=file_name,
        mime_type=mime_types.gsheets,
        parent_folder_id=parent_folder_id,
        drive_service=drive_service,
    )


def gslides_request(
    file_name: str,
    *,
    parent_folder_id: drive_api.ResourceID,
    drive_service: discovery.Resource = None,
) -> http.HttpRequest:
    """
    Generate request to create new Google slides presentation.
    """
    return request(
        name=file_name,
        mime_type=mime_types.gslides,
        parent_folder_id=parent_folder_id,
        drive_service=drive_service,
    )


def gform_request(
    file_name: str,
    *,
    parent_folder_id: drive_api.ResourceID,
    drive_service: discovery.Resource = None,
) -> http.HttpRequest:
    """
    Generate request to create new Google form.
    """
    return request(
        name=file_name,
        mime_type=mime_types.gform,
        parent_folder_id=parent_folder_id,
        drive_service=drive_service,
    )


def folder_request(
    folder_name: str,
    *,
    parent_folder_id: drive_api.ResourceID,
    drive_service: discovery.Resource = None,
) -> http.HttpRequest:
    """
    Generate request to create new folder.
    """
    return request(
        name=folder_name,
        mime_type=mime_types.folder,
        parent_folder_id=parent_folder_id,
        drive_service=drive_service,
    )


def request(
    name: str,
    *,
    mime_type: str,
    parent_folder_id: drive_api.ResourceID,
    drive_service: discovery.Resource = None,
) -> http.HttpRequest:
    """
    Generate request to create new resource.
    """
    if drive_service is None:
        drive_service = drive_api.build_service()
    file_metadata = {
        "name": name,
        "mimeType": f"application/vnd.google-apps.{mime_type}",
        "parents": [parent_folder_id],
    }
    return drive_service.files().create(body=file_metadata, fields="id")
