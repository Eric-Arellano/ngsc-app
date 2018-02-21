"""
Queries for student's civil mil and service.
"""

from typing import Dict, List, Optional, Tuple

from backend.src.data import spreadsheet_ids
from backend.src.google_apis import sheets_api


def get(student_id: int) -> Optional[Dict]:
    """
    Get student's accepted civil mil and service, and a list of logged events.
    """
    (accepted_service, accepted_civil_mil) = _get_accepted(student_id)
    if accepted_service is None or accepted_civil_mil is None:
        return None
    logged_events = _get_logged_events(student_id)
    return {"acceptedService": accepted_service,
            "acceptedCivilMil": accepted_civil_mil,
            "loggedEvents": logged_events}


def _get_logged_events(student_id: int) -> List:
    """
    Get every event logged by student, including the event's status.
    """
    all_rows = sheets_api.get_values(spreadsheet_ids.ENGAGEMENT_SPRING_2018,
                                     'Responses!A2:G')
    return [{'type': row[2],
             'status': row[1],
             'name': row[3],
             'hours': _select_hours(row)
             }
            for row in all_rows
            if int(row[0]) == student_id]


def _select_hours(row) -> float:
    """
    Choose which column to read for number of service hours.
    """
    event_type = row[2]
    if event_type == 'Service':
        return float(row[5])
    elif event_type == 'Civil-Mil OR Service':
        return float(row[6])
    return 0


def _get_accepted(student_id: int) -> Tuple[Optional[float], Optional[float]]:
    """
    Get student's accepted service and civil mil.
    """
    all_rows = sheets_api.get_values(spreadsheet_ids.ENGAGEMENT_SPRING_2018,
                                     'Requirements!A2:C')
    row = next((row for row in all_rows if int(row[0]) == student_id), None)
    if row is None:
        return None, None
    service_hours = float(row[1])
    civil_mil = float(row[2])
    return service_hours, civil_mil
