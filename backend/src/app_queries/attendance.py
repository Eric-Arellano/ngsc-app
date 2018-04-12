"""
Queries for student's attendance.
"""

from typing import Dict, Optional

from backend.src.data import file_ids, column_indexes
from backend.src.google_apis import sheets_api


def get(student_id: int) -> Optional[Dict]:
    """
    Get student's mission team, committee, OLS, and no show attendance.
    """
    all_rows = sheets_api.get_values(file_ids.master, 'Master!A2:Q')
    row = next((row for row in all_rows if int(row[column_indexes.master['id']]) == student_id), None)
    if row is None:
        return None
    return {'noShows': str(row[column_indexes.master['no_shows']]),
            'missionTeamAttendance': str(row[column_indexes.master['mt_attendance']]),
            'committeeAttendance': str(row[column_indexes.master['committee_attendance']]),
            'olsAttendance': str(row[column_indexes.master['no_shows']])}
