#!/usr/bin/env python3.6

"""
CLI script to setup the Google Drive for a new semester.

Should be run locally, not on the server.
"""
import os
import sys
from pathlib import Path

# path hack, https://chrisyeh96.github.io/2017/08/08/definitive-guide-python-imports.html
current_file_path = Path(os.path.realpath(__file__))
sys.path.append(str(current_file_path.parents[1]))
sys.path.append(str(current_file_path.parents[4]))

import pprint
import re
import functools
import textwrap
from typing import Dict, Union, NamedTuple

from googleapiclient import discovery

from scripts.utils import command_line
from backend.src.google_apis import drive_api, sheets_api
from backend.src.data import column_indexes, file_ids, folder_ids, sheet_formulas
from backend.src.data.new_semester import new_leadership, new_file_ids, new_folder_ids
from backend.src.drive_commands import copy, create, generate_link
from backend.src.sheets_commands import columns, display, formulas, sheet, validation, rows, tab

Semester = str
ResourceID = str
Key = Union[str, int]
IdMap = Dict[Key, Union[ResourceID, Dict[Key, ResourceID]]]


def main() -> None:
    print_debugging_tips()
    semester = ask_semester_target()
    # create api services
    drive_service = drive_api.build_service()
    sheets_service = sheets_api.build_service()
    # create resources
    folder_id_map = create_empty_folders(semester=semester,
                                         drive_service=drive_service)
    roster_ids = create_empty_rosters(folder_id_map=folder_id_map,
                                      semester=semester,
                                      drive_service=drive_service)
    important_files = copy_important_files(folder_id_map=folder_id_map,
                                           semester=semester,
                                           drive_service=drive_service)
    file_id_map = {**roster_ids, **important_files}
    # save to hardcoded files
    save_folder_ids(folder_id_map)
    save_file_ids(file_id_map)
    check_new_ids_different()
    # steps before adding data
    prompt_to_add_admin_email()
    prompt_to_update_leave_of_absence()
    # update ID lists
    update_participation_id_list(sheets_service=sheets_service)
    # clear old data
    clear_engagement_data(sheets_service=sheets_service)
    clear_no_show_data(sheets_service=sheets_service)
    rising_cohorts = ask_rising_cohorts()
    clear_required_committees_and_mt(sophomore_cohort=rising_cohorts.sophomores,
                                     senior_cohort=rising_cohorts.seniors,
                                     sheets_service=sheets_service)
    prompt_to_clear_remaining_old_data()
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
    print(textwrap.dedent('''\
        -------
        Disclaimer: this is a very long script with multiple potential points of failure.
        
        If the script fails prematurely, before the new IDs are saved to files, delete the Google Drive folder created and restart the script.
        
        If the new IDs are already saved to the `data/new_semester` folder, then, in this script itself, you can comment out the commands already done and restart the script.
        
        Potential sources of failure (non-exhaustive):
        - Column indexes were changed. Compare actual indexes with this script and `data/column_indexes`.
        - Tab names were changed. Compare to the formulas in `data/sheet_formulas`.
        - Occasionally Google's API server itself has failed, and the script simply needs to be run again.
        - `copy_important_files` fails because API is overloaded and does not create the accompanying forms quickly enough. Try changing the timeout.
        
        These should not be sources of error, but check just in case:
        - Changed file names. The scripts work by File IDs, instead of file names. 
        -------\n
    '''))


def ask_semester_target() -> str:
    """
    Ask CLI user for the target semester in correct format, e.g. 'Spring 2018'.
    """

    def is_valid_semester(answer: str) -> bool:
        words = answer.split()
        if len(words) != 2:
            return False
        prefix_is_semester = words[0] == 'Fall' or words[0] == 'Spring'
        postfix_is_year = bool(re.match('^(20)\d{2}$', words[1]))
        return prefix_is_semester and postfix_is_year

    return command_line.ask_input(
            prompt=textwrap.dedent('''\
                        What semester are you creating this for?
                        Enter in the format \'Spring 2018\', \'Fall 2023\'.'''),
            is_valid=is_valid_semester)


