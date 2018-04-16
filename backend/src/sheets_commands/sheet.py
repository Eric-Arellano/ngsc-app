from typing import Any, Dict, List, Union

from backend.src.google_apis import sheets_api

ID = str
Range = str

BatchRequest = Dict[str, Any]

Cell = Union[str, int, float]
Row = List[Cell]
Column = List[Cell]
Grid = List[Column]  # nested list of rows, each made up of column cells


def batch_update(spreadsheet_id: ID, requests: List[BatchRequest]) -> None:
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


def get_values(spreadsheet_id: ID, range_: Range) -> Grid:
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


def update_values(spreadsheet_id: ID, *,
                  range_: Range,
                  grid: Grid,
                  raw: bool = False) -> None:
    """
    Update range with given values.
    """
    input_mode = 'RAW' if raw else 'USER_ENTERED'
    sheets_service = sheets_api.build_service()
    body = {'values': grid}
    sheets_service.spreadsheets() \
        .values() \
        .update(
            spreadsheetId=spreadsheet_id,
            range=range_,
            valueInputOption=input_mode,
            body=body) \
        .execute()


def generate(*,
             initial_value: str = "",
             num_rows: int,
             num_columns: int = 1) -> Grid:
    """
    Generate new grid with the given initial value.
    """
    return [[initial_value] * num_columns] * num_rows
