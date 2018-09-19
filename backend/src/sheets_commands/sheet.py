from typing import Any, Dict, List, Union

from googleapiclient import discovery

from backend.src.google_apis import sheets_api

# --------------------------------------------------------
# Data structures
# --------------------------------------------------------

ID = str
Range = str

BatchRequest = Dict[str, Any]

Cell = Union[str, int, float]
Row = List[Cell]
Column = List[Cell]
Grid = List[Column]  # nested list of rows, each made up of column cells


# --------------------------------------------------------
# Core functions
# --------------------------------------------------------


def batch_update(
    spreadsheet_id: ID,
    *,
    requests: List[BatchRequest],
    sheets_service: discovery.Resource = None,
) -> None:
    """
    Perform an operation on the spreadsheet.
    """
    if sheets_service is None:
        sheets_service = sheets_api.build_service()
    body = {"requests": requests}
    sheets_service.spreadsheets().batchUpdate(
        spreadsheetId=spreadsheet_id, body=body
    ).execute()


def get_values(
    spreadsheet_id: ID, *, range_: Range, sheets_service: discovery.Resource = None
) -> Grid:
    """
    Query spreadsheet from provided range and return its values.
    """
    if sheets_service is None:
        sheets_service = sheets_api.build_service()
    result = (
        sheets_service.spreadsheets()
        .values()
        .get(spreadsheetId=spreadsheet_id, range=range_)
        .execute()
    )
    return result.get("values", [])


def update_values(
    spreadsheet_id: ID,
    *,
    range_: Range,
    grid: Grid,
    raw: bool = False,
    sheets_service: discovery.Resource = None,
) -> None:
    """
    Update range with given values.
    """
    if sheets_service is None:
        sheets_service = sheets_api.build_service()
    input_mode = "RAW" if raw else "USER_ENTERED"
    body = {"values": grid}
    sheets_service.spreadsheets().values().update(
        spreadsheetId=spreadsheet_id,
        range=range_,
        valueInputOption=input_mode,
        body=body,
    ).execute()


def generate(*, initial_value: str = "", num_rows: int, num_columns: int = 1) -> Grid:
    """
    Generate new grid with the given initial value.
    """
    return [[initial_value] * num_columns] * num_rows
