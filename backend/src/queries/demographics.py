"""
Queries for student's static demographic info.
"""

from typing import Dict, Optional

from backend.src.data import spreadsheet_ids
from backend.src.data.demographics import demographics_data
from backend.src.google_sheets import sheets_interfacer


def get(student_id: int) -> Optional[Dict]:
    """
    Get student's name, cohort, mission team, committee, and leadership position.
    """
    result = demographics_data.get(str(student_id), None)
    if result is None:
        return None
    name = result['name']
    return {'name':
                {'first': name['first'],
                 'last': name['last']},
            'cohort': int(result['cohort']),
            'missionTeam': int(result['missionTeam']),
            'committee': result['committee'],
            'leadership': result['leadership']}


def get_all() -> Dict:
    """
    Get every student's demographic info as a dictionary indexed by student id.
    """
    results = sheets_interfacer.get_values(spreadsheet_ids.MASTER_SPRING_2018,
                                           'Master!A2:O')
    demographic = {}
    for row in results:
        student_id = int(row[2])
        demographic[student_id] = {
            'name':
                {'first': row[1],
                 'last': row[0]},
            'cohort': row[7],
            'missionTeam': row[8],
            'committee': row[9],
            'leadership': row[10]}
    return demographic
