"""
Share a resource within Google Drive.
"""
from typing import List, NamedTuple, Optional

from googleapiclient import discovery, http

from backend.src.google_apis import drive_api


# ---------------------------------------------------------------------
# Single resource (immediate execution)
# ---------------------------------------------------------------------


def resource(
    resource_id: drive_api.ResourceID,
    email: str,
    *,
    email_message: str = None,
    send_email: bool = False,
    transfer_ownership: bool = False,
    drive_service: discovery.Resource = None,
) -> None:
    """
    Share specific resource with single user.
    """
    command = request(
        resource_id=resource_id,
        email=email,
        email_message=email_message,
        send_email=send_email,
        transfer_ownership=transfer_ownership,
        drive_service=drive_service,
    )
    command.execute()


# ---------------------------------------------------------------------
# Batch (immediate execution)
# ---------------------------------------------------------------------


class BatchArgument(NamedTuple):
    resource_id: drive_api.ResourceID
    emails: List[str]
    email_message: Optional[str] = None
    send_email: bool = False
    transfer_ownership: bool = False


def batch(
    arguments: List[BatchArgument],
    *,
    uniform_email_message: str = None,
    uniform_send_email: bool = False,
    uniform_transfer_ownership: bool = False,
    drive_service: discovery.Resource = None,
) -> None:
    """
    Batch share resources with provided users.
    """
    # convert uniform parameters
    if uniform_email_message is not None:
        arguments = [
            BatchArgument(
                resource_id=argument.resource_id,
                emails=argument.emails,
                email_message=uniform_email_message,
                send_email=argument.send_email,
                transfer_ownership=argument.transfer_ownership,
            )
            for argument in arguments
        ]
    if uniform_send_email is True:
        arguments = [
            BatchArgument(
                resource_id=argument.resource_id,
                emails=argument.emails,
                email_message=argument.email_message,
                send_email=True,
                transfer_ownership=argument.transfer_ownership,
            )
            for argument in arguments
        ]
    if uniform_transfer_ownership is True:
        arguments = [
            BatchArgument(
                resource_id=argument.resource_id,
                emails=argument.emails,
                email_message=argument.email_message,
                send_email=True,
                transfer_ownership=True,
            )
            for argument in arguments
        ]
    # generate requests
    requests = [
        [
            request(
                resource_id=argument.resource_id,
                email=email,
                email_message=argument.email_message,
                send_email=argument.send_email,
                transfer_ownership=argument.transfer_ownership,
                drive_service=drive_service,
            )
            for email in argument.emails
        ]
        for argument in arguments
    ]
    requests_flattened = [x for y in requests for x in y]
    # execute
    drive_api.batch_command(requests=requests_flattened, drive_service=drive_service)


# ---------------------------------------------------------------------
# Generate request (delayed execution)
# ---------------------------------------------------------------------


def request(
    resource_id: drive_api.ResourceID,
    email: str,
    *,
    email_message: str = None,
    send_email: bool = False,
    transfer_ownership: bool = False,
    drive_service: discovery.Resource = None,
) -> http.HttpRequest:
    """
    Generate request to share specific resource with user.

    Email message can have multiple lines.
    """
    if drive_service is None:
        drive_service = drive_api.build_service()
    user_permission = {
        "type": "user",
        "role": "writer" if not transfer_ownership else "owner",
        "emailAddress": email,
    }
    if transfer_ownership:
        send_email = True  # API requires this
    return drive_service.permissions().create(
        fileId=resource_id,
        body=user_permission,
        emailMessage=email_message,
        sendNotificationEmail=send_email,
        transferOwnership=transfer_ownership,
        fields="",
    )
