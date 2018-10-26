from backend.src.app import calculator


def test_no_other_scholarships():
    result = calculator.calculate_award(
        residency_status=calculator.Residency.RESIDENT, scholarship_amounts=[]
    )
    assert (
        result
        == calculator.TUITION[calculator.Residency.RESIDENT] + calculator.LIVING_STIPEND
    )


def test_has_other_scholarships():
    result = calculator.calculate_award(
        residency_status=calculator.Residency.RESIDENT, scholarship_amounts=[1000, 500]
    )
    assert (
        result
        == calculator.TUITION[calculator.Residency.RESIDENT]
        + calculator.LIVING_STIPEND
        - 1500
    )


def test_to_many_scholarships():
    result = calculator.calculate_award(
        residency_status=calculator.Residency.RESIDENT,
        scholarship_amounts=[1_000_000_000],
    )
    assert result == 0
