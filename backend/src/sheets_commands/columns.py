from typing import Dict, List

from backend.src.sheets_commands import sheet


def select(*, grid: sheet.Grid, target_indexes: List[int]) -> sheet.Grid:
    """
    Given all cells, return only the specified columns.
    """
    return [
        [cell for col_index, cell in enumerate(row) if col_index in target_indexes]
        for row in grid
    ]


def remove(*, grid: sheet.Grid, target_indexes: List[int]) -> sheet.Grid:
    """
    Remove columns from cells.
    """
    return [
        [cell for col_index, cell in enumerate(row) if col_index not in target_indexes]
        for row in grid
    ]


def add(*, grid: sheet.Grid, column: sheet.Column, target_index: int) -> sheet.Grid:
    """
    Add the provided column at specified index.
    """
    return [
        row[:target_index] + [column[row_index]] + row[target_index:]
        for row_index, row in enumerate(grid)
    ]


def add_blank(*, grid: sheet.Grid, target_index: int) -> sheet.Grid:
    """
    Add blank column at specified index.
    """
    return [row[:target_index] + [""] + row[target_index:] for row in grid]


def reorder(*, grid: sheet.Grid, new_order: List[int]) -> sheet.Grid:
    """
    Reorder to the specified order.
    """
    return [[row[index] for index in new_order] for row in grid]


def update(
    *,
    grid: sheet.Grid,
    key_index: int,
    target_index: int,
    updated_values: Dict[sheet.Cell, sheet.Cell],
    overwrite: bool,
) -> sheet.Grid:
    """
    Generate an updated list for the entire column, optionally overwriting values.
    """
    if overwrite:
        return [
            [
                updated_values.get(
                    row[key_index], cell
                )  # if nothing found in dict, keep original value
                if col_index == target_index
                else cell
                for col_index, cell in enumerate(row)
            ]
            for row in grid
        ]
    return [
        [
            updated_values.get(
                row[key_index], cell
            )  # if nothing found in dict, keep original value
            if col_index == target_index
            and (
                len(row) < target_index or not row[target_index]
            )  # only check if missing
            else cell  # else use original
            for col_index, cell in enumerate(row)
        ]
        for row in grid
    ]


def replace(*, grid: sheet.Grid, column: sheet.Column, target_index: int) -> sheet.Grid:
    """
    Replace the whole column with provided column.
    """
    return [
        [
            column[row_index]
            if col_index == target_index and row_index < len(column)
            else cell
            for col_index, cell in enumerate(row)
        ]
        for row_index, row in enumerate(grid)
    ]


def batch_replace(
    *, grid: sheet.Grid, columns_with_index: Dict[int, sheet.Column]
) -> sheet.Grid:
    """
    Replace each provided index with its accompanying column.
    """
    return [
        [
            columns_with_index[col_index][row_index]
            if col_index in columns_with_index.keys()
            and row_index < len(columns_with_index[col_index])
            else cell
            for col_index, cell in enumerate(row)
        ]
        for row_index, row in enumerate(grid)
    ]


def clear(*, grid: sheet.Grid, target_indexes: List[int]) -> sheet.Grid:
    """
    Clear all values in the target column.
    """
    return [
        [
            "" if col_index in target_indexes else cell
            for col_index, cell in enumerate(row)
        ]
        for row in grid
    ]


def clear_if(
    *,
    grid: sheet.Grid,
    key_index: int,
    key_values: List[sheet.Cell],
    target_indexes: List[int],
) -> sheet.Grid:
    """
    Clear value in target column if key cell has certain value.
    """
    return [
        [
            "" if col_index in target_indexes and row[key_index] in key_values else cell
            for col_index, cell in enumerate(row)
        ]
        for row in grid
    ]
