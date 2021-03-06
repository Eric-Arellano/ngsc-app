#!/usr/bin/env python3.7

"""
CLI script to setup the Google Drive for a new semester.

Should be run locally, not on the server.
"""
import os
import sys
from pathlib import Path
import pprint
import re
import functools
import textwrap
import math
from typing import Dict, List, Union, NamedTuple

from googleapiclient import discovery

# path hack, https://chrisyeh96.github.io/2017/08/08/definitive-guide-python-imports.html
current_file_path = Path(os.path.realpath(__file__))
sys.path.append(str(current_file_path.parents[1]))
sys.path.append(str(current_file_path.parents[4]))

from backend.src.google_apis import (  # pylint: disable=wrong-import-position
    drive_api,
    sheets_api,
)
from backend.src.data import (  # pylint: disable=wrong-import-position
    column_indexes,
    file_ids,
    folder_ids,
    sheet_formulas,
)
from backend.src.data.new_semester import (  # pylint: disable=wrong-import-position
    new_leadership,
    new_file_ids,
    new_folder_ids,
)
from backend.src.drive_commands import (  # pylint: disable=wrong-import-position
    copy,
    create,
    generate_link,
)
from backend.src.sheets_commands import (  # pylint: disable=wrong-import-position
    columns,
    display,
    formulas,
    sheet,
    validation,
    rows,
    tab,
)
from scripts import backend  # pylint: disable=wrong-import-position
from scripts.utils import command_line  # pylint: disable=wrong-import-position

Semester = str
ResourceID = str
Key = Union[str, int]
IdMap = Dict[Key, Union[ResourceID, Dict[Key, ResourceID]]]


def main() -> None:
    print_debugging_tips()
    script_section = ask_script_section()
    # create api services
    drive_service = drive_api.build_service()
    sheets_service = sheets_api.build_service()
    if script_section == 1:  # create & save resources
        semester = ask_semester_target()
        # create resources
        folder_id_map = create_empty_folders(
            semester=semester, drive_service=drive_service
        )
        roster_ids = create_empty_rosters(
            folder_id_map=folder_id_map, semester=semester, drive_service=drive_service
        )
        important_files = copy_important_files(
            folder_id_map=folder_id_map, semester=semester, drive_service=drive_service
        )
        file_id_map = {**roster_ids, **important_files}
        # save to hardcoded files
        save_folder_ids(folder_id_map)
        save_file_ids(file_id_map)
        backend.fmt()
        prompt_to_add_admin_email()
        prompt_to_restart_script()
    elif script_section == 2:  # prepare & modify resources
        # steps before adding data
        check_new_ids_different()
        # update ID lists
        update_participation_asurite_list(sheets_service=sheets_service)
        # clear old data
        clear_engagement_data(sheets_service=sheets_service)
        clear_no_show_data(sheets_service=sheets_service)
        rising_cohorts = ask_rising_cohorts()
        clear_outdated_master(
            sophomore_cohort=rising_cohorts.sophomores,
            senior_cohort=rising_cohorts.seniors,
            sheets_service=sheets_service,
        )
        prompt_to_clear_remaining_old_data()
        # mission team reshuffle
        reshuffle_mission_teams(sheets_service=sheets_service)
        # prepare leadership
        prompt_to_add_leadership()
        prepare_leadership_roster(sheets_service=sheets_service)
        # prepare files
        prepare_all_rosters(sheets_service=sheets_service)
        update_master_formulas(sheets_service=sheets_service)
        # remaining steps
        prompt_to_connect_master_links()
        print_remaining_steps()


# ------------------------------------------------------------------
# Start script
# ------------------------------------------------------------------


def print_debugging_tips() -> None:
    """
    Give instructions for if the script fails.
    """
    print(
        textwrap.dedent(
            """\
        -------------------------------------
        Disclaimer: this is a very long script with multiple potential points of failure.
        
        It is divided up into two parts. 
        - If Part 1 fails, delete the Google Drive folder and restart.
        - If Part 2 fails, comment out the steps already completed in Part 2, and rerun the script with Part 2.
        
        Potential sources of failure (non-exhaustive):
        - Frequently Google's API server itself fails. Try running the script again to see if the same error occurs at the same place.
        - Prior copies of the participation forms exist in the current semester's folder, which will cause an ambiguous search. Delete any prior "Copy of X".
        - Column indexes were changed. Compare actual indexes with this script and `data/column_indexes`.
        - Tab names were changed. Compare to the formulas in `data/sheet_formulas`.
        - `copy_important_files` fails because API is overloaded and does not create the accompanying forms quickly enough. Try changing the timeout.
        - Roster already has alternated coloring. If this happens, comment out `prepare_all_rosters()` and rerun this script Part 2, along with `./ngsc rebuild-rosters`.
        
        These should not be sources of error, but check just in case:
        - Changed file names. The scripts work by File IDs, instead of file names. 
        -------------------------------------\n\n
    """
        )
    )


def ask_script_section() -> int:
    """
    Ask if part 1 or part 2 of script.
    """
    answer = command_line.ask_input(
        prompt=textwrap.dedent(
            """\
                        Which part of the script would you like to run?
                        1) Create the empty folders and files. Run this first.
                        2) Prepare & modify files. Requires part 1 to have been completed. 
                        
                        Enter 1 or 2."""
        ),
        is_valid=lambda x: x in ["1", "2"],
    )
    return int(answer)


