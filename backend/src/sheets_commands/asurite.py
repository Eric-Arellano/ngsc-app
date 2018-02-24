from typing import Dict

from backend.src.google_apis import sheets_api


def convert_all_ids_to_asurite() -> None:
    """
    Goes through every roster and updates each ID cell with accompanying ASUrite.
    """
    spreadsheet = '1omms6ldwSZWgDXRf2HYDtGoCwzekfuSt7OAA8yVyRwY'
    read = sheets_api.read_cell(spreadsheet, 'A1')
    # sheets_api.update_cell(spreadsheet, 'A2', 12)  # TODO: authentication error


def convert_roster_ids_to_asurite(spreadsheet_id: str, *,
                                  id_to_asurite: Dict[int, str]) -> None:
    """
    Converts IDs to ASUrite for given roster.
    """
    row = 2
    student_id = sheets_api.read_cell(spreadsheet_id, f'A{row}')
    while student_id is not None:
        student_id = sheets_api.read_cell(spreadsheet_id, f'A{row}')
        asurite = id_to_asurite.get(student_id)
        # sheets_api.update_cell(spreadsheet_id, f'A{row}', asurite)
        row += 1
