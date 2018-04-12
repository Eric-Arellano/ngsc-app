import backend.src.sheets_commands.sheet


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
    backend.src.sheets_commands.sheet.batch_update(spreadsheet_id, requests)