# ------------------------------------------------------------------
# Create resources
# ------------------------------------------------------------------

@command_line.log(start_message='Creating empty folders.',
                  end_message='Empty folders created\n')
def create_empty_folders(*,
                         semester: Semester,
                         drive_service: discovery.Resource = None) -> IdMap:
    """
    Set up the folder structure and return their IDs.
    """
    # setup drive service
    if drive_service is None:
        drive_service = drive_api.build_service()
    create_folder = functools.partial(create.folder,
                                      drive_service=drive_service)
    batch_create_folder = functools.partial(create.batch_folder,
                                            drive_service=drive_service)
    # Root level
    semester_root = create_folder(semester,
                                  parent_folder_id=folder_ids.drive_playground)  # TODO change to NGSC root when ready
    id_map = {
        'ngsc_root': folder_ids.ngsc_root,
        'drive_playground': folder_ids.drive_playground,
        'semester_root': semester_root
    }
    # Root subfolders
    root_subfolders = [
        drive_api.NameAndParent('Templates', semester_root),
        drive_api.NameAndParent('All students', semester_root),
        drive_api.NameAndParent('Leadership', semester_root),
        drive_api.NameAndParent('Sections', semester_root),
        drive_api.NameAndParent('Committees', semester_root),
    ]
    root_subfolders_ids = batch_create_folder(targets=root_subfolders)
    id_map.update({
        'templates': root_subfolders_ids[0],
        'all_students_root': root_subfolders_ids[1],
        'leadership_root': root_subfolders_ids[2],
        'sections_root': root_subfolders_ids[3],
        'committees_root': root_subfolders_ids[4],
    })
    # All students subfolders
    all_students_subfolders = [
        drive_api.NameAndParent('On Leadership', id_map['all_students_root']),
        drive_api.NameAndParent('Summit', id_map['all_students_root']),
        drive_api.NameAndParent('Participation', id_map['all_students_root']),
    ]
    all_students_subfolders_ids = batch_create_folder(targets=all_students_subfolders)
    id_map['all_students'] = {
        'on_leadership': all_students_subfolders_ids[0],
        'summit': all_students_subfolders_ids[1],
        'participation': all_students_subfolders_ids[2]
    }
    # Leadership subfolders
    briefings = create_folder('Staff Briefings',
                              parent_folder_id=id_map['leadership_root'])
    id_map['leadership'] = {
        'staff_briefings': briefings
    }
    # Sections folders
    section_folders = [drive_api.NameAndParent(f'Section {section_index}',
                                               parent_folder_id=id_map['sections_root'])
                       for section_index in range(1, 11)]
    section_folders_ids = batch_create_folder(targets=section_folders)
    id_map['sections'] = dict(zip(range(1, 11), section_folders_ids))
    # Mission team folders
    mission_team_folders_by_section = [[drive_api.NameAndParent(f'Mission team {mt_number}',
                                                                id_map['sections'][section_index])
                                        for mt_number in (mt_index + (3 * (section_index - 1))
                                                          for mt_index in range(1, 4))]
                                       for section_index in range(1, 11)]
    mission_team_folders_flattened = [mt for section in mission_team_folders_by_section
                                      for mt in section]
    mission_team_folders_ids = batch_create_folder(targets=mission_team_folders_flattened)
    id_map['mission_teams'] = dict(zip(range(1, 31), mission_team_folders_ids))
    # Committee Leads
    committee_leads_folders = [
        drive_api.NameAndParent('Engagement', id_map['committees_root']),
        drive_api.NameAndParent('Education', id_map['committees_root']),
        drive_api.NameAndParent('Culture', id_map['committees_root'])
    ]
    committee_leads_folders_ids = batch_create_folder(targets=committee_leads_folders)
    id_map['committee_leads'] = {
        'Engagement': committee_leads_folders_ids[0],
        'Education': committee_leads_folders_ids[1],
        'Culture': committee_leads_folders_ids[2]
    }
    # Committee Chairs
    committee_chairs_folders = [
        drive_api.NameAndParent('Admin', id_map['committees_root']),
        drive_api.NameAndParent('Transfers', id_map['committee_leads']['Engagement']),
        drive_api.NameAndParent('Civil-Mil', id_map['committee_leads']['Engagement']),
        drive_api.NameAndParent('Service', id_map['committee_leads']['Engagement']),
        drive_api.NameAndParent('Training', id_map['committee_leads']['Education']),
        drive_api.NameAndParent('Mentorship', id_map['committee_leads']['Education']),
        drive_api.NameAndParent('Ambassadors', id_map['committee_leads']['Education']),
        drive_api.NameAndParent('Communications', id_map['committee_leads']['Culture']),
        drive_api.NameAndParent('Events', id_map['committee_leads']['Culture']),
        drive_api.NameAndParent('Social', id_map['committee_leads']['Culture']),
    ]
    committee_chairs_folders_ids = batch_create_folder(targets=committee_chairs_folders)
    id_map['committees'] = {
        'Admin': committee_chairs_folders_ids[0],
        'Transfers': committee_chairs_folders_ids[1],
        'Civil-Mil': committee_chairs_folders_ids[2],
        'Service': committee_chairs_folders_ids[3],
        'Training': committee_chairs_folders_ids[4],
        'Mentorship': committee_chairs_folders_ids[5],
        'Ambassadors': committee_chairs_folders_ids[6],
        'Communications': committee_chairs_folders_ids[7],
        'Events': committee_chairs_folders_ids[8],
        'Social': committee_chairs_folders_ids[9]
    }
    return id_map


