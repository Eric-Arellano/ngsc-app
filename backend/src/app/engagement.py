"""
Queries for student's civil mil and service.
"""

from typing import Dict, List, Optional, Tuple

from backend.src.data import column_indexes, file_ids
from backend.src.sheets_commands import sheet


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
    all_rows = sheet.get_values(file_ids.participation['engagement'],
                                range_='Responses!A2:G')
    return [{'type': row[column_indexes.engagement_responses['type']],
             'status': row[column_indexes.engagement_responses['status']],
             'name': row[column_indexes.engagement_responses['name']],
             'hours': _select_hours(row)
             }
            for row in all_rows
            if int(row[column_indexes.engagement_responses['id']]) == student_id]


def _select_hours(row) -> float:
    """
    Choose which column to read for number of service hours.
    """
    event_type = row[column_indexes.engagement_responses['type']]
    if event_type == 'Service':
        return float(row[column_indexes.engagement_responses['service_hours']])
    elif event_type == 'Civil-Mil OR Service':
        return float(row[column_indexes.engagement_responses['civil_mil_hours']])
    return 0


def _get_accepted(student_id: int) -> Tuple[Optional[float], Optional[float]]:
    """
    Get student's accepted service and civil mil.
    """
    all_rows = sheet.get_values(file_ids.participation['engagement'],
                                range_='Requirements!A2:C')
    row = next((row for row in all_rows
                if int(row[column_indexes.engagement_accepted['id']]) == student_id),
               None)
    if row is None:
        return None, None
    service_hours = float(row[column_indexes.engagement_accepted['service']])
    civil_mil = float(row[column_indexes.engagement_accepted['civil_mil']])
    return service_hours, civil_mil
