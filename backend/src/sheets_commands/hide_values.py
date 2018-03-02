from backend.src.google_apis import sheets_api
from backend.src.sheets_commands import _environment_chooser


def hide_all_ids() -> None:
    """
    Hide the student ID column from all rosters.
    """
    _environment_chooser.operate_on_all_attendance(toggle_hiding_columns,
                                                   start_index=0,
                                                   end_index=1,
                                                   hidden=True)


# ------------------------------------------------------
# Generic commands
# ------------------------------------------------------

def toggle_hiding_columns(spreadsheet_id: str, *,
                          start_index: int,
                          end_index: int,
                          hidden: bool) -> None:
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
                "hiddenByUser": hidden,
            },
            "fields": 'hiddenByUser',
        }}]
    sheets_api.batch_update(spreadsheet_id, requests)
