from typing import List, Dict, Optional

from .authentication import build_service
from .student_ids import student_ids

MASTER_2017 = '1H5leinJFGT1SDfb2hqbDpQgSC_2GYr1HFwKPpzFZ1Js'
ENGAGEMENT_2017 = '1FBDR19w831QQ8XTFMns6qVzGEGTv1UU7NAoomTaJRLA'


def get_values(spreadsheet_id: str, range_: str):
    sheets_service = build_service()
    result = sheets_service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id, range=range_).execute()
    return result.get('values', [])


# -------------------------------------------------------------------
# Demographics
# -------------------------------------------------------------------

def get_demographics(student_id: int) -> Optional[Dict]:
    result = student_ids.get(str(student_id), None)
    if result is None:
        return None
    name = result['name']
    return {'id': student_id, 'name': {'first': name['first'], 'last': name['last']},
            'cohort': int(result['cohort']), 'missionTeam': int(result['missionTeam']),
            'committee': result['committee'],
            'leadership': result['leadership']}


def get_all_demographics() -> Dict:
    results = get_values(MASTER_2017, 'Master!A2:O')
    demographic = {}
    for row in results:
        student_id = int(row[2])
        demographic[student_id] = {
            'name': {'first': row[1], 'last': row[0]},
            'cohort': row[7], 'missionTeam': row[8], 'committee': row[9],
            'leadership': row[10]}
    return demographic


# -------------------------------------------------------------------
# Attendance
# -------------------------------------------------------------------

def get_attendance(student_id: int) -> Optional[Dict]:
    all_rows = get_values(MASTER_2017, 'Master!C2:Q')
    row = next((row for row in all_rows if int(row[0]) == student_id), None)
    if row is None:
        return None
    return {'noShows': float(row[14]), 'missionTeamAttendance': str(row[12]),
            'committeeAttendance': str(row[13]), 'olsAttendance': str(row[11])}


# -------------------------------------------------------------------
# Engagement
# -------------------------------------------------------------------

def get_engagement(student_id: int) -> Optional[Dict]:
    (accepted_service, accepted_civil_mil) = get_accepted_engagement(student_id)
    if accepted_service is None or accepted_civil_mil is None:
        return None
    logged_events = get_logged_engagement_events(student_id)
    return {"acceptedService": accepted_service, "acceptedCivilMil": accepted_civil_mil,
            "loggedEvents": logged_events}


def get_logged_engagement_events(student_id: int) -> List:
    all_rows = get_values(ENGAGEMENT_2017, 'Responses!A2:Q')
    return [{'type': row[2],
             'status': row[1],
             'name': row[12] or row[13] or row[14],
             'hours': select_hours(row)
             }
            for row
            in all_rows
            if int(row[6]) == student_id]


def select_hours(row) -> float:
    event_type = row[2]
    if event_type == 'Service':
        return float(row[16])
    elif event_type == 'Civil-Mil OR Service':
        return float(row[15])
    return 0


# TODO: when adding query for getting MT %, committee %, and # no shows, this query should fall into that and 
# come from master spreadsheet to avoid the cost of also searching this spreadsheet. Just get all data from master.
def get_accepted_engagement(student_id: int) -> (Optional[float], Optional[float]):
    all_rows = get_values(ENGAGEMENT_2017, 'Requirements!A2:C')
    row = next((row for row in all_rows if int(row[0]) == student_id), None)
    if row is None:
        return None, None
    service_hours = float(row[1])
    civil_mil = float(row[2])
    return service_hours, civil_mil
