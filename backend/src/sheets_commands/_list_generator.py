from typing import Any, Dict, List


def select_columns(*,
                   all_cells: List[List[Any]],
                   target_indexes: List[int]) -> List[List[Any]]:
    """
    Given all cells, return only the specified columns. Zero-indexed.
    """
    return [[cell for col_index, cell in enumerate(row)
             if col_index in target_indexes]
            for row in all_cells]


def filter_by_cell(*,
                   all_cells: List[List[Any]],
                   target_index: int,
                   target_value: str) -> List[List[Any]]:
    """
    Filter out rows without the target value for specified column. Does not modify rows.
    """
    return [row for row in all_cells
            if len(row) > target_index and row[target_index] == target_value]


def update_column(*,
                  updated_values: Dict[str, str],
                  all_cells: List[List[Any]],
                  key_index: int,
                  target_index: int,
                  overwrite: bool) -> List[List[Any]]:
    """
    Generate an updated list for the entire column, optionally overwriting values. Zero-indexed.
    """
    if overwrite:
        return [[updated_values.get(row[key_index], row[key_index])]  # if nothing found in dict, keep original value
                for row in all_cells]
    else:
        return [[updated_values.get(row[key_index])
                 if len(row) < target_index or not row[target_index]  # only check if missing
                 else row[target_index]]  # else use original
                for row in all_cells]
