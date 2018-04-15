from backend.src.sheets_commands import sheet


# ---------------------------------------------------------------------
# Commands (immediate execution)
# ---------------------------------------------------------------------

def hide_columns(spreadsheet_id: str, *,
                 start_index: int,
                 end_index: int,
                 hidden: bool = True,
                 sheet_id: str = '0') -> None:
    """
    Hide the columns for provided column range.
    """
    request = hide_columns_request(start_index=start_index, end_index=end_index, hidden=hidden, sheet_id=sheet_id)
    sheet.batch_update(spreadsheet_id, [request])


def freeze(spreadsheet_id: str, *,
           num_rows: int = 0,
           num_columns: int = 0,
           sheet_id: str = '0') -> None:
    """
    Freeze rows and column from the leftmost corner outwards.
    """
    request = freeze_request(num_rows=num_rows, num_columns=num_columns, sheet_id=sheet_id)
    sheet.batch_update(spreadsheet_id, [request])


def auto_resize(spreadsheet_id: str, *,
                start_index: int = 0,
                end_index: int = 20,
                sheet_id: str = '0') -> None:
    """
    Automatically resize columns to their largest value.
    """
    request = auto_resize_request(start_index=start_index, end_index=end_index, sheet_id=sheet_id)
    sheet.batch_update(spreadsheet_id, [request])


def alternating_colors(spreadsheet_id: str,
                       sheet_id: str = '0') -> None:
    """
    Add alternating colors, with special header coloring.
    """
    request = alternating_colors_request(sheet_id=sheet_id)
    sheet.batch_update(spreadsheet_id, [request])


# ---------------------------------------------------------------------
# Generate requests (allows delaying execution)
# ---------------------------------------------------------------------

def hide_columns_request(*,
                         start_index: int,
                         end_index: int,
                         hidden: bool = True,
                         sheet_id: str = '0') -> sheet.BatchRequest:
    """
    Hide the columns for provided column range.
    """
    return {
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
        }}


def freeze_request(*,
                   num_rows: int = 0,
                   num_columns: int = 0,
                   sheet_id: str = '0') -> sheet.BatchRequest:
    """
    Freeze rows and column from the leftmost corner outwards.
    """
    return {
        'updateSheetProperties': {
            'properties': {
                'sheetId': sheet_id,
                'gridProperties': {
                    'frozenRowCount': num_rows,
                    'frozenColumnCount': num_columns
                }
            },
            'fields': 'gridProperties(frozenRowCount, frozenColumnCount)'
        }}


def auto_resize_request(*,
                        start_index: int = 0,
                        end_index: int = 20,
                        sheet_id: str = '0') -> sheet.BatchRequest:
    """
    Automatically resize columns to their largest value.
    """
    return {
        'autoResizeDimensions': {
            'dimensions': {
                'sheetId': sheet_id,
                'dimension': 'COLUMNS',
                'startIndex': start_index,
                'endIndex': end_index,
            }
        }}


def alternating_colors_request(*, sheet_id: str = '0') -> sheet.BatchRequest:
    """
    Add alternating colors, with special header coloring.
    """
    return {
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
        }}
