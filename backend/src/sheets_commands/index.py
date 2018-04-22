import string
from typing import Optional

from googleapiclient import discovery

from backend.src.sheets_commands import sheet


def get_numeric(spreadsheet_id: sheet.ID, *,
                column_name: str,
                sheets_service: discovery.Resource = None) -> Optional[int]:
    """
    Searches for given column name and returns list index, e.g. '0' or '3'.
    """
    columns = sheet.get_values(spreadsheet_id,
                               range_='A1:1',
                               sheets_service=sheets_service)
    flattened_column_names = [name for cols in columns for name in cols]
    try:
        column_index = flattened_column_names.index(column_name)
    except ValueError:
        return None
    else:
        return column_index


def get_letter(spreadsheet_id: sheet.ID, *,
               column_name: str,
               sheets_service: discovery.Resource = None) -> Optional[str]:
    """
    Searches for given column name and returns Google Sheet index, e.g. 'A' or 'C'.
    """
    numeric_index = get_numeric(spreadsheet_id,
                                column_name=column_name,
                                sheets_service=sheets_service)
    if numeric_index is None:
        return None
    number_to_upper = {num: upper for num, upper in enumerate(string.ascii_uppercase, 0)}
    return number_to_upper.get(numeric_index)
