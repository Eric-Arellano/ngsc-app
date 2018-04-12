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
            'range': {
                'sheetId': sheet_id,
                'dimension': 'COLUMNS',
                'startIndex': start_index,
                'endIndex': end_index,
            },
            'properties': {
                'hiddenByUser': hidden,
            },
            'fields': 'hiddenByUser',
        }}]
    sheet.batch_update(spreadsheet_id, requests)


def freeze(spreadsheet_id: str, *,
           num_rows: int = 0,
           num_columns: int = 0) -> None:
    """
    Freeze rows and column from the leftmost corner outwards.
    """
    sheet_id = '0'
    requests = [{
        'updateSheetProperties': {
            'properties': {
                'sheetId': sheet_id,
                'gridProperties': {
                    'frozenRowCount': num_rows,
                    'frozenColumnCount': num_columns
                }
            },
            'fields': 'gridProperties(frozenRowCount, frozenColumnCount)'
        }}]
    sheet.batch_update(spreadsheet_id, requests)


def auto_resize(spreadsheet_id: str, *,
                start_index: int = 0,
                end_index: int = 20) -> None:
    """
    Automatically resize columns to their largest value.
    """
    sheet_id = '0'
    requests = [{
        'autoResizeDimensions': {
            'dimensions': {
                'sheetId': sheet_id,
                'dimension': 'COLUMNS',
                'startIndex': start_index,
                'endIndex': end_index,
            }
        }}]
    sheet.batch_update(spreadsheet_id, requests)


def alternating_colors(spreadsheet_id: str) -> None:
    """
    Add alternating colors, with special header coloring.
    """
    sheet_id = '0'
    requests = [{
        'addBanding': {
            'bandedRange': {
                'bandedRangeId': 1,
                'range': {
                    'sheetId': sheet_id
                },
                'rowProperties': {
                    'headerColor': {
                        'red': 189 / 255.0,
                        'green': 189 / 255.0,
                        'blue': 189 / 255.0,
                        'alpha': .2
                    },
                    'firstBandColor': {
                        'red': 255 / 255.0,
                        'green': 255 / 255.0,
                        'blue': 255 / 255.0,
                        'alpha': 0
                    },
                    'secondBandColor': {
                        'red': 243 / 255.0,
                        'green': 243 / 255.0,
                        'blue': 243 / 255.0,
                        'alpha': .07
                    }
                }
            }
        }}]
    sheet.batch_update(spreadsheet_id, requests)
