import pytest

from backend.src.sheets_commands import _list_generator


@pytest.fixture
def dictionary():
    id_to_new_values = {'ecarell1': '13',
                        'ecka13': '44'}
    return id_to_new_values


def test_update_column_with_overwrite(dictionary):
    original_cells = [['ecarell1', ''],
                      ['ecka13', ''],
                      ['ecka13', '99']]
    updated_values = _list_generator.update_column(updated_values=dictionary,
                                                   all_cells=original_cells,
                                                   key_index=0,
                                                   target_index=1,
                                                   overwrite=True)
    assert updated_values == [['13'],
                              ['44'],
                              ['44']]


def test_update_column_without_overwrite(dictionary):
    original_cells = [['ecarell1', ''],
                      ['ecka13', ''],
                      ['ecka13', '99']]
    updated_values = _list_generator.update_column(updated_values=dictionary,
                                                   all_cells=original_cells,
                                                   key_index=0,
                                                   target_index=1,
                                                   overwrite=False)
    assert updated_values == [['13'],
                              ['44'],
                              ['99']]


@pytest.mark.skip('Not yet implemented')
def test_update_column_empty_lists(dictionary):
    original_cells = [['ecarell1'],
                      [''],
                      ['', '']]
    updated_values_with_overwrite = _list_generator.update_column(updated_values=dictionary,
                                                                  all_cells=original_cells,
                                                                  key_index=0,
                                                                  target_index=1,
                                                                  overwrite=True)
    updated_values_without_overwrite = _list_generator.update_column(updated_values=dictionary,
                                                                     all_cells=original_cells,
                                                                     key_index=0,
                                                                     target_index=1,
                                                                     overwrite=False)
    assert updated_values_with_overwrite == updated_values_without_overwrite == [['13'],
                                                                                 [],
                                                                                 []]


def test_update_column_additional_data(dictionary):
    original_cells = [['ecarell1', '', 'e'],
                      ['ecka13', '', 'e']]
    updated_values_with_overwrite = _list_generator.update_column(updated_values=dictionary,
                                                                  all_cells=original_cells,
                                                                  key_index=0,
                                                                  target_index=1,
                                                                  overwrite=True)
    updated_values_without_overwrite = _list_generator.update_column(updated_values=dictionary,
                                                                     all_cells=original_cells,
                                                                     key_index=0,
                                                                     target_index=1,
                                                                     overwrite=False)
    assert updated_values_with_overwrite == updated_values_without_overwrite == [['13'],
                                                                                 ['44']]
