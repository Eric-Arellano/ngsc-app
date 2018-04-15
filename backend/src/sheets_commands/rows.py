from typing import Any, List


def append_blank(*,
                 all_cells: List[List[Any]],
                 num_rows: int) -> List[List[Any]]:
    """
    Append blank rows.
    """
    new_rows = [[''] * len(all_cells[0])] * num_rows
    return all_cells + new_rows
