import textwrap
from typing import Dict, List, Union

from backend.src.data import column_indexes
from backend.src.sheets_commands import sheet

Formula = str


# ---------------------------------------------------------------------
#  Helpers
# ---------------------------------------------------------------------


def roster_participation() -> Formula:
    def count_if(criterion: str) -> str:
        return f'COUNTIF(I@:AA@, "{criterion}")'  # Replace @ with row index

    return f"""=TO_PERCENT(IFERROR(
           ({count_if("yes")} + {count_if("remote")} + {count_if("excused")}) / 
           ({count_if("yes")} + {count_if("no")} + {count_if("remote")} + {count_if("excused")})
           , ""))"""


def query_for_id(
    *,
    spreadsheet_id: sheet.ID,
    tab_range: str,
    target_column: int,
    match_column: int,
    equal_signs_prefix: bool = True,
) -> Formula:
    """
    Get accompanying value for matching ID.

    This function is zero-indexed, unlike the actual Sheets formula.
    """
    formula = textwrap.dedent(
        f"""QUERY(IMPORTRANGE("https://docs.google.com/spreadsheets/d/{spreadsheet_id}", "{tab_range}"),
            "select Col{target_column + 1} where Col{match_column + 1}='" &C@& "' limit 1", -1)"""
    )
    return f"={formula}" if equal_signs_prefix else formula


def roster_switch(
    *,
    roster_id_map: Dict[Union[str, int], sheet.ID],
    association_column_letter: str,
    leadership_role: str,
) -> Formula:
    def switch_item(key: Union[str, int], roster_file_id: sheet.ID) -> Formula:
        query = query_for_id(
            spreadsheet_id=roster_file_id,
            tab_range="Attendance!A$2:B",
            target_column=column_indexes.roster["participation"],
            match_column=column_indexes.roster["asurite"],
            equal_signs_prefix=False,
        )
        formatted_key = f'"{key}"' if isinstance(key, str) else key
        return f"{formatted_key}, {query},\n"

    statements: List[str] = [
        switch_item(key, roster_id) for key, roster_id in roster_id_map.items()
    ]
    return textwrap.dedent(
        f"""=IF(K@="{leadership_role}", 100%, SWITCH({association_column_letter}@,
            {''.join(statements)}
            "", ""))
            """
    )


# ---------------------------------------------------------------------
#  Engagement Hours
# ---------------------------------------------------------------------

engagement_tab_range = "Total!A$2:E"


def master_civil_mil(*, engagement_id: sheet.ID) -> Formula:
    return query_for_id(
        spreadsheet_id=engagement_id,
        tab_range=engagement_tab_range,
        target_column=column_indexes.engagement_accepted["civil_mil"],
        match_column=column_indexes.engagement_accepted["asurite"],
    )


def master_hours_total(*, engagement_id: sheet.ID) -> Formula:
    return query_for_id(
        spreadsheet_id=engagement_id,
        tab_range=engagement_tab_range,
        target_column=column_indexes.engagement_accepted["hours_total"],
        match_column=column_indexes.engagement_accepted["asurite"],
    )


def master_service(*, engagement_id: sheet.ID) -> Formula:
    return query_for_id(
        spreadsheet_id=engagement_id,
        tab_range=engagement_tab_range,
        target_column=column_indexes.engagement_accepted["service"],
        match_column=column_indexes.engagement_accepted["asurite"],
    )


def master_ngsc(*, engagement_id: sheet.ID) -> Formula:
    return query_for_id(
        spreadsheet_id=engagement_id,
        tab_range=engagement_tab_range,
        target_column=column_indexes.engagement_accepted["ngsc"],
        match_column=column_indexes.engagement_accepted["asurite"],
    )


# ---------------------------------------------------------------------
#  Attendance
# ---------------------------------------------------------------------


def master_all_student(*, all_student_id: sheet.ID) -> Formula:
    return query_for_id(
        spreadsheet_id=all_student_id,
        tab_range="Total!A$2:B",
        target_column=column_indexes.all_students["total"],
        match_column=column_indexes.all_students["asurite"],
    )


def master_no_shows(*, no_shows_id: sheet.ID) -> Formula:
    return query_for_id(
        spreadsheet_id=no_shows_id,
        tab_range="Total!A$2:B",
        target_column=column_indexes.no_shows["total"],
        match_column=column_indexes.no_shows["asurite"],
    )


def master_committee_attendance(*, committee_id_map: Dict[str, sheet.ID]) -> Formula:
    return roster_switch(
        roster_id_map=committee_id_map,
        association_column_letter="K",
        leadership_role="Committee Chair",
    )


def master_mt_attendance(*, mt_id_map: Dict[int, sheet.ID]) -> Formula:
    return roster_switch(
        roster_id_map=mt_id_map,
        association_column_letter="J",
        leadership_role="MT Leader",
    )


# ---------------------------------------------------------------------
#  Triggers
# ---------------------------------------------------------------------


def master_triggers_current() -> Formula:
    return textwrap.dedent(
        """=SUM(
            COUNTIF(L@, "<8"),
            COUNTIF(M@, "<1"),
            COUNTIF(N@, "<.5"),
            COUNTIF(O@, "<.5"),
            COUNTIF(P@, "<.5"),
            COUNTIF(Q@, ">=2")
            )"""
    )


def master_triggers_earlier_semester(*, old_master_id: sheet.ID) -> Formula:
    return query_for_id(
        spreadsheet_id=old_master_id,
        tab_range="Master!A$2:Z",
        target_column=column_indexes.master["triggers_current"],
        match_column=column_indexes.master["asurite"],
    )
