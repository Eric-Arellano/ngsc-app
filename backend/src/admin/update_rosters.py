from typing import Dict

from backend.src.admin import _environment_chooser
from backend.src.sheets_commands import columns, display, index, sheet


# --------------------------------------------------------------
# Hide IDs
# --------------------------------------------------------------

def hide_all_ids() -> None:
    """
    Hide the student ID column from all rosters.
    """
    _environment_chooser.operate_on_all_attendance(display.toggle_hiding_columns,
                                                   start_index=0,
                                                   end_index=1,
                                                   hidden=True)


# --------------------------------------------------------------
# Update phones
# --------------------------------------------------------------

def update_all_phone_numbers() -> None:
    """
    Attempt to add missing phone numbers to roster.

    Do not modify if phone already exists.
    """
    spreadsheet = '1omms6ldwSZWgDXRf2HYDtGoCwzekfuSt7OAA8yVyRwY'
    asurite_to_phones = {'ecarell1': '925858', 'ecka13': '111'}
    update_roster_phone_numbers(spreadsheet_id=spreadsheet,
                                asurite_to_phones=asurite_to_phones,
                                overwrite=False)


def update_roster_phone_numbers(spreadsheet_id: str, *,
                                asurite_to_phones: Dict[str, str],
                                overwrite: bool = False) -> None:
    """
    Update roster's phone numbers if missing.
    """
    phone_column_index = index.get_numeric(spreadsheet_id, 'phone')
    phone_column_letter = index.get_letter(spreadsheet_id, 'phone')
    if phone_column_index is None:
        return
    all_cells = sheet.get_values(spreadsheet_id, f'A2:{phone_column_letter}')
    updated_phones = columns.update(updated_values=asurite_to_phones,
                                    all_cells=all_cells,
                                    key_index=0,
                                    target_index=phone_column_index,
                                    overwrite=overwrite)
    sheet.update_values(spreadsheet_id, f'{phone_column_letter}2:{phone_column_letter}', updated_phones)


# --------------------------------------------------------------
# IDs -> ASUrite
# --------------------------------------------------------------

def convert_all_ids_to_asurite() -> None:
    """
    Goes through every roster and updates each ID cell with accompanying ASUrite.
    """
    spreadsheet = '1omms6ldwSZWgDXRf2HYDtGoCwzekfuSt7OAA8yVyRwY'
    id_to_asurite = {'1208487250': 'ecarell1', '1210': 'ecka13'}
    convert_roster_ids_to_asurite(spreadsheet, id_to_asurite=id_to_asurite)
    # _environment_chooser.operate_on_all_attendance(convert_roster_ids_to_asurite,
    #                                                id_to_asurite=id_to_asurite)


def convert_roster_ids_to_asurite(spreadsheet_id: str, *,
                                  id_to_asurite: Dict[str, str]) -> None:
    """
    Converts IDs to ASUrite for given roster.
    """
    all_cells = sheet.get_values(spreadsheet_id, 'A2:A')
    asurites = columns.update(updated_values=id_to_asurite,
                              all_cells=all_cells,
                              key_index=0,
                              target_index=0,
                              overwrite=True)
    sheet.update_values(spreadsheet_id, 'A2:A', asurites)
