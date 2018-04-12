from backend.src.sheets_commands import formulas


def test_formula_adaptive_row_index():
    formula = '=A$:A'
    adaptive_formula = formulas.generate_adaptive_row_index(formula=formula,
                                                            num_rows=3,
                                                            row_index_offset=4)
    assert adaptive_formula == [
        ['=A4:A'],
        ['=A5:A'],
        ['=A6:A']
    ]
