"""
Queries for student's static demographic info.
"""

from typing import Dict, Optional

from backend.src.app import encryptor
from backend.src.data import column_indexes, file_ids, mission_teams
from backend.src.data.demographics import demographics_data
from backend.src.sheets_commands import sheet


def get(student_id: int) -> Optional[Dict]:
    """
    Get student's name, cohort, mission team, committee, and leadership position.
    """
    encrypted_id = encryptor.encrypt(str(student_id))
    result = demographics_data.get(encrypted_id, None)
    result = encryptor.decrypt_dict_values(result)
    if result is None:
        return None
    mission_team_number = int(result['missionTeam']) if result['missionTeam'] else None
    return {'name':
                {'first': result['name']['first'],
                 'last': result['name']['last']},
            'cohort': int(result['cohort']),
            'missionTeam': (f'{mission_team_number} - {mission_teams.missions[mission_team_number]}'
                            if mission_team_number else ''),
            'committee': result['committee'],
            'leadership': result['leadership'],
            'email': result['email'],
            'phone': result['phone'],
            'campus': result['campus'],
            }


def get_all() -> Dict:
    """
    Get every student's demographic info as a dictionary indexed by student id.
    """
    results = sheet.get_values(file_ids.master,
                               range_='Master!A2:O')
    demographic = {}
    for row in results:
        student_id = row[column_indexes.master['id']]
        demographic[student_id] = {
            'name':
                {'first': row[column_indexes.master['first']],
                 'last': row[column_indexes.master['last']]},
            'cohort': row[column_indexes.master['cohort']],
            'missionTeam': row[column_indexes.master['mt']],
            'committee': row[column_indexes.master['committee']],
            'leadership': row[column_indexes.master['leadership']],
            'email': row[column_indexes.master['email']],
            'phone': row[column_indexes.master['phone']],
            'campus': row[column_indexes.master['campus']],
        }
    return demographic


def get_all_encrypted() -> Dict:
    """
    Get every student's info and obfuscate the data.
    """
    demographics = get_all()
    return encryptor.encrypt_demographics(demographics)
