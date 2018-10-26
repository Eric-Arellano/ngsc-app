from typing import List
from enum import Enum


class Residency(Enum):
    RESIDENT = "resident"
    NON_RESIDENT = "non_resident"
    NON_RESIDENT_WUE = "non_resident_wue"
    INTERNATIONAL = "international"


TUITION = {
    Residency.RESIDENT: 9834,
    Residency.NON_RESIDENT: 26824,
    Residency.NON_RESIDENT_WUE: 14526,
    Residency.INTERNATIONAL: 28824,
}

LIVING_STIPEND = 2500


def calculate_award(
    residency_status: Residency, scholarship_amounts: List[float]
) -> float:
    tuition = TUITION[residency_status]
    total_scholarships = sum(scholarship_amounts)
    return max(tuition + LIVING_STIPEND - total_scholarships, 0)
