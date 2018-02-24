"""
Queries for student's attendance.
"""

from typing import Dict, Optional

from backend.src.data import spreadsheet_ids
from backend.src.google_apis import sheets_api


def get(student_id: int) -> Optional[Dict]:
    """
    Get student's mission team, committee, OLS, and no show attendance.
    """
    all_rows = sheets_api.get_values(spreadsheet_ids.master, 'Master!C2:Q')
    row = next((row for row in all_rows if int(row[0]) == student_id), None)
    if row is None:
        return None
    return {'noShows': str(row[14]),
            'missionTeamAttendance': str(row[12]),
            'committeeAttendance': str(row[13]),
            'olsAttendance': str(row[11])}