def ask_semester_target() -> str:
    """
    Ask CLI user for the target semester in correct format, e.g. 'Spring 2018'.
    """

    def is_valid_semester(answer: str) -> bool:
        words = answer.split()
        if len(words) != 2:
            return False
        prefix_is_semester = words[0] == "Fall" or words[0] == "Spring"
        postfix_is_year = bool(re.match(r"^(20)\d{2}$", words[1]))
        return prefix_is_semester and postfix_is_year

    return command_line.ask_input(
        prompt=textwrap.dedent(
            """\
                        What semester are you creating this for?
                        Enter in the format \'Spring 2018\', \'Fall 2023\'."""
        ),
        is_valid=is_valid_semester,
    )


# ------------------------------------------------------------------
# Create resources
# ------------------------------------------------------------------


@command_line.log(
    start_message="Creating empty folders.", end_message="Empty folders created\n"
)
def create_empty_folders(
    *, semester: Semester, drive_service: discovery.Resource = None
) -> IdMap:
    """
    Set up the folder structure and return their IDs.
    """
    # setup drive service
    if drive_service is None:
        drive_service = drive_api.build_service()
    create_folder = functools.partial(create.folder, drive_service=drive_service)
    batch_create_folder = functools.partial(
        create.batch_folder, drive_service=drive_service
    )
    # Root level
    semester_root = create_folder(semester, parent_folder_id=folder_ids.ngsc_root)
    id_map: IdMap = {
        "ngsc_root": folder_ids.ngsc_root,
        "drive_playground": folder_ids.drive_playground,
        "semester_root": semester_root,
    }
    # Root subfolders
    root_subfolders_ids = batch_create_folder(
        [
            create.BatchArgument("Templates", parent_folder_id=semester_root),
            create.BatchArgument("All students", parent_folder_id=semester_root),
            create.BatchArgument("Leadership", parent_folder_id=semester_root),
            create.BatchArgument("Sections", parent_folder_id=semester_root),
            create.BatchArgument("Committees", parent_folder_id=semester_root),
        ]
    )
    id_map.update(
        {
            "templates": root_subfolders_ids[0],
            "all_students_root": root_subfolders_ids[1],
            "leadership_root": root_subfolders_ids[2],
            "sections_root": root_subfolders_ids[3],
            "committees_root": root_subfolders_ids[4],
        }
    )
    # All students subfolders
    all_students_subfolders_ids = batch_create_folder(
        [
            create.BatchArgument(
                "On Leadership", parent_folder_id=id_map["all_students_root"]
            ),
            create.BatchArgument(
                "Participation", parent_folder_id=id_map["all_students_root"]
            ),
        ]
    )
    id_map["all_students"] = {
        "on_leadership": all_students_subfolders_ids[0],
        "participation": all_students_subfolders_ids[1],
    }
    # Leadership subfolders
    briefings = create_folder("Training", parent_folder_id=id_map["leadership_root"])
    id_map["leadership"] = {"training": briefings}
    # Sections folders
    section_folders = [
        create.BatchArgument(
            f"Section {section_index}", parent_folder_id=id_map["sections_root"]
        )
        for section_index in range(1, 11)
    ]
    section_folders_ids = batch_create_folder(section_folders)
    id_map["sections"] = dict(zip(range(1, 11), section_folders_ids))
    # Mission team folders
    mission_team_folders_by_section = [
        [
            create.BatchArgument(
                f"Mission team {mt_number}",
                parent_folder_id=id_map["sections"][section_index],
            )
            for mt_number in (
                mt_index + (3 * (section_index - 1)) for mt_index in range(1, 4)
            )
        ]
        for section_index in range(1, 11)
    ]
    mission_team_folders_flattened = [
        x for y in mission_team_folders_by_section for x in y
    ]
    mission_team_folders_ids = batch_create_folder(mission_team_folders_flattened)
    id_map["mission_teams"] = dict(zip(range(1, 31), mission_team_folders_ids))
    # Committee Leads
    committee_leads_folders_ids = batch_create_folder(
        [
            create.BatchArgument(
                "Engagement", parent_folder_id=id_map["committees_root"]
            ),
            create.BatchArgument(
                "Education", parent_folder_id=id_map["committees_root"]
            ),
            create.BatchArgument("Culture", parent_folder_id=id_map["committees_root"]),
        ]
    )
    id_map["committee_leads"] = {
        "Engagement": committee_leads_folders_ids[0],
        "Education": committee_leads_folders_ids[1],
        "Culture": committee_leads_folders_ids[2],
    }
    # Committee Chairs
    committee_chairs_folders_ids = batch_create_folder(
        [
            create.BatchArgument("Admin", parent_folder_id=id_map["committees_root"]),
            create.BatchArgument(
                "Transfers", parent_folder_id=id_map["committee_leads"]["Engagement"]
            ),
            create.BatchArgument(
                "Civil-Mil", parent_folder_id=id_map["committee_leads"]["Engagement"]
            ),
            create.BatchArgument(
                "Service", parent_folder_id=id_map["committee_leads"]["Engagement"]
            ),
            create.BatchArgument(
                "Training", parent_folder_id=id_map["committee_leads"]["Education"]
            ),
            create.BatchArgument(
                "Ambassadors", parent_folder_id=id_map["committee_leads"]["Education"]
            ),
            create.BatchArgument(
                "Communications", parent_folder_id=id_map["committee_leads"]["Culture"]
            ),
            create.BatchArgument(
                "Events", parent_folder_id=id_map["committee_leads"]["Culture"]
            ),
            create.BatchArgument(
                "Social", parent_folder_id=id_map["committee_leads"]["Culture"]
            ),
        ]
    )
    id_map["committees"] = {
        "Admin": committee_chairs_folders_ids[0],
        "Transfers": committee_chairs_folders_ids[1],
        "Civil-Mil": committee_chairs_folders_ids[2],
        "Service": committee_chairs_folders_ids[3],
        "Training": committee_chairs_folders_ids[4],
        "Ambassadors": committee_chairs_folders_ids[5],
        "Communications": committee_chairs_folders_ids[6],
        "Events": committee_chairs_folders_ids[7],
        "Social": committee_chairs_folders_ids[8],
    }
    return id_map


