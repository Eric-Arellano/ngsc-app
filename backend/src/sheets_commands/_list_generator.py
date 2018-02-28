from typing import Any, Dict, List


def update_column(*,
                  updated_values: Dict[str, str],
                  all_cells: List[List[Any]],
                  key_index: int,
                  target_index: int,
                  overwrite: bool) -> List[List[Any]]:
    """
    Generate an updated list for the entire column, optionally overwriting values.
    """
    if overwrite:
        return [[updated_values.get(row[key_index], row[key_index])]  # if nothing found in dict, keep original value
                for row in all_cells]
    else:
        return [[updated_values.get(row[key_index])
                 if len(row) < target_index or not row[target_index]  # only check if missing
                 else row[target_index]]  # else use original
                for row in all_cells]
