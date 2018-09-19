import pytest

from backend.src.sheets_commands import columns


# --------------------------------------------------------------------
# Select column(s)
# --------------------------------------------------------------------


def test_select():
    original_grid = [
        ["Eric", "Arellano", "1"],
        ["Sami", "Mooney", "2"],
        ["Diana", "Chen", "3"],
    ]
    result = columns.select(grid=original_grid, target_indexes=[0, 2])
    assert result == [["Eric", "1"], ["Sami", "2"], ["Diana", "3"]]


def test_select_with_missing_cells():
    original_grid = [["Eric", "Arellano", "1"], ["Sami"], ["Diana", "", "3"]]
    result = columns.select(grid=original_grid, target_indexes=[0, 2])
    assert result == [["Eric", "1"], ["Sami"], ["Diana", "3"]]


# --------------------------------------------------------------------
# Remove columns
# --------------------------------------------------------------------


def test_remove():
    original_grid = [["Eric", "1"], ["Sami", "2"]]
    result = columns.remove(grid=original_grid, target_indexes=[1])
    assert result == [["Eric"], ["Sami"]]


# --------------------------------------------------------------------
# Add columns
# --------------------------------------------------------------------


def test_add():
    original_grid = [["Eric", "1"], ["Sami", "2"]]
    new_column = ["A", "B"]
    result = columns.add(grid=original_grid, column=new_column, target_index=1)
    assert result == [["Eric", "A", "1"], ["Sami", "B", "2"]]


def test_add_blank():
    original_grid = [["Eric", "1"], ["Sami", "2"]]
    result = columns.add_blank(grid=original_grid, target_index=0)
    assert result == [["", "Eric", "1"], ["", "Sami", "2"]]


# --------------------------------------------------------------------
# Reorder columns
# --------------------------------------------------------------------


def test_reorder():
    original_grid = [["Eric", "1"], ["Sami", "2"]]
    result = columns.reorder(grid=original_grid, new_order=[1, 0])
    assert result == [["1", "Eric"], ["2", "Sami"]]


# --------------------------------------------------------------------
# Update column
# --------------------------------------------------------------------


@pytest.fixture
def mock_updated_values():
    id_to_new_values = {"ecarell1": "13", "ecka13": "44"}
    return id_to_new_values


def test_update_with_overwrite(mock_updated_values):
    original_grid = [["ecarell1", ""], ["ecka13", ""], ["ecka13", "99"]]
    result = columns.update(
        updated_values=mock_updated_values,
        grid=original_grid,
        key_index=0,
        target_index=1,
        overwrite=True,
    )
    assert result == [["ecarell1", "13"], ["ecka13", "44"], ["ecka13", "44"]]


def test_update_without_overwrite(mock_updated_values):
    original_grid = [["ecarell1", ""], ["ecka13", ""], ["ecka13", "99"]]
    result = columns.update(
        updated_values=mock_updated_values,
        grid=original_grid,
        key_index=0,
        target_index=1,
        overwrite=False,
    )
    assert result == [["ecarell1", "13"], ["ecka13", "44"], ["ecka13", "99"]]


def test_update_empty_grid(mock_updated_values):
    original_grid = [["ecarell1"], [], ["", ""]]
    result_with_overwrite = columns.update(
        updated_values=mock_updated_values,
        grid=original_grid,
        key_index=0,
        target_index=1,
        overwrite=True,
    )
    result_without_overwrite = columns.update(
        updated_values=mock_updated_values,
        grid=original_grid,
        key_index=0,
        target_index=1,
        overwrite=False,
    )
    assert (
        result_with_overwrite
        == result_without_overwrite
        == [["ecarell1"], [], ["", ""]]
    )


def test_update_additional_data(mock_updated_values):
    original_grid = [["ecarell1", "", "e"], ["ecka13", "", "e"]]
    result_with_overwrite = columns.update(
        updated_values=mock_updated_values,
        grid=original_grid,
        key_index=0,
        target_index=1,
        overwrite=True,
    )
    result_without_overwrite = columns.update(
        updated_values=mock_updated_values,
        grid=original_grid,
        key_index=0,
        target_index=1,
        overwrite=False,
    )
    assert (
        result_with_overwrite
        == result_without_overwrite
        == [["ecarell1", "13", "e"], ["ecka13", "44", "e"]]
    )


