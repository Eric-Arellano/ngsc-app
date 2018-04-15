from backend.src.sheets_commands import sheet


def append_blank(*,
                 all_cells: sheet.Grid,
                 num_rows: int,
                 num_columns: int) -> sheet.Grid:
    """
    Append blank rows.
    """
    new_rows = [[''] * num_columns] * num_rows
    return all_cells + new_rows