@command_line.log(start_message='Creating empty rosters.',
                  end_message='Empty rosters created\n')
def create_empty_rosters(*,
                         folder_id_map: IdMap,
                         semester: Semester,
                         drive_service: discovery.Resource = None) -> IdMap:
    """
    Create the roster spreadsheets (not set up) and save their IDs.
    """
    # setup drive service
    if drive_service is None:
        drive_service = drive_api.build_service()
    batch_create_gsheet = functools.partial(create.batch_gsheet,
                                            drive_service=drive_service)
    # Committee rosters
    committee_rosters = [drive_api.NameAndParent(name=f'Attendance - {committee} - {semester}',
                                                 parent_folder_id=folder_id)
                         for committee, folder_id
                         in folder_id_map['committees'].items()]
    committee_roster_ids = batch_create_gsheet(targets=committee_rosters)
    committee_file_dict = dict(zip(folder_id_map['committees'].keys(), committee_roster_ids))
    # Mission team rosters
    mission_team_rosters = [drive_api.NameAndParent(name=f'Attendance - Mission Team {mt_number} - {semester}',
                                                    parent_folder_id=folder_id)
                            for mt_number, folder_id
                            in folder_id_map['mission_teams'].items()]
    mission_team_roster_ids = batch_create_gsheet(targets=mission_team_rosters)
    mission_team_file_dict = dict(zip(folder_id_map['mission_teams'].keys(), mission_team_roster_ids))
    return {
        'committee_attendance': committee_file_dict,
        'mission_team_attendance': mission_team_file_dict
    }


@command_line.log(start_message='Copying important files.',
                  end_message='Important files copied.\n')