# --------------------------------------------------------------------
# Replace column
# --------------------------------------------------------------------


def test_replace():
    original_grid = [["ecarell1", ""], ["ecka13", ""], ["ecka13", "99"]]
    result = columns.replace(
        grid=original_grid, target_index=1, column=["n1", "n2", "n3"]
    )
    assert result == [["ecarell1", "n1"], ["ecka13", "n2"], ["ecka13", "n3"]]


def test_replace_longer_column():
    original_grid = [["ecarell1", ""], ["ecka13", ""], ["ecka13", "99"]]
    result = columns.replace(
        grid=original_grid, target_index=1, column=["n1", "n2", "n3", "n4"]
    )
    assert result == [["ecarell1", "n1"], ["ecka13", "n2"], ["ecka13", "n3"]]


def test_replace_shorter_column():
    original_grid = [["ecarell1", ""], ["ecka13", ""], ["ecka13", "99"]]
    result = columns.replace(grid=original_grid, target_index=1, column=["n1", "n2"])
    assert result == [["ecarell1", "n1"], ["ecka13", "n2"], ["ecka13", "99"]]


def test_replace_empty_grid():
    original_grid = [["ecarell1", ""], []]
    result = columns.replace(grid=original_grid, target_index=1, column=["n1", "n2"])
    assert result == [["ecarell1", "n1"], []]


# --------------------------------------------------------------------
# Batch replace column
# --------------------------------------------------------------------


def test_batch_replace():
    original_grid = [
        ["ecarell1", "", "longer"],
        ["ecka13", "", "shorter"],
        ["ecka13", "99", ""],
    ]
    targets = {
        0: ["eric", "diana", "raul"],
        1: ["n1", "n2", "n3"],
        2: ["taller", "wider", "bigger"],
    }
    result = columns.batch_replace(grid=original_grid, columns_with_index=targets)
    assert result == [
        ["eric", "n1", "taller"],
        ["diana", "n2", "wider"],
        ["raul", "n3", "bigger"],
    ]


def test_batch_replace_longer_column():
    original_grid = [["ecarell1", ""], ["ecka13", ""], ["ecka13", "99"]]
    targets = {0: ["eric", "diana", "raul", "nikki"], 1: ["n1", "n2", "n3", "n4"]}
    result = columns.batch_replace(grid=original_grid, columns_with_index=targets)
    assert result == [["eric", "n1"], ["diana", "n2"], ["raul", "n3"]]


def test_batch_replace_shorter_column():
    original_grid = [["ecarell1", ""], ["ecka13", ""], ["ecka13", "99"]]
    targets = {0: ["eric"], 1: ["n1", "n2"]}
    result = columns.batch_replace(grid=original_grid, columns_with_index=targets)
    assert result == [["eric", "n1"], ["ecka13", "n2"], ["ecka13", "99"]]


def test_batch_replace_empty_grid():
    original_grid = [["ecarell1", ""], []]
    targets = {0: ["eric", "diana"], 1: ["n1", "n2"]}
    result = columns.batch_replace(grid=original_grid, columns_with_index=targets)
    assert result == [["eric", "n1"], []]


# --------------------------------------------------------------------
# Clear column
# --------------------------------------------------------------------


def test_clear():
    original_grid = [["ecarell1", "1"], ["ecka13", "2"], ["ecka13", "3"]]
    result = columns.clear(grid=original_grid, target_indexes=[1])
    assert result == [["ecarell1", ""], ["ecka13", ""], ["ecka13", ""]]


def test_clear_if():
    original_grid = [["ecarell1", "1"], ["ecka13", "2"], ["ecka13", "3"]]
    result = columns.clear_if(
        grid=original_grid, target_indexes=[1], key_index=0, key_values=["ecka13"]
    )
    assert result == [["ecarell1", "1"], ["ecka13", ""], ["ecka13", ""]]