@command_line.log(
    start_message="Creating empty rosters.", end_message="Empty rosters created\n"
)
def create_empty_rosters(
    *,
    folder_id_map: IdMap,
    semester: Semester,
    drive_service: discovery.Resource = None,
) -> IdMap:
    """
    Create the roster spreadsheets (not set up) and save their IDs.
    """
    # setup drive service
    if drive_service is None:
        drive_service = drive_api.build_service()
    batch_create_gsheet = functools.partial(
        create.batch_gsheet, drive_service=drive_service
    )
    # Leadership
    leadership_roster_id = create.gsheet(
        file_name=f"Leadership - {semester}",
        parent_folder_id=folder_id_map["leadership_root"],
        drive_service=drive_service,
    )
    # Committee rosters
    committee_rosters = [
        create.BatchArgument(
            name=f"Attendance - {committee} - {semester}", parent_folder_id=folder_id
        )
        for committee, folder_id in folder_id_map["committees"].items()
    ]
    committee_roster_ids = batch_create_gsheet(committee_rosters)
    committee_file_dict = dict(
        zip(folder_id_map["committees"].keys(), committee_roster_ids)
    )
    # Mission team rosters
    mission_team_rosters = [
        create.BatchArgument(
            name=f"Attendance - Mission Team {mt_number} - {semester}",
            parent_folder_id=folder_id,
        )
        for mt_number, folder_id in folder_id_map["mission_teams"].items()
    ]
    mission_team_roster_ids = batch_create_gsheet(mission_team_rosters)
    mission_team_file_dict = dict(
        zip(folder_id_map["mission_teams"].keys(), mission_team_roster_ids)
    )
    return {
        "leadership_roster": leadership_roster_id,
        "committee_attendance": committee_file_dict,
        "mission_team_attendance": mission_team_file_dict,
    }


@command_line.log(
    start_message="Copying important files.", end_message="Important files copied.\n"
)
def copy_important_files(
    *,
    folder_id_map: IdMap,
    semester: Semester,
    drive_service: discovery.Resource = None,
) -> IdMap:
    """
    Copy the Master, schedule, all-student attendance, no shows, & templates.
    """
    if drive_service is None:
        drive_service = drive_api.build_service()
    batch_copy_file = functools.partial(copy.batch, drive_service=drive_service)
    copy_linked_sheet_and_form = functools.partial(
        copy.linked_sheet_and_form,
        drive_service=drive_service,
        initial_form_search_delay=20,
        timeout=120,
    )
    # normal files
    copied_file_ids = batch_copy_file(
        [
            copy.BatchArgument(
                origin_resource_id=file_ids.master,
                new_name=f"Master - {semester}",
                target_folder_id=folder_id_map["semester_root"],
            ),
            copy.BatchArgument(
                origin_resource_id=file_ids.schedule,
                new_name=f"Schedule - {semester}",
                target_folder_id=folder_id_map["semester_root"],
            ),
            copy.BatchArgument(
                origin_resource_id=file_ids.templates["rsvp"],
                new_name="RSVP Template",
                target_folder_id=folder_id_map["templates"],
            ),
            copy.BatchArgument(
                origin_resource_id=file_ids.templates["initial_meeting"],
                new_name="Initial meeting template",
                target_folder_id=folder_id_map["templates"],
            ),
            copy.BatchArgument(
                origin_resource_id=file_ids.templates["event_proposal"],
                new_name="Event proposal template",
                target_folder_id=folder_id_map["templates"],
            ),
            copy.BatchArgument(
                origin_resource_id=file_ids.templates["ols_cancel_rsvp"],
                new_name="OLS cancel RSVP template",
                target_folder_id=folder_id_map["templates"],
            ),
            copy.BatchArgument(
                origin_resource_id=file_ids.participation["all_students"],
                new_name=f"All student attendance - {semester}",
                target_folder_id=folder_id_map["all_students"]["participation"],
            ),
        ]
    )
    id_map: IdMap = {
        "master_prior_semester": file_ids.master,
        "master": copied_file_ids[0],
        "schedule": copied_file_ids[1],
        "templates": {
            "rsvp": copied_file_ids[2],
            "initial_meeting": copied_file_ids[3],
            "event_proposal": copied_file_ids[4],
            "ols_cancel_rsvp": copied_file_ids[5],
        },
        "participation": {"all_students": copied_file_ids[6]},
    }
    # linked spreadsheet and form
    engagement = copy_linked_sheet_and_form(
        origin_sheet_id=file_ids.participation["engagement"],
        origin_form_id=file_ids.participation["engagement_form"],
        origin_parent_folder_id=folder_ids.all_students["participation"],
        new_sheet_name=f"Engagement - {semester}",
        new_form_name=f"Engagement - {semester}",
        target_parent_folder_id=folder_id_map["all_students"]["participation"],
    )
    no_shows = copy_linked_sheet_and_form(
        origin_sheet_id=file_ids.participation["no_shows"],
        origin_form_id=file_ids.participation["no_shows_form"],
        origin_parent_folder_id=folder_ids.all_students["participation"],
        new_sheet_name=f"No shows - {semester}",
        new_form_name=f"No shows - {semester}",
        target_parent_folder_id=folder_id_map["all_students"]["participation"],
    )
    id_map["participation"].update(
        {
            "engagement": engagement.sheet,
            "engagement_form": engagement.form,
            "no_shows": no_shows.sheet,
            "no_shows_form": no_shows.form,
        }
    )
    return id_map


