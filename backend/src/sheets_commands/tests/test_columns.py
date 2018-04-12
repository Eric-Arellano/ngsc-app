import pytest

from backend.src.sheets_commands import columns


# --------------------------------------------------------------------
# Select column(s)
# --------------------------------------------------------------------

def test_select():
    original_cells = [
        ['Eric', 'Arellano', '1'],
        ['Sami', 'Mooney', '2'],
        ['Diana', 'Chen', '3']
    ]
    selected = columns.select(all_cells=original_cells,
                              target_indexes=[0, 2])
    assert selected == [
        ['Eric', '1'],
        ['Sami', '2'],
        ['Diana', '3']
    ]


def test_select_with_missing_cells():
    original_cells = [
        ['Eric', 'Arellano', '1'],
        ['Sami'],
        ['Diana', '', '3']
    ]
    selected = columns.select(all_cells=original_cells,
                              target_indexes=[0, 2])
    assert selected == [
        ['Eric', '1'],
        ['Sami'],
        ['Diana', '3']
    ]


# --------------------------------------------------------------------
# Remove columns
# --------------------------------------------------------------------

def test_remove():
    original_cells = [
        ['Eric', '1'],
        ['Sami', '2'],
    ]
    selected = columns.remove(all_cells=original_cells,
                              target_indexes=[1])
    assert selected == [
        ['Eric'],
        ['Sami'],
    ]


# --------------------------------------------------------------------
# Add blank columns
# --------------------------------------------------------------------

def test_add_blank():
    original_cells = [
        ['Eric', '1'],
        ['Sami', '2'],
    ]
    selected = columns.add_blank(all_cells=original_cells,
                                 target_index=0)
    assert selected == [
        ['', 'Eric', '1'],
        ['', 'Sami', '2'],
    ]


# --------------------------------------------------------------------
# Reorder columns
# --------------------------------------------------------------------

def test_reorder():
    original_cells = [
        ['Eric', '1'],
        ['Sami', '2'],
    ]
    selected = columns.reorder(all_cells=original_cells,
                               new_order=[1, 0])
    assert selected == [
        ['1', 'Eric'],
        ['2', 'Sami'],
    ]


# --------------------------------------------------------------------
# Filter
# --------------------------------------------------------------------

def test_filter():
    original_cells = [
        ['Eric', '1'],
        ['Sami', '2'],
        ['Diana', '2'],
        ['Raul', '3']
    ]
    filtered = columns.filter_by_cell(all_cells=original_cells,
                                      target_index=1,
                                      target_value='2')
    assert filtered == [
        ['Sami', '2'],
        ['Diana', '2'],
    ]


def test_filter_with_missing_cells():
    original_cells = [
        ['Eric', '1'],
        ['Sami'],
        ['Diana', '2'],
    ]
    filtered = columns.filter_by_cell(all_cells=original_cells,
                                      target_index=1,
                                      target_value='2')
    assert filtered == [
        ['Diana', '2'],
    ]


# --------------------------------------------------------------------
# Update column
# --------------------------------------------------------------------

@pytest.fixture
def mock_updated_values():
    id_to_new_values = {
        'ecarell1': '13',
        'ecka13': '44'
    }
    return id_to_new_values


def test_update_with_overwrite(mock_updated_values):
    original_cells = [
        ['ecarell1', ''],
        ['ecka13', ''],
        ['ecka13', '99']
    ]
    updated_values = columns.update(updated_values=mock_updated_values,
                                    all_cells=original_cells,
                                    key_index=0,
                                    target_index=1,
                                    overwrite=True)
    assert updated_values == [
        ['13'],
        ['44'],
        ['44']
    ]


def test_update_without_overwrite(mock_updated_values):
    original_cells = [
        ['ecarell1', ''],
        ['ecka13', ''],
        ['ecka13', '99']
    ]
    updated_values = columns.update(updated_values=mock_updated_values,
                                    all_cells=original_cells,
                                    key_index=0,
                                    target_index=1,
                                    overwrite=False)
    assert updated_values == [
        ['13'],
        ['44'],
        ['99']
    ]


@pytest.mark.skip('Not yet implemented')
def test_update_empty_lists(mock_updated_values):
    original_cells = [
        ['ecarell1'],
        [''],
        ['', '']
    ]
    updated_values_with_overwrite = columns.update(updated_values=mock_updated_values,
                                                   all_cells=original_cells,
                                                   key_index=0,
                                                   target_index=1,
                                                   overwrite=True)
    updated_values_without_overwrite = columns.update(updated_values=mock_updated_values,
                                                      all_cells=original_cells,
                                                      key_index=0,
                                                      target_index=1,
                                                      overwrite=False)
    assert updated_values_with_overwrite == updated_values_without_overwrite == [
        ['13'],
        [],
        []
    ]


def test_update_additional_data(mock_updated_values):
    original_cells = [
        ['ecarell1', '', 'e'],
        ['ecka13', '', 'e']
    ]
    updated_values_with_overwrite = columns.update(updated_values=mock_updated_values,
                                                   all_cells=original_cells,
                                                   key_index=0,
                                                   target_index=1,
                                                   overwrite=True)
    updated_values_without_overwrite = columns.update(updated_values=mock_updated_values,
                                                      all_cells=original_cells,
                                                      key_index=0,
                                                      target_index=1,
                                                      overwrite=False)
    assert updated_values_with_overwrite == updated_values_without_overwrite == [
        ['13'],
        ['44']
    ]
