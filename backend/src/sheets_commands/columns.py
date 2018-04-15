from typing import Dict, List

from backend.src.sheets_commands import sheet


def select(*,
           all_cells: sheet.Grid,
           target_indexes: List[int]) -> sheet.Grid:
    """
    Given all cells, return only the specified columns.
    """
    return [[cell for col_index, cell in enumerate(row)
             if col_index in target_indexes]
            for row in all_cells]


def remove(*,
           all_cells: sheet.Grid,
           target_indexes: List[int]) -> sheet.Grid:
    """
    Remove columns from cells.
    """
    return [[cell for col_index, cell in enumerate(row)
             if col_index not in target_indexes]
            for row in all_cells]


def add(*,
        all_cells: sheet.Grid,
        column: sheet.Column,
        target_index: int) -> sheet.Grid:
    """
    Add the provided column at specified index.
    """
    return [row[:target_index] + [column[row_index]] + row[target_index:]
            for row_index, row in enumerate(all_cells)]


def add_blank(*,
              all_cells: sheet.Grid,
              target_index: int) -> sheet.Grid:
    """
    Add blank column at specified index.
    """
    return [row[:target_index] + [""] + row[target_index:]
            for row in all_cells]


def reorder(*,
            all_cells: sheet.Grid,
            new_order: List[int]) -> sheet.Grid:
    """
    Reorder to the specified order.
    """
    return [[row[index] for index in new_order]
            for row in all_cells]


def filter_by_cell(*,
                   all_cells: sheet.Grid,
                   target_index: int,
                   target_value: sheet.Cell) -> sheet.Grid:
    """
    Filter out rows without the target value for specified column. Does not modify rows.
    """
    return [row for row in all_cells
            if len(row) > target_index and row[target_index] == target_value]


def update(*,
           updated_values: Dict[str, str],
           all_cells: sheet.Grid,
           key_index: int,
           target_index: int,
           overwrite: bool) -> sheet.Grid:
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

