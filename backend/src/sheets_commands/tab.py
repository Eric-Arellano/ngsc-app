from backend.src.sheets_commands import sheet


# ---------------------------------------------------------------------
# Commands (immediate execution)
# ---------------------------------------------------------------------

def rename(*,
           spreadsheet_id: sheet.ID,
           tab_name: str,
           tab_id: int = 0) -> None:
    """
    Rename specified tab.
    """
    request = rename_request(tab_name=tab_name,
                             tab_id=tab_id)
    sheet.batch_update(spreadsheet_id, [request])


# ---------------------------------------------------------------------
# Generate requests (allows delaying execution)
# ---------------------------------------------------------------------

def rename_request(*,
                   tab_name: str,
                   tab_id: int = 0) -> sheet.BatchRequest:
    """
    Rename specified tab.
    """
    return {
        'updateSheetProperties': {
            'properties': {
                'sheetId': tab_id,
                'title': tab_name
            },
            'fields': 'title'
        }}
