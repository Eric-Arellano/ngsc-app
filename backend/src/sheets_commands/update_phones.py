from typing import Dict

from backend.src.google_apis import sheets_api


def update_all_phone_numbers() -> None:
    """
    Attempt to add missing phone numbers to roster.

    Do not modify if phone already exists.
    """
    spreadsheet = '1omms6ldwSZWgDXRf2HYDtGoCwzekfuSt7OAA8yVyRwY'
    demographics = {'ecarell1': '925858', 'ecka13': '111'}
    update_roster_phone_numbers(spreadsheet_id=spreadsheet,
                                demographics=demographics)


def update_roster_phone_numbers(spreadsheet_id: str, *,
                                demographics: Dict[str, str]) -> None:
    """
    Update roster's phone numbers if missing.
    """
    column_index = sheets_api.get_column_numeric_index(spreadsheet_id, 'phone')
    column_letter = sheets_api.get_column_letter_index(spreadsheet_id, 'phone')
    if column_index is not None:
        all_data = sheets_api.get_values(spreadsheet_id, f'A2:50')
        updated_phones = [[demographics.get(row[0])  # check phone for given asurite
                           if len(row) < column_index or not row[column_index]  # only check if phone is missing
                           else row[column_index]]  # else return original phone
                          for row in all_data]
        sheets_api.update_values(spreadsheet_id, f'{column_letter}2:{column_letter}', updated_phones)