def copy_important_files(*,
                         folder_id_map: IdMap,
                         semester: Semester,
                         drive_service: discovery.Resource = None) -> IdMap:
    """
    Copy the Master, schedule, all-student attendance, no shows, & templates.
    """
    id_map = {}
    if drive_service is None:
        drive_service = drive_api.build_service()
    # master
    master = copy.file(origin_file_id=file_ids.master,
                       target_parent_folder_id=folder_id_map['semester_root'],
                       new_name=f'Master - {semester}',
                       drive_service=drive_service)
    id_map['master'] = master
    id_map['master_prior_semester'] = file_ids.master
    # schedule
    schedule = copy.file(origin_file_id=file_ids.schedule,
                         target_parent_folder_id=folder_id_map['semester_root'],
                         new_name=f'Schedule - {semester}',
                         drive_service=drive_service)
    id_map['schedule'] = schedule
    # participation
    all_students = copy.file(origin_file_id=file_ids.participation['all_students'],
                             target_parent_folder_id=folder_id_map['all_students']['participation'],
                             new_name=f'All student attendance - {semester}',
                             drive_service=drive_service)
    engagement = copy.linked_sheet_and_form(origin_sheet_id=file_ids.participation['engagement'],
                                            origin_form_id=file_ids.participation['engagement_form'],
                                            origin_parent_folder_id=folder_ids.all_students['participation'],
                                            new_sheet_name=f'Engagement - {semester}',
                                            new_form_name=f'Engagement - {semester}',
                                            target_parent_folder_id=folder_id_map['all_students']['participation'],
                                            drive_service=drive_service,
                                            initial_form_search_delay=20,
                                            timeout=120)
    no_shows = copy.linked_sheet_and_form(origin_sheet_id=file_ids.participation['no_shows'],
                                          origin_form_id=file_ids.participation['no_shows_form'],
                                          origin_parent_folder_id=folder_ids.all_students['participation'],
                                          new_sheet_name=f'No shows - {semester}',
                                          new_form_name=f'No shows - {semester}',
                                          target_parent_folder_id=folder_id_map['all_students']['participation'],
                                          drive_service=drive_service,
                                          initial_form_search_delay=20,
                                          timeout=120)
    id_map['participation'] = {
        'all_students': all_students,
        'engagement': engagement.sheet,
        'engagement_form': engagement.form,
        'no_shows': no_shows.sheet,
        'no_shows_form': no_shows.form
    }
    # templates
    rsvp = copy.file(origin_file_id=file_ids.templates['rsvp'],
                     target_parent_folder_id=folder_id_map['templates'],
                     new_name='RSVP Template',
                     drive_service=drive_service)
    initial_meeting = copy.file(origin_file_id=file_ids.templates['initial_meeting'],
                                target_parent_folder_id=folder_id_map['templates'],
                                new_name='Initial meeting template',
                                drive_service=drive_service)
    event_proposal = copy.file(origin_file_id=file_ids.templates['event_proposal'],
                               target_parent_folder_id=folder_id_map['templates'],
                               new_name='Event proposal template',
                               drive_service=drive_service)
    ols_cancel_rsvp = copy.file(origin_file_id=file_ids.templates['ols_cancel_rsvp'],
                                target_parent_folder_id=folder_id_map['templates'],
                                new_name='OLS cancel RSVP template',
                                drive_service=drive_service)
    id_map['templates'] = {
        'rsvp': rsvp,
        'initial_meeting': initial_meeting,
        'event_proposal': event_proposal,
        'ols_cancel_rsvp': ols_cancel_rsvp
    }
    return id_map


# ------------------------------------------------------------------
# Save IDs to hardcoded files.
# ------------------------------------------------------------------

@command_line.log(end_message='Folder IDs saved to `backend/src/data/new_semester/new_folder_ids.py`.\n')
def save_folder_ids(ids: IdMap) -> None:
    """
    Write the given folder IDs to the file `data/folder_ids.py`.
    """
    output = _format_id_output(ids)
    with open('backend/src/data/new_semester/new_folder_ids.py', 'w') as file:
        file.writelines(output)


@command_line.log(end_message='File IDs saved to `backend/src/data/new_semester/new_file_ids.py`.\n')
def save_file_ids(ids: IdMap) -> None:
    """
    Write the given file IDs to the file `data/file_ids.py`.
    """
    output = _format_id_output(ids)
    with open('backend/src/data/new_semester/new_file_ids.py', 'w') as file:
        file.writelines(output)


@command_line.log(
        start_message='Checking new IDs are different than current IDs so that the script doesn\'t overwrite current data.',
        end_message='IDs are different. Safe to continue.')
