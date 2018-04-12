from typing import Any, List


def generate_adaptive_row_index(*,
                                formula: str,
                                num_rows: int,
                                row_index_offset: int = 2) -> List[List[Any]]:
    """
    Generate column with the given formula, replacing every `$` with the current row index.
    """
    return [[formula.replace('$', str(row_index + row_index_offset))]
            for row_index, row in enumerate(range(0, num_rows))]