# ------------------------------------------------------------------
# Save IDs to hardcoded files.
# ------------------------------------------------------------------


@command_line.log(
    end_message="Folder IDs saved to `backend/src/data/new_semester/new_folder_ids.py`.\n"
)
def save_folder_ids(ids: IdMap) -> None:
    """
    Write the given folder IDs to the file `data/folder_ids.py`.
    """
    output = _format_id_output(ids)
    with open("backend/src/data/new_semester/new_folder_ids.py", "w") as file:
        file.writelines(output)


@command_line.log(
    end_message="File IDs saved to `backend/src/data/new_semester/new_file_ids.py`.\n"
)
def save_file_ids(ids: IdMap) -> None:
    """
    Write the given file IDs to the file `data/file_ids.py`.
    """
    output = _format_id_output(ids)
    with open("backend/src/data/new_semester/new_file_ids.py", "w") as file:
        file.writelines(output)


def prompt_to_add_admin_email() -> None:
    """
    Make sure new admin chair added to leadership data file. Necessary for preparing rosters.
    """
    command_line.ask_confirmation(
        instructions=textwrap.dedent(
            """\
            1. Open up the file `backend/src/data/new_semester/new_leadership.py`. 
            2. Add the emails for the new Admin Chair, Chief of Staff, and staff."""
        ),
        default_to_yes=True,
    )


def prompt_to_restart_script() -> None:
    """
    Instruct user to restart script to complete part 2 of the script.
    """
    print(
        textwrap.dedent(
            """\
        Part 1 complete! All content has been created and saved (although everything is empty).
        You must now restart the script with `./ngsc setup-semester` and choose part 2.
        This is because the saved file IDs must be reloaded.
        Part 2 will update and prepare the resources.\n"""
        )
    )


# ------------------------------------------------------------------
# Steps before adding data
# ------------------------------------------------------------------


@command_line.log(
    start_message="Checking new IDs are different than current IDs so that the script doesn't overwrite current data.",
    end_message="IDs are different. Safe to continue.\n",
)
def check_new_ids_different() -> None:
    """
    Check new and old file & folder IDs are different.
    """
    files_different = (
        (file_ids.master != new_file_ids.master)
        and (file_ids.master_prior_semester != new_file_ids.master_prior_semester)
        and (file_ids.committee_attendance != new_file_ids.committee_attendance)
        and (file_ids.mission_team_attendance != new_file_ids.mission_team_attendance)
        and (file_ids.participation != new_file_ids.participation)
        and (file_ids.templates != new_file_ids.templates)
        and (file_ids.schedule != new_file_ids.schedule)
    )
    if not files_different:
        raise SystemExit(
            textwrap.dedent(
                """\
            At least one new file ID is the same as a current file ID. 
            Make sure you ran `./ngsc setup-semester` Part 1.
            Aborting script."""
            )
        )
    folders_different = (
        (folder_ids.semester_root != new_folder_ids.semester_root)
        and (folder_ids.all_students != new_folder_ids.all_students)
        and (folder_ids.committees != new_folder_ids.committees)
        and (folder_ids.committee_leads != new_folder_ids.committee_leads)
        and (folder_ids.sections != new_folder_ids.sections)
        and (folder_ids.mission_teams != new_folder_ids.mission_teams)
    )
    if not folders_different:
        raise SystemExit(
            textwrap.dedent(
                """\
            At least one new folder ID is the same as a current folder ID. 
            Make sure you ran `./ngsc setup-semester` Part 1.
            Aborting script."""
            )
        )


def _format_id_output(ids: IdMap) -> str:
    """
    Convert ID dict to output as variables separated by newlines.
    """
    variable_syntax = [
        f"{k} = '{v}'" if isinstance(v, str) else f"{k} = {pprint.pformat(v)}"
        for k, v in ids.items()
    ]
    return "\n\n".join(variable_syntax)


# ------------------------------------------------------------------
# Update Participation ID lists
# ------------------------------------------------------------------