def check_new_ids_different() -> None:
    """
    Check new and old file & folder IDs are different.
    """
    files_different = (file_ids.master != new_file_ids.master) \
                      and (file_ids.master_prior_semester != new_file_ids.master_prior_semester) \
                      and (file_ids.committee_attendance != new_file_ids.committee_attendance) \
                      and (file_ids.mission_team_attendance != new_file_ids.mission_team_attendance) \
                      and (file_ids.participation != new_file_ids.participation) \
                      and (file_ids.templates != new_file_ids.templates) \
                      and (file_ids.schedule != new_file_ids.schedule)
    if not files_different:
        raise SystemExit('At least one new file ID is the same as a current file ID. Aborting script.')
    folders_different = (folder_ids.semester_root != new_folder_ids.semester_root) \
                        and (folder_ids.all_students != folder_ids.all_students) \
                        and (folder_ids.committee_chair_folders != folder_ids.committee_chair_folders) \
                        and (folder_ids.committee_lead_folders != folder_ids.committee_lead_folders) \
                        and (folder_ids.section_folders != folder_ids.section_folders) \
                        and (folder_ids.mission_team_folders != folder_ids.mission_team_folders)
    if not files_different:
        raise SystemExit('At least one new folder ID is the same as the current file IDs. Aborting script.')


def _format_id_output(ids: IdMap) -> str:
    """
    Convert ID dict to output as variables separated by newlines.
    """
    variable_syntax = [f'{k} = \'{v}\'' if isinstance(v, str)
                       else f'{k} = {pprint.pformat(v)}'
                       for k, v in ids.items()]
    return '\n\n'.join(variable_syntax)


# ------------------------------------------------------------------
# Steps before adding data
# ------------------------------------------------------------------

def prompt_to_add_admin_email() -> None:
    """
    Make sure new admin chair added to leadership data file. Necessary for preparing rosters.
    """
    command_line.ask_confirmation(question=textwrap.dedent('''\
            1. Open up the file `backend/src/data/new_semester/new_leadership.py`. 
            2. Add the emails for the new Admin Chair, Chief of Staff, and staff.'''),
                                  default_to_yes=True)


def prompt_to_update_leave_of_absence() -> None:
    """
    Prompt to transfer students on leave of absence back into Master spreadsheet.
    """
    master_link = generate_link.gsheet(new_file_ids.master)
    command_line.ask_confirmation(question=textwrap.dedent(f'''\
            1. Open up the new master spreadsheet at {master_link}
            2. Select the tab \'Leave of absence\'.
            3. Transfer any students who will be back during the upcoming semester back to the \'Master\' tab.'''),
                                  default_to_yes=True)


# ------------------------------------------------------------------
# Update Participation ID lists
# ------------------------------------------------------------------

@command_line.log(start_message='Updating ID lists for participation spreadsheets.',
                  end_message='ID lists updated.')
def update_participation_id_list(*, sheets_service: discovery.Resource = None) -> None:
    """
    Re-pull the list of student IDs for All Student Attendance, No Shows, and Engagement.
    """
    student_ids = sheet.get_values(spreadsheet_id=new_file_ids.master,
                                   range_='Master!C2:C',
                                   sheets_service=sheets_service)
    update_student_id_list = functools.partial(sheet.update_values,
                                               range_='Total!A2:A',
                                               grid=student_ids,
                                               sheets_service=sheets_service)
    update_student_id_list(spreadsheet_id=new_file_ids.participation['engagement'])
    update_student_id_list(spreadsheet_id=new_file_ids.participation['no_shows'])
    update_student_id_list(spreadsheet_id=new_file_ids.participation['engagement'])


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
        return bool(re.match('^[1-9][0-9]?$', answer))

    sophomore = command_line.ask_input(
            prompt=textwrap.dedent('''\
                        Which cohort are the rising sophomores?
                        Enter as a whole number.'''),
            is_valid=is_valid_cohort)
    senior = command_line.ask_input(
            prompt=textwrap.dedent('''\
                        Which cohort are the rising seniors?
                        Enter as a whole number.'''),
            is_valid=is_valid_cohort)
    return RisingCohorts(sophomores=int(sophomore),
                         seniors=int(senior))


@command_line.log(start_message='Clearing engagement data.',
                  end_message='Engagement data cleared.\n')
