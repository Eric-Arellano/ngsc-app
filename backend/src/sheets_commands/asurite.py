from typing import Dict

from backend.src.google_apis import sheets_api


def convert_all_ids_to_asurite() -> None:
    """
    Goes through every roster and updates each ID cell with accompanying ASUrite.
    """
    spreadsheet = '1omms6ldwSZWgDXRf2HYDtGoCwzekfuSt7OAA8yVyRwY'
    read = sheets_api.get_values(spreadsheet, 'A2:A')
    print(read)
    # sheets_api.update_values(spreadsheet, 'A2', [[12]])  # TODO: authentication error


def convert_roster_ids_to_asurite(spreadsheet_id: str, *,
                                  id_to_asurite: Dict[int, str]) -> None:
    """
    Converts IDs to ASUrite for given roster.
    """
    rows = sheets_api.get_values(spreadsheet_id, 'A2:A')
    asurites = [[id_to_asurite.get(student_id)]
                for row in rows
                for student_id in row]
    # sheets_api.update_values(spreadsheet_id, 'A2:A', asurites)