@command_line.log(
    start_message="Updating ASUrite lists for participation spreadsheets.",
    end_message="ASUrite lists updated.\n",
)
def update_participation_asurite_list(
    *, sheets_service: discovery.Resource = None
) -> None:
    """
    Re-pull the list of ASUrites for All Student Attendance, No Shows, and Engagement.
    """
    asurites = sheet.get_values(
        spreadsheet_id=new_file_ids.master,
        range_="Master!C2:C",
        sheets_service=sheets_service,
    )
    update_asurite_list = functools.partial(
        sheet.update_values,
        range_="Total!A2:A",
        grid=asurites,
        sheets_service=sheets_service,
    )
    update_asurite_list(spreadsheet_id=new_file_ids.participation["engagement"])
    update_asurite_list(spreadsheet_id=new_file_ids.participation["no_shows"])
    update_asurite_list(spreadsheet_id=new_file_ids.participation["engagement"])


# ------------------------------------------------------------------
# Clear old data
# ------------------------------------------------------------------


class RisingCohorts(NamedTuple):
    sophomores: int
    seniors: int


def ask_rising_cohorts() -> RisingCohorts:
    """
    Ask who are rising sophomores and seniors.
    """

    def is_valid_cohort(answer: str) -> bool:
        return bool(re.match("^[1-9][0-9]?$", answer))

    sophomore = command_line.ask_input(
        prompt=textwrap.dedent(
            """\
                        Which cohort are the rising sophomores?
                        Enter as a whole number."""
        ),
        is_valid=is_valid_cohort,
    )
    senior = command_line.ask_input(
        prompt=textwrap.dedent(
            """\
                        Which cohort are the rising seniors?
                        Enter as a whole number."""
        ),
        is_valid=is_valid_cohort,
    )
    return RisingCohorts(sophomores=int(sophomore), seniors=int(senior))


@command_line.log(
    start_message="Clearing engagement data.", end_message="Engagement data cleared.\n"
)
def clear_engagement_data(*, sheets_service: discovery.Resource = None) -> None:
    """
    Remove last semester's submissions.
    """
    original_grid = sheet.get_values(
        new_file_ids.participation["engagement"],
        range_="Responses!A2:Z",
        sheets_service=sheets_service,
    )
    cleared_grid = columns.clear(grid=original_grid, target_indexes=list(range(30)))
    sheet.update_values(
        spreadsheet_id=new_file_ids.participation["engagement"],
        range_="Responses!A2:Z",
        grid=cleared_grid,
        sheets_service=sheets_service,
    )


@command_line.log(
    start_message="Clearing no-show form data.",
    end_message="No-show form data cleared.\n",
)
def clear_no_show_data(*, sheets_service: discovery.Resource = None) -> None:
    """
    Remove last semester's submissions.
    """
    original_grid = sheet.get_values(
        new_file_ids.participation["no_shows"],
        range_="'Form events'!A2:BU",
        sheets_service=sheets_service,
    )
    cleared_grid = columns.clear(grid=original_grid, target_indexes=list(range(70)))
    sheet.update_values(
        spreadsheet_id=new_file_ids.participation["no_shows"],
        range_="'Form events'!A2:BU",
        grid=cleared_grid,
        sheets_service=sheets_service,
    )


@command_line.log(
    start_message="Clearing outdated master info (current leadership, sophomores with committees, and seniors with mission teams).",
    end_message="Cleared outdated master info.\n",
)
def clear_outdated_master(
    *,
    sophomore_cohort: int,
    senior_cohort: int,
    sheets_service: discovery.Resource = None,
) -> None:
    """
    Remove committees for rising sophomores and mission teams for rising seniors.
    """
    original_grid = sheet.get_values(
        new_file_ids.master, range_="A2:Z", sheets_service=sheets_service
    )
    cleared_committees = columns.clear_if(
        grid=original_grid,
        key_index=column_indexes.master["cohort"],
        key_values=[
            str(sophomore_cohort),
            str(sophomore_cohort - 1),
            str(senior_cohort),
        ],
        target_indexes=[column_indexes.master["committee"]],
    )
    cleared_mission_teams = columns.clear_if(
        grid=cleared_committees,
        key_index=column_indexes.master["cohort"],
        key_values=[str(senior_cohort)],
        target_indexes=[column_indexes.master["mt"]],
    )
    cleared_leadership_and_status = columns.clear(
        grid=cleared_mission_teams,
        target_indexes=[
            column_indexes.master["leadership"],
            column_indexes.master["status"],
        ],
    )
    sheet.update_values(
        spreadsheet_id=new_file_ids.master,
        range_="A2:Z",
        grid=cleared_leadership_and_status,
        sheets_service=sheets_service,
    )


def prompt_to_clear_remaining_old_data() -> None:
    """
    Prompt to clear data that cannot be safely deleted.
    """
    all_students_link = generate_link.gsheet(new_file_ids.participation["all_students"])
    no_shows_link = generate_link.gsheet(new_file_ids.participation["no_shows"])
    command_line.ask_confirmation(
        instructions=textwrap.dedent(
            f"""\
                The script is not able to safely delete some data, so you will have to do it.
                1. Open up the new 'All student attendance' sheet at {all_students_link}
                2. Erase the data on every tab except for 'Total attendance'. (Make sure the formulas are saved in the 'Formulas' tab.)
                3. Rename the tabs to the relevant events, e.g. "OLS 1" and "Fall Retreat".
                4. Go back to the tab 'All student attendance'. Confirm everyone has 0s.
                5. We don't want everyone to actually have 0s, because we haven't had the events yet. So, erase the formula in column 'Total attendance %'. 
                   After the event happens, go back and add the formula.
                6. Go to the new 'No shows' sheet at {no_shows_link}
                7. Erase the data under the tabs named after All-student Events, like 'OLS 3'. (Make sure the 'Formulas' tab.)
                8. Every student should have 0 on the 'Total no-shows' tab."""
        ),
        default_to_yes=True,
    )


