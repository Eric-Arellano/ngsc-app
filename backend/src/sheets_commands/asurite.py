from typing import Dict

from backend.src.google_apis import sheets_api
from backend.src.sheets_commands import _environment_chooser, _list_generator


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
    all_cells = sheets_api.get_values(spreadsheet_id, 'A2:A')
    asurites = _list_generator.update_column(updated_values=id_to_asurite,
                                             all_cells=all_cells,
                                             key_index=0,
                                             target_index=0,
                                             overwrite=True)
    sheets_api.update_values(spreadsheet_id, 'A2:A', asurites)