def clear_engagement_data(*, sheets_service: discovery.Resource = None) -> None:
    """
    Remove last semester's submissions.
    """
    original_grid = sheet.get_values(new_file_ids.participation['engagement'],
                                     range_='Responses!A2:Z',
                                     sheets_service=sheets_service)
    cleared_grid = columns.clear(grid=original_grid,
                                 target_indexes=list(range(30)))
    sheet.update_values(spreadsheet_id=new_file_ids.participation['engagement'],
                        range_='Responses!A2:Z',
                        grid=cleared_grid,
                        sheets_service=sheets_service)


@command_line.log(start_message='Clearing no-show form data.',
                  end_message='No-show form data cleared.\n')
def clear_no_show_data(*, sheets_service: discovery.Resource = None) -> None:
    """
    Remove last semester's submissions.
    """
    original_grid = sheet.get_values(new_file_ids.participation['no_shows'],
                                     range_="'Form events'!A2:BU",
                                     sheets_service=sheets_service)
    cleared_grid = columns.clear(grid=original_grid,
                                 target_indexes=list(range(70)))
    sheet.update_values(spreadsheet_id=new_file_ids.participation['no_shows'],
                        range_="'Form events'!A2:BU",
                        grid=cleared_grid,
                        sheets_service=sheets_service)


@command_line.log(
        start_message='Clearing required committees for rising sophomores and mission teams for rising seniors.',
        end_message='Cleared required committees and mission teams.\n')
def clear_required_committees_and_mt(*,
                                     sophomore_cohort: int,
                                     senior_cohort: int,
                                     sheets_service: discovery.Resource = None) -> None:
    """
    Remove committees for rising sophomores and mission teams for rising seniors.
    """
    original_grid = sheet.get_values(new_file_ids.master,
                                     range_='A2:Z',
                                     sheets_service=sheets_service)
    cleared_committees = columns.clear_if(grid=original_grid,
                                          key_index=column_indexes.master['cohort'],
                                          key_values=[str(sophomore_cohort)],
                                          target_indexes=[column_indexes.master['committee']])
    cleared_mission_teams = columns.clear_if(grid=cleared_committees,
                                             key_index=column_indexes.master['cohort'],
                                             key_values=[str(senior_cohort)],
                                             target_indexes=[column_indexes.master['mt']])
    sheet.update_values(spreadsheet_id=new_file_ids.master,
                        range_='A2:Z',
                        grid=cleared_mission_teams,
                        sheets_service=sheets_service)


def prompt_to_clear_remaining_old_data() -> None:
    """
    Prompt to clear data that cannot be safely deleted.
    """
    all_students_link = generate_link.gsheet(new_file_ids.participation['all_students'])
    no_shows_link = generate_link.gsheet(new_file_ids.participation['no_shows'])
    command_line.ask_confirmation(question=textwrap.dedent(f'''\
                Some of the data cannot be safely deleted from the script, so you will have to do it.
                1. Open up the new 'All student attendance' sheet at {all_students_link}
                2. Erase the data on every tab except for 'Total attendance'. (Make sure the formulas are saved in the 'Formulas' tab.)
                3. Rename the tabs to the relevant events, e.g. "OLS 1" and "Fall Retreat".
                4. Go back to the tab 'All student attendance'. Confirm everyone has 0s.
                5. We don't want everyone to actually have 0s, because we haven't had the events yet. So, erase the formula in column 'Total attendance %'. 
                   After the event happens, go back and add the formula.
                6. Go to the new 'No shows' sheet at {no_shows_link}
                7. Erase the data under the tabs named after All-student Events, like 'OLS 3'. (Make sure the 'Formulas' tab.)
                8. Every student should have 0 on the 'Total no-shows' tab.'''),
                                  default_to_yes=True)


# ------------------------------------------------------------------
# Prepare rosters
# ------------------------------------------------------------------

@command_line.log(start_message='Setting up rosters.',
                  end_message='Rosters set up.\n')
