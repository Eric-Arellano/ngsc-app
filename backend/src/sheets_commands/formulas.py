from backend.src.sheets_commands import sheet


def generate_adaptive_row_index(*,
                                formula: str,
                                num_rows: int,
                                row_index_offset: int = 2) -> sheet.Column:
    """
    Generate column with the given formula, replacing every `@` with the current row index.
    """
    return [formula.replace('@', str(row_index + row_index_offset))
            for row_index, row in enumerate(range(0, num_rows))]
