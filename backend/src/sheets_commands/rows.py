from backend.src.sheets_commands import sheet


def append_blank(*,
                 all_cells: sheet.Grid,
                 num_rows: int) -> sheet.Grid:
    """
    Append blank rows.
    """
    new_rows = [[''] * len(all_cells[0])] * num_rows
    return all_cells + new_rows
