from typing import Any, List

from backend.src.google_apis import sheets_api


def batch_update(spreadsheet_id: str, requests: List) -> None:
    """
    Perform an operation on the spreadsheet.
    """
    sheets_service = sheets_api.build_service()
    body = {'requests': requests}
    sheets_service.spreadsheets() \
        .batchUpdate(
            spreadsheetId=spreadsheet_id,
            body=body) \
        .execute()


def get_values(spreadsheet_id: str, range_: str) -> List[List[Any]]:
    """
    Query spreadsheet from provided range and return its values.
    """
    sheets_service = sheets_api.build_service()
    result = sheets_service.spreadsheets() \
        .values() \
        .get(
            spreadsheetId=spreadsheet_id,
            range=range_) \
        .execute()
    return result.get('values', [])


def update_values(spreadsheet_id: str, range_: str, values: List[List[Any]]) -> None:
    """
    Update range with given values.
    """
    sheets_service = sheets_api.build_service()
    body = {'values': values}
    sheets_service.spreadsheets() \
        .values() \
        .update(
            spreadsheetId=spreadsheet_id,
            range=range_,
            valueInputOption='USER_ENTERED',
            body=body) \
        .execute()
