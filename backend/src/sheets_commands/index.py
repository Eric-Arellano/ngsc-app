import string
from typing import Optional

from backend.src.sheets_commands import sheet


def get_numeric(spreadsheet_id: sheet.ID, column_name: str) -> Optional[int]:
    """
    Searches for given column name and returns list index, e.g. '0' or '3'.
    """
    columns = sheet.get_values(spreadsheet_id, 'A1:1')
    flattened_column_names = [name for cols in columns for name in cols]
    try:
        column_index = flattened_column_names.index(column_name)
    except ValueError:
        return None
    else:
        return column_index


def get_letter(spreadsheet_id: sheet.ID, column_name: str) -> Optional[str]:
    """
    Searches for given column name and returns Google Sheet index, e.g. 'A' or 'C'.
    """
    numeric_index = get_numeric(spreadsheet_id, column_name)
    if numeric_index is None:
        return None
    number_to_upper = {num: upper for num, upper in enumerate(string.ascii_uppercase, 0)}
    return number_to_upper.get(numeric_index)
