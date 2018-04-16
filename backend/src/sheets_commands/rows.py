from typing import List

from backend.src.sheets_commands import sheet


def select(*,
           grid: sheet.Grid,
           target_indexes: List[int]) -> sheet.Grid:
    """
    Given grid, return only the specified rows.
    """
    return [row for row_index, row in enumerate(grid)
            if row_index in target_indexes]


def remove(*,
           grid: sheet.Grid,
           target_indexes: List[int]) -> sheet.Grid:
    """
    Remove target row from grid.
    """
    return [row for row_index, row in enumerate(grid)
            if row_index not in target_indexes]


def append_blank(*,
                 grid: sheet.Grid,
                 num_rows: int,
                 num_columns: int) -> sheet.Grid:
    """
    Append blank rows.
    """
    new_rows = [[''] * num_columns] * num_rows
    return grid + new_rows


def filter_by_cell(*,
                   grid: sheet.Grid,
                   target_index: int,
                   target_value: sheet.Cell) -> sheet.Grid:
    """
    Filter out rows without the target value for specified column. Does not modify rows.
    """
    return [row for row in grid
            if len(row) > target_index and row[target_index] == target_value]