# ------------------------------------------------------------------
# Mission team reshuffle
# ------------------------------------------------------------------


def reshuffle_mission_teams(sheets_service: discovery.Resource = None) -> None:
    """
    Ask if mission teams changed, then ask for new mappings and update master.
    """
    # check if reshuffled
    changed = command_line.ask_yes_no(
        question="Were mission teams reshuffled this semester?", default="no"
    )
    if not changed:
        return

    # get input
    def valid_mapping_input(answer: str) -> bool:
        valid_mt_number = r"(?:[1-9]|[1-2][0-9]|30)"
        valid_mapping = f"\\b{valid_mt_number}:{valid_mt_number}\\b\\s?"
        valid_input = f"^({valid_mapping})+$"
        return bool(re.match(valid_input, answer))

    new_mapping_input = command_line.ask_input(
        prompt=textwrap.dedent(
            """\
                            For every mission team that has changed, which team should people now be changed to?
                            
                            Enter in the format of old_mt_number:new_mt_number, as a list with spaces between entries.
                            For example, the input `1:4 8:5` means people originally on team 1 should now be team 4, and originally on team 8 should now be team 5.
                            """
        ),
        is_valid=valid_mapping_input,
    )
    new_mapping_list = [mapping.split(":") for mapping in new_mapping_input.split()]
    new_mappings = {
        mapping[0]: mapping[1] for mapping in new_mapping_list
    }  # original mt -> new mt
    # update values
    master_grid = sheet.get_values(
        new_file_ids.master, range_="Master!A2:Z", sheets_service=sheets_service
    )
    updated_grid = columns.update(
        grid=master_grid,
        key_index=column_indexes.master["mt"],
        target_index=column_indexes.master["mt"],
        overwrite=True,
        updated_values=new_mappings,
    )
    sheet.update_values(
        new_file_ids.master,
        range_="Master!A2:Z",
        grid=updated_grid,
        sheets_service=sheets_service,
    )


# ------------------------------------------------------------------
# Prepare leadership
# ------------------------------------------------------------------


def prompt_to_add_leadership() -> None:
    """
    Prompt to add leadership info to Master.
    """
    master_link = generate_link.gsheet(new_file_ids.master)
    command_line.ask_confirmation(
        instructions=textwrap.dedent(
            f"""\
            1. Open up the new master spreadsheet at {master_link}
            2. Add leadership roles to new leadership using the 'Leadership' column and its dropdown options.
            3. For mission team leaders, make sure their MT number reflects what they are leading. 
            4. For committee chairs, add their committee under the Committee column."""
        ),
        default_to_yes=True,
    )


@command_line.log(
    start_message="Setting up leadership roster.",
    end_message="Leadership roster set up.\n",
)
def prepare_leadership_roster(sheets_service: discovery.Resource) -> None:
    """
    Setup leadership roster with contact info.
    """
    master_grid = sheet.get_values(
        new_file_ids.master, range_="Master!A2:Z", sheets_service=sheets_service
    )
    filtered = rows.filter_out_blank(
        grid=master_grid, target_index=column_indexes.master["leadership"]
    )
    reordered = columns.reorder(
        grid=filtered,
        new_order=[
            column_indexes.master["asurite"],
            column_indexes.master["first"],
            column_indexes.master["last"],
            column_indexes.master["status"],
            column_indexes.master["email"],
            column_indexes.master["phone"],
            column_indexes.master["campus"],
            column_indexes.master["cohort"],
            column_indexes.master["leadership"],
            column_indexes.master["committee"],
            column_indexes.master["mt"],
        ],
    )
    without_status = columns.remove(grid=reordered, target_indexes=[3])
    # find specific position, e.g. MT 30
    Position = Union[str, int]
    Email = str

    def invert(d: Dict[Position, Email]) -> Dict[Email, Position]:
        return {email: position for position, email in d.items()}

    email_to_leadership_position = {
        **invert(new_leadership.committee_chairs),
        **invert(new_leadership.committee_leads),
        **invert(new_leadership.section_leads),
        **invert(new_leadership.mission_team_leaders),
    }
    with_specific_position = columns.update(
        grid=without_status,
        key_index=3,
        target_index=8,
        updated_values=email_to_leadership_position,
        overwrite=True,
    )
    # find sister group, e.g. Section 1 -> MT 1, 2, 3
    def find_sister(*, leadership_group: str, specific_position: Position) -> str:
        # TODO: these functions should be drawn into a dedicated file
        def find_mt_sister_section(mt_number: int) -> int:
            return math.ceil(mt_number / 3)

        def find_section_sister_mts(section_number: int) -> List[int]:
            return [mt_index + (3 * (section_number - 1)) for mt_index in range(1, 4)]

        def generate_mt_sister_section(mt_number: str) -> str:
            try:
                parsed_mt_number = int(mt_number)
            except ValueError:
                return ""
            else:
                section_number = find_mt_sister_section(parsed_mt_number)
                return str(section_number)

        def generate_section_sister_mts(section_number: str) -> str:
            try:
                parsed_section_number = int(section_number)
            except ValueError:
                return ""
            else:
                mt_numbers = find_section_sister_mts(parsed_section_number)
                return ", ".join(str(n) for n in mt_numbers)

        # TODO: add sister group for committee chairs and committee leads.
        # Will require changing the dropdown for master to "Committee Lead", rather than "Culture Lead" etc

        generator_func = {
            "MT Leader": generate_mt_sister_section,
            "Section Lead": generate_section_sister_mts,
        }.get(leadership_group, lambda _: "")
        return generator_func(specific_position)

    sister_column = [
        find_sister(leadership_group=row[7], specific_position=row[8])
        for row in with_specific_position
    ]
    with_sister_column = columns.replace(
        grid=with_specific_position, column=sister_column, target_index=9
    )

    headers = [
        [
            "ASUrite",
            "First name",
            "Last name",
            "Email",
            "Cell",
            "Campus",
            "Cohort",
            "Position",
            "Group",
            "Sister Group",
        ]
    ]
    with_headers = headers + with_sister_column
    # batch requests
    requests = [
        display.freeze_request(num_rows=1),
        display.auto_resize_request(),
        display.alternating_colors_request(),
    ]
    # send API requests
    sheet.update_values(
        new_file_ids.leadership_roster,
        range_="A1:Z",
        grid=with_headers,
        sheets_service=sheets_service,
    )
    sheet.batch_update(
        new_file_ids.leadership_roster, requests=requests, sheets_service=sheets_service
    )


