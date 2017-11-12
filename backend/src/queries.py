from .authentication import build_service

MASTER_2017_ID = '1H5leinJFGT1SDfb2hqbDpQgSC_2GYr1HFwKPpzFZ1Js'
ENGAGEMENT_2017_ID = '1FBDR19w831QQ8XTFMns6qVzGEGTv1UU7NAoomTaJRLA'

sheets_service = build_service()


def get_values(spreadsheet_id: str, range_: str):
    result = sheets_service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id, range=range_).execute()
    return result.get('values', [])


def get_name(id: int):
    results = get_values(MASTER_2017_ID, 'Master!A2:C')
    for row in results:
        if int(row[2]) == id:
            return {'id': id, 'name': {'first': row[1], 'last': row[0]}}
    return None


def get_engagement(id: int):
    requirements = get_logged_requirements(id)
    if requirements is None:
        return None
    (accepted_service, accepted_civil_mil) = get_accepted_requirements(id)
    return {"id": id, "approvedService": accepted_service, "approvedCivilMil": accepted_civil_mil,
            "requirements": requirements}


def get_logged_requirements(id: int):
    events = get_values(ENGAGEMENT_2017_ID, 'Responses!A2:Q')
    all_events = []
    for row in events:
        if int(row[6]) == id:
            event_dict = {}
            event_dict.append('type', row[2])
            if row[1] == 'Accepted' or 'Reclassified':
                if row[2] == 'Service':
                    event_dict.append('hours', int(float(row[16])))
                elif row[2] == 'Civil-Mil':
                    event_dict.append('hours', 1)
                elif row[2] == 'Civil-Mil OR Service':
                    event_dict.append('hours', int(float(row[15])))
            event_dict.append('status', row[1])
            if row[12]:
                event_dict.append('name', row[12])
            elif row[13]:
                event_dict.append('name', row[13])
            elif row[14]:
                event_dict.append('name', row[14])
            all_events.append(event_dict)
    if len(all_events) == 0:
        return None
    return event_dict


def get_accepted_requirements(id: int):
    accepted_requirements = get_values(ENGAGEMENT_2017_ID, 'Requirements!A2:C')
    accepted_service_hours = 0
    accepted_civil_mil = 0
    for row in accepted_requirements:
        if int(float(row[0])) == id:
            accepted_service_hours = row[1]
            accepted_civil_mil = row[2]
    return accepted_service_hours, accepted_civil_mil
