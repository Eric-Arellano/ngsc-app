from backend.src.sheets_commands import sheet


def hide_columns(spreadsheet_id: str, *,
                 start_index: int,
                 end_index: int,
                 hidden: bool = True) -> None:
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
    sheet.batch_update(spreadsheet_id, requests)


def freeze(spreadsheet_id: str, *, num_rows: int = 0, num_columns: int = 0) -> None:
    sheet_id = '0'
    requests = [{
        'updateSheetProperties': {
            "properties": {
                "sheetId": sheet_id,
                "gridProperties": {
                    "frozenRowCount": num_rows,
                    "frozenColumnCount": num_columns
                }
            },
            'fields': 'gridProperties(frozenRowCount, frozenColumnCount)'
        }}]
    sheet.batch_update(spreadsheet_id, requests)