# ------------------------------------------------------------------
# Prepare rosters
# ------------------------------------------------------------------


@command_line.log(start_message="Setting up rosters.", end_message="Rosters set up.\n")
def prepare_all_rosters(
    *,
    include_committees: bool = True,
    include_mission_teams: bool = True,
    add_colors: bool = True,
    sheets_service: discovery.Resource = None,
) -> None:
    """
    Setup every roster with data and formatting, pulling data from Master.
    """
    # setup sheets service
    if sheets_service is None:
        sheets_service = sheets_api.build_service()
    # feed master values
    master_grid = sheet.get_values(
        new_file_ids.master, range_="Master!A2:Z", sheets_service=sheets_service
    )
    prepare_new_roster = functools.partial(
        prepare_roster,
        master_grid=master_grid,
        add_colors=add_colors,
        sheets_service=sheets_service,
    )
    if include_mission_teams:
        for mt_number, mt_roster_id in new_file_ids.mission_team_attendance.items():
            prepare_new_roster(
                spreadsheet_id=mt_roster_id,
                subgroup_column_name="Squad",
                filter_column_index=column_indexes.master["mt"],
                filter_value=str(mt_number),
            )
    if include_committees:
        for committee, committee_roster_id in new_file_ids.committee_attendance.items():
            prepare_new_roster(
                spreadsheet_id=committee_roster_id,
                subgroup_column_name="Task force",
                filter_column_index=column_indexes.master["committee"],
                filter_value=committee,
            )


def prepare_roster(
    spreadsheet_id: str,
    *,
    filter_column_index: int,
    filter_value: str,
    master_grid: sheet.Grid,
    add_colors: bool = True,
    subgroup_column_name: str,
    sheets_service: discovery.Resource = None,
) -> None:
    """
    Setup provided roster's data and formatting.
    """
    # setup grid content
    filtered = rows.filter_by_cell(
        grid=master_grid, target_index=filter_column_index, target_values=[filter_value]
    )
    reordered = columns.reorder(
        grid=filtered,
        new_order=[
            column_indexes.master["asurite"],
            column_indexes.master["first"],
            column_indexes.master["last"],
            column_indexes.master["status"],
            column_indexes.master["email"],
            column_indexes.master["phone"],
            column_indexes.master["campus"],
            column_indexes.master["cohort"],
        ],
    )
    without_status = columns.remove(grid=reordered, target_indexes=[3])
    with_additional_rows = rows.append_blank(
        grid=without_status, num_rows=10, num_columns=8
    )
    participation_column = formulas.generate_adaptive_row_index(
        formula=sheet_formulas.roster_participation(),
        num_rows=len(with_additional_rows),
    )
    with_participation = columns.add(
        grid=with_additional_rows, column=participation_column, target_index=1
    )
    with_empty_subgroup_column = columns.add_blank(
        grid=with_participation, target_index=8
    )
    headers = [
        [
            "ASUrite",
            "Participation Rate",
            "First name",
            "Last name",
            "Email",
            "Cell",
            "Campus",
            "Cohort",
            subgroup_column_name,
            "Ex: 9/12",
        ]
    ]
    with_headers = headers + with_empty_subgroup_column
    # batch requests
    requests = [
        validation.dropdown_options_request(
            options=["yes", "no", "remote", "excused"],
            row_start_index=1,
            row_end_index=len(with_participation),
            column_start_index=9,
            column_end_index=25,
        ),
        validation.protected_range_request(
            editor_emails=new_leadership.drive_root_access,
            description="Participation formula",
            column_start_index=0,
            column_end_index=2,
        ),
        display.hide_columns_request(start_column_index=0, end_column_index=1),
        display.freeze_request(num_rows=1),
        display.auto_resize_request(),
        tab.rename_request(tab_name="Attendance"),
    ]
    if add_colors:  # will crash app if colors already added
        requests.append(display.alternating_colors_request())
    # send API requests
    sheet.update_values(
        spreadsheet_id, range_="A1:Z", grid=with_headers, sheets_service=sheets_service
    )
    sheet.batch_update(spreadsheet_id, requests=requests, sheets_service=sheets_service)


