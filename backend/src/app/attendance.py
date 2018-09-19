"""
Queries for student's attendance.
"""

from typing import Dict, Optional

from backend.src.data import column_indexes, file_ids
from backend.src.sheets_commands import sheet


def get(asurite: str) -> Optional[Dict]:
    """
    Get student's mission team, committee, OLS, and no show attendance.
    """
    all_rows = sheet.get_values(file_ids.master, range_="Master!A2:T")
    row = next(
        (row for row in all_rows if row[column_indexes.master["asurite"]] == asurite),
        None,
    )
    if row is None:
        return None
    return {
        "noShows": str(row[column_indexes.master["no_shows"]]),
        "missionTeamAttendance": str(row[column_indexes.master["mt_attendance"]]),
        "committeeAttendance": str(row[column_indexes.master["committee_attendance"]]),
        "olsAttendance": str(row[column_indexes.master["ols"]]),
    }
