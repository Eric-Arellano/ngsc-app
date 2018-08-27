from typing import Dict

from backend.src.admin import _environment_chooser
from backend.src.data import column_indexes, file_ids
from backend.src.sheets_commands import columns, display, index, sheet


# --------------------------------------------------------------
# Hide IDs
# --------------------------------------------------------------

def hide_all_ids() -> None:
    """
    Hide the student ID column from all rosters.
    """
    _environment_chooser.operate_on_all_attendance(display.hide_columns,
                                                   start_index=0,
                                                   end_index=1)


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
    phone_column_index = index.get_numeric(spreadsheet_id, column_name='phone')
    phone_column_letter = index.get_letter(spreadsheet_id, column_name='phone')
    if phone_column_index is None:
        return
    range_ = f'A2:{phone_column_letter}'
    grid = sheet.get_values(spreadsheet_id, range_=range_)
    updated_phones = columns.update(updated_values=asurite_to_phones,
                                    grid=grid,
                                    key_index=0,
                                    target_index=phone_column_index,
                                    overwrite=overwrite)
    sheet.update_values(spreadsheet_id,
                        range_=range_,
                        grid=updated_phones)


# --------------------------------------------------------------
# IDs -> ASUrite
# --------------------------------------------------------------

def convert_all_ids_to_asurite() -> None:
    """
    Goes through every roster and updates each ID cell with accompanying ASUrite.
    """
    spreadsheet = '1omms6ldwSZWgDXRf2HYDtGoCwzekfuSt7OAA8yVyRwY'  # TODO(asurite): remove and use operate_on_all()
    values = sheet.get_values(file_ids.master, range_='Master!A2:D')
    id_to_asurite = {v[column_indexes.master['id']]: v[column_indexes.master['asurite']]
                     for v in values}
    convert_roster_ids_to_asurite(spreadsheet, id_to_asurite=id_to_asurite)
    # _environment_chooser.operate_on_all_attendance(convert_roster_ids_to_asurite,
    #                                                id_to_asurite=id_to_asurite)


def convert_roster_ids_to_asurite(spreadsheet_id: str, *,
                                  id_to_asurite: Dict[str, str]) -> None:
    """
    Converts IDs to ASUrite for given roster.
    """
    range_ = 'A2:A'
    grid = sheet.get_values(spreadsheet_id, range_=range_)
    asurites = columns.update(updated_values=id_to_asurite,
                              grid=grid,
                              key_index=0,
                              target_index=0,
                              overwrite=True)
    sheet.update_values(spreadsheet_id, range_=range_, grid=asurites)
