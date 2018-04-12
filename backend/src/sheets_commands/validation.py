from typing import List

from backend.src.sheets_commands import sheet


def dropdown_options(*,
                     spreadsheet_id: str,
                     options: List[str],
                     row_start_index: int,
                     row_end_index: int,
                     column_start_index: int,
                     column_end_index: int) -> None:
    """
    Add dropdown data validation - must be a member of the list.
    """
    sheet_id = '0'
    mapped_options = [{"userEnteredValue": option} for option in options]
    requests = [{
        'setDataValidation': {
            'range': {
                'sheetId': sheet_id,
                'startRowIndex': row_start_index,
                'endRowIndex': row_end_index,
                'startColumnIndex': column_start_index,
                'endColumnIndex': column_end_index,
            },
            'rule': {
                'condition': {
                    'type': 'ONE_OF_LIST',
                    'values': mapped_options
                },
                'showCustomUi': True
            },
        }}]
    sheet.batch_update(spreadsheet_id, requests)
