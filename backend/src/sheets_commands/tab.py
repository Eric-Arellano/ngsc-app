from typing import Optional

from googleapiclient import discovery

from backend.src.sheets_commands import sheet


# ---------------------------------------------------------------------
# Commands (immediate execution)
# ---------------------------------------------------------------------

def new(*,
        spreadsheet_id: sheet.ID,
        tab_name: str,
        tab_id: Optional[int] = None,
        sheets_service: discovery.Resource = None) -> None:
    """
    Create a new tab with given name.
    """
    request = new_request(tab_name=tab_name, tab_id=tab_id)
    sheet.batch_update(spreadsheet_id,
                       requests=[request],
                       sheets_service=sheets_service)


def rename(*,
           spreadsheet_id: sheet.ID,
           tab_name: str,
           tab_id: int = 0,
           sheets_service: discovery.Resource = None) -> None:
    """
    Rename specified tab.
    """
    request = rename_request(tab_name=tab_name,
                             tab_id=tab_id)
    sheet.batch_update(spreadsheet_id,
                       requests=[request],
                       sheets_service=sheets_service)


# ---------------------------------------------------------------------
# Generate requests (allows delaying execution)
# ---------------------------------------------------------------------

def new_request(*,
                tab_name: str,
                tab_id: Optional[int] = None) -> sheet.BatchRequest:
    """
    Create a new tab with given name.
    """
    request = {
        'addSheet': {
            'properties': {
                'title': tab_name
            },
        }
    }
    if tab_id is not None:
        request['addSheet']['properties']['sheetId'] = tab_id
    return request


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
