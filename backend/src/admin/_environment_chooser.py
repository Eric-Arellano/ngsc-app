from typing import Callable

from backend.src.data import file_ids


# -------------------------------------------------------
# Attendance rosters
# -------------------------------------------------------

def operate_on_all_attendance(func: Callable, *args, **kwargs) -> None:
    """
    Call the passed function on committee and mission team rosters.
    """
    operate_on_all_committee_attendance(func, *args, **kwargs)
    operate_on_all_mission_team_attendance(func, *args, **kwargs)


def operate_on_all_mission_team_attendance(func: Callable, *args, **kwargs) -> None:
    """
    Call the passed function on mission team rosters.
    """
    for mt_spreadsheet_id in file_ids.mission_team_attendance.values():
        func(mt_spreadsheet_id, *args, **kwargs)


def operate_on_all_committee_attendance(func: Callable, *args, **kwargs) -> None:
    """
    Call the passed function on committee rosters.
    """
    for committee_spreadsheet_id in file_ids.committee_attendance.values():
        func(committee_spreadsheet_id, *args, **kwargs)
