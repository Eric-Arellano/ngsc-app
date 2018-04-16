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
    original_grid = [
        ['Eric', '1'],
        ['Sami', '2'],
    ]
    result = rows.append_blank(grid=original_grid,
                               num_rows=2,
                               num_columns=2)
    assert result == [
        ['Eric', '1'],
        ['Sami', '2'],
        ['', ''],
        ['', ''],
    ]


def test_add_blank_to_empty():
    original_grid = [[]]
    result = rows.append_blank(grid=original_grid,
                               num_rows=2,
                               num_columns=2)
    assert result == [
        [],
        ['', ''],
        ['', ''],
    ]


# --------------------------------------------------------------------
# Filter
# --------------------------------------------------------------------


def test_filter():
    original_grid = [
        ['Eric', '1'],
        ['Sami', '2'],
        ['Diana', '2'],
        ['Raul', '3']
    ]
    result = rows.filter_by_cell(grid=original_grid,
                                 target_index=1,
                                 target_value='2')
    assert result == [
        ['Sami', '2'],
        ['Diana', '2'],
    ]


def test_filter_with_missing_cells():
    original_grid = [
        ['Eric', '1'],
        ['Sami'],
        ['Diana', '2'],
    ]
    result = rows.filter_by_cell(grid=original_grid,
                                 target_index=1,
                                 target_value='2')
    assert result == [
        ['Diana', '2'],
    ]
