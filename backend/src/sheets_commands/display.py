from typing import Optional

from googleapiclient import discovery

from backend.src.sheets_commands import range, sheet


# ---------------------------------------------------------------------
# Commands (immediate execution)
# ---------------------------------------------------------------------


def hide_columns(
    spreadsheet_id: sheet.ID,
    *,
    hidden: bool = True,
    start_column_index: Optional[int] = None,
    end_column_index: Optional[int] = None,
    tab_id: int = 0,
    sheets_service: Optional[discovery.Resource] = None,
) -> None:
    """
    Hide the columns for provided column range.
    """
    request = hide_columns_request(
        start_column_index=start_column_index,
        end_column_index=end_column_index,
        hidden=hidden,
        tab_id=tab_id,
    )
    sheet.batch_update(
        spreadsheet_id, requests=[request], sheets_service=sheets_service
    )


def freeze(
    spreadsheet_id: sheet.ID,
    *,
    num_rows: int = 0,
    num_columns: int = 0,
    tab_id: int = 0,
    sheets_service: Optional[discovery.Resource] = None,
) -> None:
    """
    Freeze rows and column from the leftmost corner outwards.
    """
    request = freeze_request(num_rows=num_rows, num_columns=num_columns, tab_id=tab_id)
    sheet.batch_update(
        spreadsheet_id, requests=[request], sheets_service=sheets_service
    )


def auto_resize(
    spreadsheet_id: sheet.ID,
    *,
    start_column_index: int = 0,
    end_column_index: int = 20,
    tab_id: int = 0,
    sheets_service: Optional[discovery.Resource] = None,
) -> None:
    """
    Automatically resize columns to their largest value.
    """
    request = auto_resize_request(
        start_column_index=start_column_index,
        end_column_index=end_column_index,
        tab_id=tab_id,
    )
    sheet.batch_update(
        spreadsheet_id, requests=[request], sheets_service=sheets_service
    )


def alternating_colors(
    spreadsheet_id: sheet.ID,
    *,
    row_start_index: Optional[int] = None,
    row_end_index: Optional[int] = None,
    column_start_index: Optional[int] = None,
    column_end_index: Optional[int] = None,
    tab_id: int = 0,
    sheets_service: Optional[discovery.Resource] = None,
) -> None:
    """
    Add alternating colors, with special header coloring.
    """
    request = alternating_colors_request(
        row_start_index=row_start_index,
        row_end_index=row_end_index,
        column_start_index=column_start_index,
        column_end_index=column_end_index,
        tab_id=tab_id,
    )
    sheet.batch_update(
        spreadsheet_id, requests=[request], sheets_service=sheets_service
    )


# ---------------------------------------------------------------------
# Generate requests (allows delaying execution)
# ---------------------------------------------------------------------


def hide_columns_request(
    *,
    start_column_index: Optional[int] = None,
    end_column_index: Optional[int] = None,
    hidden: bool = True,
    tab_id: int = 0,
) -> sheet.BatchRequest:
    """
    Hide the columns for provided column range.
    """
    range_ = range.column(
        start_index=start_column_index, end_index=end_column_index, tab_id=tab_id
    )
    return {
        "updateDimensionProperties": {
            "range": range_,
            "properties": {"hiddenByUser": hidden},
            "fields": "hiddenByUser",
        }
    }


def freeze_request(
    *, num_rows: int = 0, num_columns: int = 0, tab_id: int = 0
) -> sheet.BatchRequest:
    """
    Freeze rows and column from the leftmost corner outwards.
    """
    return {
        "updateSheetProperties": {
            "properties": {
                "sheetId": tab_id,
                "gridProperties": {
                    "frozenRowCount": num_rows,
                    "frozenColumnCount": num_columns,
                },
            },
            "fields": "gridProperties(frozenRowCount, frozenColumnCount)",
        }
    }


def auto_resize_request(
    *, start_column_index: int = 0, end_column_index: int = 20, tab_id: int = 0
) -> sheet.BatchRequest:
    """
    Automatically resize columns to their largest value.
    """
    range_ = range.column(
        start_index=start_column_index, end_index=end_column_index, tab_id=tab_id
    )
    return {"autoResizeDimensions": {"dimensions": range_}}


def alternating_colors_request(
    *,
    row_start_index: Optional[int] = None,
    row_end_index: Optional[int] = None,
    column_start_index: Optional[int] = None,
    column_end_index: Optional[int] = None,
    tab_id: int = 0,
) -> sheet.BatchRequest:
    """
    Add alternating colors, with special header coloring.
    """
    range_ = range.grid(
        row_start_index=row_start_index,
        row_end_index=row_end_index,
        column_start_index=column_start_index,
        column_end_index=column_end_index,
        tab_id=tab_id,
    )
    return {
        "addBanding": {
            "bandedRange": {
                "bandedRangeId": 1,
                "range": range_,
                "rowProperties": {
                    "headerColor": {
                        "red": 189 / 255.0,
                        "green": 189 / 255.0,
                        "blue": 189 / 255.0,
                        "alpha": 0.2,
                    },
                    "firstBandColor": {
                        "red": 255 / 255.0,
                        "green": 255 / 255.0,
                        "blue": 255 / 255.0,
                        "alpha": 0,
                    },
                    "secondBandColor": {
                        "red": 243 / 255.0,
                        "green": 243 / 255.0,
                        "blue": 243 / 255.0,
                        "alpha": 0.07,
                    },
                },
            }
        }
    }
