from backend.src.sheets_commands import rows


# --------------------------------------------------------------------
# Append columns
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
