"""
Queries for student's civil mil and service.
"""

from typing import Dict, List, Optional, Union

from backend.src.data import column_indexes, file_ids
from backend.src.sheets_commands import sheet


def get(student_id: int) -> Optional[Dict]:
    """
    Get student's accepted civil mil and service, and a list of logged events.
    """
    accepted = _get_accepted(student_id)
    if accepted is None:
        return None
    logged_events = {'loggedEvents': _get_logged_events(student_id)}
    # Merge dictionaries
    return {**accepted, **logged_events}


def _get_logged_events(student_id: int) -> List[Dict[str, Union[str, float]]]:
    """
    Get every event logged by student, including the event's status.
    """
    all_rows = sheet.get_values(file_ids.participation['engagement'],
                                range_='Responses!A2:G')
    return [{'type': row[column_indexes.engagement_responses['type']],
             'status': row[column_indexes.engagement_responses['status']],
             'name': row[column_indexes.engagement_responses['name']],
             'hours': float(row[column_indexes.engagement_responses['hours']])
             }
            for row in all_rows
            if int(row[column_indexes.engagement_responses['id']]) == student_id]


def _get_accepted(student_id: int) -> Optional[Dict[str, float]]:
    """
    Get student's accepted service and civil mil.
    """
    all_rows = sheet.get_values(file_ids.participation['engagement'],
                                range_='Total!A2:E')
    row = next((row for row in all_rows
                if int(row[column_indexes.engagement_accepted['id']]) == student_id),
               None)
    if row is None:
        return None
    return {
        'acceptedService': float(row[column_indexes.engagement_accepted['service']]),
        "acceptedCivilMil": float(row[column_indexes.engagement_accepted['civil_mil']]),
        "acceptedTotal": float(row[column_indexes.engagement_accepted['hours_total']]),
        "acceptedNGSC": float(row[column_indexes.engagement_accepted['ngsc']])
    }
