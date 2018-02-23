from backend.src.google_apis import sheets_api
from backend.src.sheets_commands import _environment_chooser


def hide_all_ids() -> None:
    """
    Hide the student ID column from all rosters.
    """
    _environment_chooser.operate_on_all_attendance(hide_values,
                                                   start_index=0,
                                                   end_index=1)


# ------------------------------------------------------
# Generic commands
# ------------------------------------------------------

def hide_values(spreadsheet_id: str, start_index, end_index) -> None:
    """
    Hide the columns for provided column range.
    """
    sheet_id = '0'
    requests = [{
        'updateDimensionProperties': {
            "range": {
                "sheetId": sheet_id,
                "dimension": 'COLUMNS',
                "startIndex": start_index,
                "endIndex": end_index,
            },
            "properties": {
                "hiddenByUser": True,
            },
            "fields": 'hiddenByUser',
        }}]
    sheets_api.batch_update(spreadsheet_id, requests)
