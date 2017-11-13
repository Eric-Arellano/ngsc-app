from .authentication import build_service

MASTER_2017 = '1H5leinJFGT1SDfb2hqbDpQgSC_2GYr1HFwKPpzFZ1Js'
ENGAGEMENT_2017 = '1FBDR19w831QQ8XTFMns6qVzGEGTv1UU7NAoomTaJRLA'


def get_values(spreadsheet_id: str, range_: str):
    sheets_service = build_service()
    result = sheets_service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id, range=range_).execute()
    return result.get('values', [])


def get_name(id: int):
    results = get_values(MASTER_2017, 'Master!A2:C')
    for row in results:
        if int(row[2]) == id:
            return {'id': id, 'name': {'first': row[1], 'last': row[0]}}
    return None


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
                   'hours': select_hours(row[2], row)}
            requirements.append(req)
    return requirements


def select_hours(type: str, row):
    if type == 'Service': return float(row[16])
    elif type == 'Civil-Mil OR Service': return float(row[15])
    return 0


def get_accepted_requirements(id: int):
    all_accepted_requirements = get_values(ENGAGEMENT_2017, 'Requirements!A2:C')
    accepted_service_hours = 0
    accepted_civil_mil = 0
    for row in all_accepted_requirements:
        if int(row[0]) == id:
            accepted_service_hours = row[1]
            accepted_civil_mil = row[2]
    return accepted_service_hours, accepted_civil_mil
