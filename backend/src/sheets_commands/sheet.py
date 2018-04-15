from typing import Any, Dict, List

from backend.src.google_apis import sheets_api

BatchRequest = Dict[str, Any]


def batch_update(spreadsheet_id: str, requests: List[BatchRequest]) -> None:
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


def update_values(spreadsheet_id: str, *,
                  range_: str,
                  values: List[List[Any]],
                  raw: bool = False) -> None:
    """
    Update range with given values.
    """
    input_mode = 'RAW' if raw else 'USER_ENTERED'
    sheets_service = sheets_api.build_service()
    body = {'values': values}
    sheets_service.spreadsheets() \
        .values() \
        .update(
            spreadsheetId=spreadsheet_id,
            range=range_,
            valueInputOption=input_mode,
            body=body) \
        .execute()
