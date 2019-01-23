from typing import Dict, Union, Optional

GridRange = Dict[str, int]
DimensionRange = Dict[str, Union[int, str]]


def grid(
    *,
    row_start_index: Optional[int] = None,
    row_end_index: Optional[int] = None,
    column_start_index: Optional[int] = None,
    column_end_index: Optional[int] = None,
    tab_id: int = 0,
) -> GridRange:
    """
    Create GridRange object.
    """
    range_ = {"sheetId": tab_id}

    if row_start_index:
        range_["startRowIndex"] = row_start_index
    if row_end_index:
        range_["endRowIndex"] = row_end_index
    if column_start_index:
        range_["startColumnIndex"] = column_start_index
    if column_end_index:
        range_["endColumnIndex"] = column_end_index
    return range_


def column(
    *,
    start_index: Optional[int] = None,
    end_index: Optional[int] = None,
    tab_id: int = 0,
) -> DimensionRange:
    """
    Create DimensionRange object for column.
    """
    range_: DimensionRange = {"sheetId": tab_id, "dimension": "COLUMNS"}
    if start_index:
        range_["startIndex"] = start_index
    if end_index:
        range_["endIndex"] = end_index
    return range_
