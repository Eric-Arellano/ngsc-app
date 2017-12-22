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

def get_demographics(id: int):
    result = student_ids.get(str(id), None)
    if result:
        name = result['name']
        return {'id': id, 'name': {'first': name['first'], 'last': name['last']},
                    'cohort': int(result['cohort']), 'missionTeam': int(result['missionTeam']), 'committee': result['committee'],
                    'leadership': result['leadership']}
    return None


def get_all_demographics():
    results = get_values(MASTER_2017, 'Master!A2:O')
    demographic = {}
    for row in results:
        id = int(row[2])
        demographic[id] = {
                    'name': {'first': row[1], 'last': row[0]},
                    'cohort': row[7], 'missionTeam': row[8], 'committee': row[9],
                    'leadership': row[10]}
    return demographic

# -------------------------------------------------------------------
# Attendance
# -------------------------------------------------------------------

def get_attendance(id: int):
    results = get_values(MASTER_2017, 'Master!C2:Q')
    attendanceData = {}
    for row in results:
        if int(row[0]) == id:
            attendanceData = {'noShows': float(row[14])}
    return attendanceData

# -------------------------------------------------------------------
# Engagement
# -------------------------------------------------------------------

def get_engagement(id: int):
    (accepted_service, accepted_civil_mil) = get_accepted_requirements(id)
    requirements = get_logged_requirements(id)
    return {"id": id, "acceptedService": accepted_service, "acceptedCivilMil": accepted_civil_mil,
            "requirements": requirements}


def get_logged_requirements(id: int):
    all_responses = get_values(ENGAGEMENT_2017, 'Responses!A2:Q')
    requirements = []
    for row in all_responses:
        if int(row[6]) == id:
            req = {'reqType': row[2],
                   'status': row[1],
                   'name': row[12] or row[13] or row[14],
                   'hours': select_hours(row)}
            requirements.append(req)
    return requirements


def select_hours(row):
    type_ = row[2]
    if type_ == 'Service': return float(row[16])
    elif type_ == 'Civil-Mil OR Service': return float(row[15])
    return 0


# TODO: when adding query for getting MT %, committee %, and # no shows, this query should fall into that and 
# come from master spreadsheet to avoid the cost of also searching this spreadsheet. Just get all data from master.
def get_accepted_requirements(id: int):
    all_accepted_requirements = get_values(ENGAGEMENT_2017, 'Requirements!A2:C')
    accepted_service_hours = 0
    accepted_civil_mil = 0
    for row in all_accepted_requirements:
        if int(row[0]) == id:
            accepted_service_hours = row[1]
            accepted_civil_mil = row[2]
    return accepted_service_hours, accepted_civil_mil
