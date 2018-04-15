from backend.src.sheets_commands import rows


# --------------------------------------------------------------------
# Select rows
# --------------------------------------------------------------------

def test_select():
    original_grid = [
        ['Eric', '1'],
        ['Sami', '2'],
        ['Danny', '3'],
    ]
    result = rows.select(grid=original_grid,
                         target_indexes=[0, 2])
    assert result == [
        ['Eric', '1'],
        ['Danny', '3'],
    ]


# --------------------------------------------------------------------
# Remove rows
# --------------------------------------------------------------------

def test_remove():
    original_grid = [
        ['Eric', '1'],
        ['Sami', '2'],
        ['Danny', '3'],
    ]
    result = rows.remove(grid=original_grid,
                         target_indexes=[0, 2])
    assert result == [
        ['Sami', '2'],
    ]


# --------------------------------------------------------------------
# Append rows
# --------------------------------------------------------------------

def test_add_blank():
    original_cells = [
        ['Eric', '1'],
        ['Sami', '2'],
    ]
    result = rows.append_blank(all_cells=original_cells,
                               num_rows=2,
                               num_columns=2)
    assert result == [
        ['Eric', '1'],
        ['Sami', '2'],
        ['', ''],
        ['', ''],
    ]


def test_add_blank_to_empty():
    original_cells = [[]]
    result = rows.append_blank(all_cells=original_cells,
                               num_rows=2,
                               num_columns=2)
    assert result == [
        [],
        ['', ''],
        ['', ''],
    ]
