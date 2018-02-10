from typing import Dict, List, Optional

from backend.src.data import spreadsheet_ids
from backend.src.google_sheets import sheets_interfacer


def get(student_id: int) -> Optional[Dict]:
    (accepted_service, accepted_civil_mil) = _get_accepted(student_id)
    if accepted_service is None or accepted_civil_mil is None:
        return None
    logged_events = _get_logged_events(student_id)
    return {"acceptedService": accepted_service,
            "acceptedCivilMil": accepted_civil_mil,
            "loggedEvents": logged_events}


def _get_logged_events(student_id: int) -> List:
    all_rows = sheets_interfacer.get_values(spreadsheet_ids.ENGAGEMENT_SPRING_2018,
                                            'Responses!A2:G')
    return [{'type': row[2],
             'status': row[1],
             'name': row[3],
             'hours': _select_hours(row)
             }
            for row in all_rows
            if int(row[0]) == student_id]


def _select_hours(row) -> float:
    event_type = row[2]
    if event_type == 'Service':
        return float(row[5])
    elif event_type == 'Civil-Mil OR Service':
        return float(row[6])
    return 0


def _get_accepted(student_id: int) -> (Optional[float], Optional[float]):
    all_rows = sheets_interfacer.get_values(spreadsheet_ids.ENGAGEMENT_SPRING_2018,
                                            'Requirements!A2:C')
    row = next((row for row in all_rows if int(row[0]) == student_id), None)
    if row is None:
        return None, None
    service_hours = float(row[1])
    civil_mil = float(row[2])
    return service_hours, civil_mil
