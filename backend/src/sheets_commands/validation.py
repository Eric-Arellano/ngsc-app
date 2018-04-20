from typing import List

from backend.src.sheets_commands import sheet


# ---------------------------------------------------------------------
# Commands (immediate execution)
# ---------------------------------------------------------------------

def dropdown_options(*,
                     spreadsheet_id: sheet.ID,
                     options: List[str],
                     row_start_index: int,
                     row_end_index: int,
                     column_start_index: int,
                     column_end_index: int,
                     tab_id: str = '0') -> None:
    """
    Add dropdown data validation - must be a member of the list.
    """
    request = dropdown_options_request(options=options,
                                       row_start_index=row_start_index,
                                       row_end_index=row_end_index,
                                       column_start_index=column_start_index,
                                       column_end_index=column_end_index,
                                       tab_id=tab_id)
    sheet.batch_update(spreadsheet_id, [request])


def protected_range(*,
                    spreadsheet_id: sheet.ID,
                    editor_emails: List[str] = None,
                    warning_only: bool = False,
                    description: str = None,
                    row_start_index: int,
                    row_end_index: int,
                    column_start_index: int,
                    column_end_index: int,
                    tab_id: str = '0') -> None:
    """
    Protect range so only provided users can edit.
    """
    request = protected_range_request(editor_emails=editor_emails,
                                      warning_only=warning_only,
                                      description=description,
                                      row_start_index=row_start_index,
                                      row_end_index=row_end_index,
                                      column_start_index=column_start_index,
                                      column_end_index=column_end_index,
                                      tab_id=tab_id)
    sheet.batch_update(spreadsheet_id, [request])


# ---------------------------------------------------------------------
# Generate requests (allows delaying execution)
# ---------------------------------------------------------------------

def dropdown_options_request(*,
                             options: List[str],
                             row_start_index: int,
                             row_end_index: int,
                             column_start_index: int,
                             column_end_index: int,
                             tab_id: str = '0') -> sheet.BatchRequest:
    """
    Add dropdown data validation - must be a member of the list.
    """
    mapped_options = [{"userEnteredValue": option} for option in options]
    return {
        'setDataValidation': {
            'range': {
                'sheetId': tab_id,
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
        }}


def protected_range_request(*,
                            editor_emails: List[str] = None,
                            warning_only: bool = False,
                            description: str = None,
                            row_start_index: int,
                            row_end_index: int,
                            column_start_index: int,
                            column_end_index: int,
                            tab_id: str = '0') -> sheet.BatchRequest:
    """
    Protect range so only provided users can edit.
    """
    request = {
        'addProtectedRange': {
            'protectedRange': {
                'range': {
                    'sheetId': tab_id,
                    'startRowIndex': row_start_index,
                    'endRowIndex': row_end_index,
                    'startColumnIndex': column_start_index,
                    'endColumnIndex': column_end_index,
                },
                'warningOnly': warning_only,
                'requestingUserCanEdit': True
            }
        }
    }
    if description:
        request['addProtectedRange']['protectedRange']['description'] = description
    if editor_emails:
        request['addProtectedRange']['protectedRange']['editors'] = {
            'users': editor_emails
        }
    return request