def prepare_all_rosters(*,
                        include_committees: bool = True,
                        include_mission_teams: bool = True,
                        add_colors: bool = True,
                        sheets_service: discovery.Resource = None) -> None:
    """
    Setup every roster with data and formatting, pulling data from Master.
    """
    if sheets_service is None:
        sheets_service = sheets_api.build_service()
    master_grid = sheet.get_values(new_file_ids.master,
                                   range_='Master!A2:Z',
                                   sheets_service=sheets_service)
    if include_mission_teams:
        for mt_number, mt_roster_id in new_file_ids.mission_team_attendance.items():
            prepare_roster(spreadsheet_id=mt_roster_id,
                           filter_column_index=column_indexes.master['mt'],
                           filter_value=str(mt_number),
                           master_grid=master_grid,
                           add_colors=add_colors,
                           sheets_service=sheets_service)
    if include_committees:
        for committee, committee_roster_id in new_file_ids.committee_attendance.items():
            prepare_roster(spreadsheet_id=committee_roster_id,
                           filter_column_index=column_indexes.master['committee'],
                           filter_value=committee,
                           master_grid=master_grid,
                           add_colors=add_colors,
                           sheets_service=sheets_service)


def prepare_roster(spreadsheet_id: str, *,
                   filter_column_index: int,
                   filter_value: str,
                   master_grid: sheet.Grid,
                   add_colors: bool = True,
                   sheets_service: discovery.Resource = None) -> None:
    """
    Setup provided roster's data and formatting.
    """
    # add data
    filtered = rows.filter_by_cell(grid=master_grid,
                                   target_index=filter_column_index,
                                   target_value=filter_value)
    reordered = columns.reorder(grid=filtered,
                                new_order=[column_indexes.master['id'],
                                           column_indexes.master['first'],
                                           column_indexes.master['last'],
                                           column_indexes.master['status'],
                                           column_indexes.master['email'],
                                           column_indexes.master['phone'],
                                           column_indexes.master['campus'],
                                           column_indexes.master['cohort']])
    without_status = columns.remove(grid=reordered, target_indexes=[3])
    with_additional_rows = rows.append_blank(grid=without_status,
                                             num_rows=10,
                                             num_columns=8)
    # add participation formula
    participation_column = formulas.generate_adaptive_row_index(formula=sheet_formulas.roster_participation(),
                                                                num_rows=len(with_additional_rows))
    with_participation = columns.add(grid=with_additional_rows, column=participation_column, target_index=1)
    # add header row
    headers = [['ASUrite',
                'Participation Rate',
                'First name',
                'Last name',
                'Email',
                'Cell',
                'Campus',
                'Cohort',
                'Ex: 9/12']]
    with_headers = headers + with_participation
    # add attendance dropdown
    attendance_options = ['yes', 'no', 'remote', 'excused']
    dropdown_request = validation.dropdown_options_request(options=attendance_options,
                                                           row_start_index=1,
                                                           row_end_index=len(with_participation),
                                                           column_start_index=8,
                                                           column_end_index=25)
    # lock first 2 columns
    protected_range_request = validation.protected_range_request(editor_emails=new_leadership.drive_root_access,
                                                                 description='Participation formula',
                                                                 column_start_index=0,
                                                                 column_end_index=2)
    # modify display
    hide_request = display.hide_columns_request(start_column_index=0, end_column_index=1)
    freeze_request = display.freeze_request(num_rows=1)
    resize_request = display.auto_resize_request()
    colors_request = display.alternating_colors_request()
    # rename tab
    rename_request = tab.rename_request(tab_name='Attendance')
    # collate requests
    requests = [dropdown_request,
                protected_range_request,
                hide_request,
                freeze_request,
                resize_request,
                rename_request]
    if add_colors:  # will crash app if colors already added
        requests.append(colors_request)
    # send API requests
    sheet.update_values(spreadsheet_id,
                        range_='A1:Z',
                        grid=with_headers,
                        sheets_service=sheets_service)
    sheet.batch_update(spreadsheet_id,
                       requests=requests,
                       sheets_service=sheets_service)


# ------------------------------------------------------------------
# Update important files like Master
# ------------------------------------------------------------------

@command_line.log(start_message='Updating formulas in Master.',
                  end_message='Master formulas updated.\n')