# ------------------------------------------------------------------
# Update important files like Master
# ------------------------------------------------------------------


@command_line.log(
    start_message="Updating formulas in Master.",
    end_message="Master formulas updated.\n",
)
def update_master_formulas(*, sheets_service: discovery.Resource = None) -> None:
    """
    Link master to all of the rosters and attendance sheets.
    """
    master_values = sheet.get_values(
        new_file_ids.master, range_="A2:Z", sheets_service=sheets_service
    )
    # generate columns
    generate_master_formula = functools.partial(
        formulas.generate_adaptive_row_index, num_rows=len(master_values)
    )
    civil_mil_column = generate_master_formula(
        formula=sheet_formulas.master_civil_mil(
            engagement_id=new_file_ids.participation["engagement"]
        )
    )
    hours_total_column = generate_master_formula(
        formula=sheet_formulas.master_hours_total(
            engagement_id=new_file_ids.participation["engagement"]
        )
    )
    service_column = generate_master_formula(
        formula=sheet_formulas.master_service(
            engagement_id=new_file_ids.participation["engagement"]
        )
    )
    ngsc_column = generate_master_formula(
        formula=sheet_formulas.master_ngsc(
            engagement_id=new_file_ids.participation["engagement"]
        )
    )
    committee_attendance_column = generate_master_formula(
        formula=sheet_formulas.master_committee_attendance(
            committee_id_map=new_file_ids.committee_attendance
        )
    )
    mt_attendance_column = generate_master_formula(
        formula=sheet_formulas.master_mt_attendance(
            mt_id_map=new_file_ids.mission_team_attendance
        )
    )
    all_student_column = generate_master_formula(
        formula=sheet_formulas.master_all_student(
            all_student_id=new_file_ids.participation["all_students"]
        )
    )
    no_show_column = generate_master_formula(
        formula=sheet_formulas.master_no_shows(
            no_shows_id=new_file_ids.participation["no_shows"]
        )
    )
    triggers_current_column = generate_master_formula(
        formula=sheet_formulas.master_triggers_current()
    )
    triggers_last_column = generate_master_formula(
        formula=sheet_formulas.master_triggers_earlier_semester(
            old_master_id=file_ids.master
        )
    )
    triggers_two_semesters_column = generate_master_formula(
        formula=sheet_formulas.master_triggers_earlier_semester(
            old_master_id=file_ids.master_prior_semester
        )
    )
    # update grid
    replace = {
        column_indexes.master["civil_mil"]: civil_mil_column,
        column_indexes.master["hours_total"]: hours_total_column,
        column_indexes.master["service"]: service_column,
        column_indexes.master["ngsc"]: ngsc_column,
        column_indexes.master["committee_attendance"]: committee_attendance_column,
        column_indexes.master["mt_attendance"]: mt_attendance_column,
        column_indexes.master["ols"]: all_student_column,
        column_indexes.master["no_shows"]: no_show_column,
        column_indexes.master["triggers_current"]: triggers_current_column,
        column_indexes.master["triggers_last"]: triggers_last_column,
        column_indexes.master["triggers_two_semesters"]: triggers_two_semesters_column,
    }
    result = columns.batch_replace(grid=master_values, columns_with_index=replace)
    sheet.update_values(
        new_file_ids.master, range_="A2:Z", grid=result, sheets_service=sheets_service
    )


# -------------------------------------
# Remaining steps
# -------------------------------------


def prompt_to_connect_master_links() -> None:
    """
    Prompt to connect Master to all the rosters and participation sheets.
    """
    master_link = generate_link.gsheet(new_file_ids.master)
    command_line.ask_confirmation(
        instructions=textwrap.dedent(
            f"""\
            1. Open up the new master spreadsheet at {master_link}
            2. Scroll to the right to the participation section.
            3. Highlight over cells with `#REF!` and press 'Allow access'.
            4. Continue to add access until there are no more `#REF!`s."""
        ),
        default_to_yes=True,
    )


def print_remaining_steps() -> None:
    semester_link = generate_link.folder(new_folder_ids.semester_root)
    print(
        textwrap.dedent(
            f"""\
        The semester's drive is set up! Bookmark the semester's folder at {semester_link}

        Once you are ready to share with new leadership, run `./ngsc share-drive`
        If you need to rebuild the rosters, e.g. when freshmen join the program, run `./ngsc rebuild-rosters`.

        Finally, you will need to copy all of the data under `backend/src/data/new_semester` into the files in `backend/src/data`.
        Only do this once the current semester is completely done, because it will change the data used by the web app.
        After you do this, run `./ngsc student-info`, deploy, and make sure the web app still works.
        """
        )
    )


if __name__ == "__main__":
    main()
