"""
Utilities for interfacing with Google Sheet's API.
"""

from typing import Any, List, Optional
import string

from backend.src.google_apis import authentication


def batch_update(spreadsheet_id: str, requests: List) -> None:
    """
    Perform an operation on the spreadsheet.
    """
    sheets_service = authentication.build_service()
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
    sheets_service = authentication.build_service()
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
    sheets_service = authentication.build_service()
    body = {'values': values}
    sheets_service.spreadsheets() \
        .values() \
        .update(
            spreadsheetId=spreadsheet_id,
            range=range_,
            valueInputOption='USER_ENTERED',
            body=body) \
        .execute()


def get_column_numeric_index(spreadsheet_id: str, column_name: str) -> Optional[int]:
    """
    Searches for given column name and returns list index, e.g. '0' or '3'.
    """
    columns = get_values(spreadsheet_id, 'A1:1')
    flattened_column_names = [name for cols in columns for name in cols]
    try:
        column_index = flattened_column_names.index(column_name)
    except ValueError:
        return None
    else:
        return column_index


def get_column_letter_index(spreadsheet_id: str, column_name: str) -> Optional[str]:
    """
    Searches for given column name and returns Google Sheet index, e.g. 'A' or 'C'.
    """
    numeric_index = get_column_numeric_index(spreadsheet_id, column_name)
    if numeric_index is None:
        return None
    number_to_upper = {num: upper for num, upper in enumerate(string.ascii_uppercase, 0)}
    return number_to_upper.get(numeric_index)