def update_master_formulas(*, sheets_service: discovery.Resource = None) -> None:
    """
    Link master to all of the rosters and attendance sheets.
    """
    master_values = sheet.get_values(new_file_ids.master,
                                     range_='A2:Z',
                                     sheets_service=sheets_service)
    # generate columns
    generate_master_formula = functools.partial(formulas.generate_adaptive_row_index,
                                                num_rows=len(master_values))
    service_column = generate_master_formula(
            formula=sheet_formulas.master_service(engagement_id=new_file_ids.participation['engagement']))
    civil_mil_column = generate_master_formula(
            formula=sheet_formulas.master_civil_mil(engagement_id=new_file_ids.participation['engagement']))
    committee_attendance_column = generate_master_formula(
            formula=sheet_formulas.master_committee_attendance(committee_id_map=new_file_ids.committee_attendance))
    mt_attendance_column = generate_master_formula(
            formula=sheet_formulas.master_mt_attendance(mt_id_map=new_file_ids.mission_team_attendance))
    all_student_column = generate_master_formula(
            formula=sheet_formulas.master_all_student(all_student_id=new_file_ids.participation['all_students']))
    no_show_column = generate_master_formula(
            formula=sheet_formulas.master_no_shows(no_shows_id=new_file_ids.participation['no_shows']))
    triggers_current_column = generate_master_formula(
            formula=sheet_formulas.master_triggers_current())
    triggers_last_column = generate_master_formula(
            formula=sheet_formulas.master_triggers_earlier_semester(old_master_id=file_ids.master))
    triggers_two_semesters_column = generate_master_formula(
            formula=sheet_formulas.master_triggers_earlier_semester(old_master_id=file_ids.master_prior_semester))
    # update grid
    result = columns.replace(grid=master_values,
                             column=service_column,
                             target_index=column_indexes.master['service'])
    result = columns.replace(grid=result,
                             column=civil_mil_column,
                             target_index=column_indexes.master['civil-mil'])
    result = columns.replace(grid=result,
                             column=committee_attendance_column,
                             target_index=column_indexes.master['committee_attendance'])
    result = columns.replace(grid=result,
                             column=mt_attendance_column,
                             target_index=column_indexes.master['mt_attendance'])
    result = columns.replace(grid=result,
                             column=all_student_column,
                             target_index=column_indexes.master['ols'])
    result = columns.replace(grid=result,
                             column=no_show_column,
                             target_index=column_indexes.master['no_shows'])
    result = columns.replace(grid=result,
                             column=triggers_current_column,
                             target_index=column_indexes.master['triggers_current'])
    result = columns.replace(grid=result,
                             column=triggers_last_column,
                             target_index=column_indexes.master['triggers_last'])
    result = columns.replace(grid=result,
                             column=triggers_two_semesters_column,
                             target_index=column_indexes.master['triggers_two_semesters'])
    sheet.update_values(new_file_ids.master,
                        range_='A2:Z',
                        grid=result,
                        sheets_service=sheets_service)


# -------------------------------------
# Remaining steps
# -------------------------------------

def prompt_to_connect_master_links() -> None:
    """
    Prompt to connect Master to all the rosters and participation sheets.
    """
    master_link = generate_link.gsheet(new_file_ids.master)
    command_line.ask_confirmation(question=textwrap.dedent(f'''\
            1. Open up the new master spreadsheet at {master_link}
            2. Scroll to the right to the participation section.
            3. Highlight over cells with `#REF!` and press 'Allow access'.
            4. Continue to add access until there are no more `#REF!`s.'''),
                                  default_to_yes=True)


def print_remaining_steps() -> None:
    semester_link = generate_link.folder(new_folder_ids.semester_root)
    print(textwrap.dedent(f'''\
        The semester's drive is set up! Check {semester_link}

        Once you are ready to share with new leadership, run `./run.py share-drive`
        If you need to rebuild the rosters, e.g. when freshmen join the program, run `./run.py rebuild-rosters`.

        Finally, you will need to copy all of the data under `backend/src/data/new_semester` 
        Only do this once the current semester is completely done, because it will change the links used by the web app.
        After you do this, run `./run.py student-info`, deploy, and make sure the web app still works.
        '''))


# -------------------------------------
# Run script
# -------------------------------------

if __name__ == '__main__':
    main()
