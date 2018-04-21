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
from typing import Dict, Union, Tuple

from scripts.utils import command_line
from backend.src.data import column_indexes, file_ids, folder_ids, sheet_formulas
from backend.src.data.new_semester import new_leadership, new_file_ids, new_folder_ids
from backend.src.drive_commands import copy, create, find, rename, move, generate_link
from backend.src.sheets_commands import columns, display, formulas, sheet, validation, rows, tab

Semester = str
ResourceID = str
Key = Union[str, int]
IdMap = Dict[Key, Union[ResourceID, Dict[Key, ResourceID]]]


def main() -> None:
    semester = ask_semester_target()
    # create resources
    folder_id_map = create_empty_folders(semester)
    roster_ids = create_empty_rosters(folder_id_map, semester)
    important_files = copy_important_files(folder_id_map, semester)
    file_id_map = {**roster_ids, **important_files}
    # save to hardcoded files
    save_folder_ids(folder_id_map)
    save_file_ids(file_id_map)
    # clear old data
    clear_engagement_data(engagement_file_id=file_id_map['participation']['engagement'])
    clear_no_show_data(no_show_file_id=file_id_map['participation']['no_shows'])
    clear_all_student_attendance_data(all_student_file_id=file_id_map['participation']['on_leadership'])
    sophomore_cohort, senior_cohort = ask_rising_cohorts()
    clear_required_committees_and_mt(master_file_id=file_id_map['master'],
                                     senior_cohort=senior_cohort,
                                     sophomore_cohort=sophomore_cohort)
    # steps before preparing rosters
    prompt_to_add_admin_email()
    prompt_to_update_leave_of_absence()
    # prepare files
    prepare_all_rosters(file_id_map)
    update_master_formulas()
    # remaining steps
    prompt_to_connect_master_links()
    print_remaining_steps()


# ------------------------------------------------------------------
# CLI
# ------------------------------------------------------------------

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
                        Enter in the format \'Spring 2018\', \'Fall 2019\'.'''),
            is_valid=is_valid_semester)


def ask_rising_cohorts() -> Tuple[int, int]:
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
    return int(sophomore), int(senior)


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


# ------------------------------------------------------------------
# Create resources
# ------------------------------------------------------------------

@command_line.log(start_message='Creating empty folders.',
                  end_message='Empty folders created\n')
def create_empty_folders(semester: Semester) -> IdMap:
    """
    Set up the folder structure and return their IDs.
    """
    # NGSC root level
    id_map = {
        'ngsc_root': folder_ids.ngsc_root,
        'drive_playground': folder_ids.drive_playground
    }
    # Semester root
    root = create.folder(semester)
    id_map['semester_root'] = root
    # Templates
    templates = create.folder('Templates', parent_folder_id=root)
    id_map['templates'] = templates
    # All students
    all_students = create.folder('All students', parent_folder_id=root)
    id_map['all_students_root'] = all_students
    on_leadership = create.folder('On Leadership', parent_folder_id=all_students)
    summit = create.folder('Summit', parent_folder_id=all_students)
    participation = create.folder('Participation', parent_folder_id=all_students)
    id_map['all_students'] = {
        'on_leadership': on_leadership,
        'summit': summit,
        'participation': participation
    }
    # Leadership
    leadership = create.folder('Leadership', parent_folder_id=root)
    id_map['leadership_root'] = leadership
    briefings = create.folder('Staff Briefings', parent_folder_id=leadership)
    id_map['leadership'] = {
        'staff_briefings': briefings
    }
    # Sections & MTs
    sections = create.folder('Sections', parent_folder_id=root)
    id_map['sections_root'] = sections
    id_map['sections'] = {}
    id_map['mission_teams'] = {}
    for section_index in range(1, 11):
        section_folder_id = create.folder(f'Section {section_index}', parent_folder_id=sections)
        id_map['sections'][section_index] = section_folder_id
        for mt_index in range(1, 4):
            mt_number = mt_index + (3 * (section_index - 1))
            mt_folder_id = create.folder(f'Mission Team {mt_number}', parent_folder_id=section_folder_id)
            id_map['mission_teams'][mt_number] = mt_folder_id
    # Committees
    committees = create.folder('Committees', parent_folder_id=root)
    id_map['committees_root'] = committees
    # Committee Leads
    engagement = create.folder('Engagement', parent_folder_id=committees)
    education = create.folder('Education', parent_folder_id=committees)
    culture = create.folder('Culture', parent_folder_id=committees)
    id_map['committee_leads'] = {
        'engagement': engagement,
        'education': education,
        'culture': culture
    }
    # Committee Chairs
    admin = create.folder('Admin', parent_folder_id=committees)
    transfers = create.folder('Transfers', parent_folder_id=engagement)
    civil_mil = create.folder('Civil-Mil', parent_folder_id=engagement)
    service = create.folder('Service', parent_folder_id=engagement)
    training = create.folder('Training', parent_folder_id=education)
    mentorship = create.folder('Mentorship', parent_folder_id=education)
    ambassadors = create.folder('Ambassadors', parent_folder_id=education)
    communications = create.folder('Communications', parent_folder_id=culture)
    events = create.folder('Events', parent_folder_id=culture)
    social = create.folder('Social', parent_folder_id=culture)
    id_map['committees'] = {
        'Admin': admin,
        'Transfers': transfers,
        'Civil-Mil': civil_mil,
        'Service': service,
        'Training': training,
        'Mentorship': mentorship,
        'Ambassadors': ambassadors,
        'Communications': communications,
        'Events': events,
        'Social': social
    }
    return id_map


@command_line.log(start_message='Creating empty rosters.',
                  end_message='Empty rosters created\n')
def create_empty_rosters(folder_id_map: IdMap, semester: Semester) -> IdMap:
    """
    Create the roster spreadsheets (not set up) and save their IDs.
    """
    id_map = {
        'committee_attendance': {},
        'mission_team_attendance': {}
    }
    # Committee rosters
    for committee, committee_folder_id in folder_id_map['committees'].items():
        committee_roster_id = create.gsheet(file_name=f'Attendance - {committee} - {semester}',
                                            parent_folder_id=committee_folder_id)
        id_map['committee_attendance'][committee] = committee_roster_id
    # Mission team rosters
    for mt_number, mt_folder_id in folder_id_map['mission_teams'].items():
        mt_roster_id = create.gsheet(file_name=f'Attendance - Mission Team {mt_number} - {semester}',
                                     parent_folder_id=mt_folder_id)
        id_map['mission_team_attendance'][mt_number] = mt_roster_id
    return id_map


@command_line.log(start_message='Copying important files.',
                  end_message='Important files copied.\n')
def copy_important_files(folder_id_map: IdMap, semester: Semester) -> IdMap:
    """
    Copy the Master, schedule, all-student attendance, no shows, & templates.
    """
    id_map = {}
    # master
    master = copy.file(origin_file_id=file_ids.master,
                       parent_folder_id=folder_id_map['semester_root'],
                       copy_name=f'Master - {semester}')
    id_map['master'] = master
    id_map['master_prior_semester'] = file_ids.master
    # schedule
    schedule = copy.file(origin_file_id=file_ids.schedule,
                         parent_folder_id=folder_id_map['semester_root'],
                         copy_name=f'Schedule - {semester}')
    id_map['schedule'] = schedule
    # participation
    all_students = copy.file(origin_file_id=file_ids.participation['all_students'],
                             parent_folder_id=folder_id_map['all_students']['participation'],
                             copy_name=f'All student attendance - {semester}')
    engagement = copy.file(origin_file_id=file_ids.participation['engagement'],
                           parent_folder_id=folder_id_map['all_students']['participation'],
                           copy_name=f'Engagement - {semester}')
    engagement_form = find.gform(file_name='Copy of Engagement - ',
                                 parent_folder_id=folder_ids.all_students['participation'],
                                 exact_match=False)
    rename.file(file_id=engagement_form, new_name=f'Engagement - {semester}')
    move.file(origin_file_id=engagement_form, target_folder_id=folder_id_map['all_students']['participation'])
    no_shows = copy.file(origin_file_id=file_ids.participation['no_shows'],
                         parent_folder_id=folder_id_map['all_students']['participation'],
                         copy_name=f'No shows - {semester}')
    no_shows_form = find.gform(file_name='Copy of No shows - ',
                               parent_folder_id=folder_ids.all_students['participation'],
                               exact_match=False)
    rename.file(file_id=engagement_form, new_name=f'No shows - {semester}')
    move.file(origin_file_id=engagement_form, target_folder_id=folder_id_map['all_students']['participation'])
    id_map['participation'] = {
        'all_students': all_students,
        'engagement': engagement,
        'engagement_form': engagement_form,
        'no_shows': no_shows,
        'no_shows_form': no_shows_form
    }
    # templates
    rsvp = copy.file(origin_file_id=file_ids.templates['rsvp'],
                     parent_folder_id=folder_id_map['templates'],
                     copy_name='RSVP Template')
    initial_meeting = copy.file(origin_file_id=file_ids.templates['initial_meeting'],
                                parent_folder_id=folder_id_map['templates'],
                                copy_name='Initial meeting template')
    event_proposal = copy.file(origin_file_id=file_ids.templates['event_proposal'],
                               parent_folder_id=folder_id_map['templates'],
                               copy_name='Event proposal template')
    ols_cancel_rsvp = copy.file(origin_file_id=file_ids.templates['ols_cancel_rsvp'],
                                parent_folder_id=folder_id_map['templates'],
                                copy_name='OLS cancel RSVP template')
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


def _format_id_output(ids: IdMap) -> str:
    """
    Convert ID dict to output as variables separated by newlines.
    """
    variable_syntax = [f'{k} = \'{v}\'' if isinstance(v, str)
                       else f'{k} = {pprint.pformat(v)}'
                       for k, v in ids.items()]
    return '\n\n'.join(variable_syntax)


# ------------------------------------------------------------------
# Clear old data
# ------------------------------------------------------------------

@command_line.log(start_message='Clearing engagement data.',
                  end_message='Engagement data cleared.\n')
def clear_engagement_data(*, engagement_file_id: sheet.ID) -> None:
    """
    Remove last semester's submissions.
    """
    original_grid = sheet.get_values(engagement_file_id, range_='Responses!A2:Z')
    cleared_grid = columns.clear(grid=original_grid,
                                 target_indexes=list(range(30)))
    sheet.update_values(spreadsheet_id=engagement_file_id,
                        range_='Responses!A2:Z',
                        grid=cleared_grid)


@command_line.log(start_message='Clearing all-student attendance data.',
                  end_message='All-student attendance data cleared.\n')
def clear_all_student_attendance_data(*, all_student_file_id: sheet.ID) -> None:
    """
    Remove last semester's submissions.
    """
    raise NotImplementedError  # TODO: implement
    # original_grid = sheet.get_values(file_id, range_='Responses!A2:Z')
    # cleared_grid = columns.clear(all_cells=original_grid,
    #                              target_indexes=list(range(30)))
    # sheet.update_values(spreadsheet_id=file_id,
    #                     range_='Responses!A2:Z',
    #                     values=cleared_grid)


@command_line.log(start_message='Clearing no-show data.',
                  end_message='No-show data cleared.\n')
def clear_no_show_data(*, no_show_file_id: sheet.ID) -> None:
    """
    Remove last semester's submissions.
    """
    raise NotImplementedError  # TODO: implement
    # original_grid = sheet.get_values(no_show_file_id, range_='Responses!A2:Z')
    # cleared_grid = columns.clear(all_cells=original_grid,
    #                              target_indexes=list(range(30)))
    # sheet.update_values(spreadsheet_id=no_show_file_id,
    #                     range_='Responses!A2:Z',
    #                     values=cleared_grid)


@command_line.log(
        start_message='Clearing required committees for rising sophomores and mission teams for rising seniors.',
        end_message='Cleared required committees and mission teams.\n')
def clear_required_committees_and_mt(*,
                                     master_file_id: sheet.ID,
                                     sophomore_cohort: int,
                                     senior_cohort: int) -> None:
    """
    Remove committees for rising sophomores and mission teams for rising seniors.
    """
    original_grid = sheet.get_values(master_file_id, range_='A2:Z')
    cleared_committees = columns.clear_if(grid=original_grid,
                                          key_index=column_indexes.master['cohort'],
                                          key_values=[str(sophomore_cohort)],
                                          target_indexes=[column_indexes.master['committee']])
    cleared_mission_teams = columns.clear_if(grid=cleared_committees,
                                             key_index=column_indexes.master['cohort'],
                                             key_values=[str(senior_cohort)],
                                             target_indexes=[column_indexes.master['mt']])
    sheet.update_values(spreadsheet_id=master_file_id,
                        range_='A2:Z',
                        grid=cleared_mission_teams)


# ------------------------------------------------------------------
# Prepare rosters
# ------------------------------------------------------------------

@command_line.log(start_message='Setting up rosters.',
                  end_message='Rosters set up.\n')
def prepare_all_rosters(file_id_map: IdMap) -> None:
    """
    Setup every roster with data and formatting, pulling data from Master.
    """
    master_grid = sheet.get_values(file_id_map['master'], 'Master!A2:Z')
    for mt_number, mt_roster_id in file_id_map['mission_team_attendance'].items():
        prepare_roster(spreadsheet_id=mt_roster_id,
                       filter_column_index=column_indexes.master['mt'],
                       filter_value=str(mt_number),
                       master_grid=master_grid)
    for committee, committee_roster_id in file_id_map['committee_attendance'].items():
        prepare_roster(spreadsheet_id=committee_roster_id,
                       filter_column_index=column_indexes.master['committee'],
                       filter_value=committee,
                       master_grid=master_grid)


def prepare_roster(spreadsheet_id: str, *,
                   filter_column_index: int,
                   filter_value: str,
                   master_grid: sheet.Grid) -> None:
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
    # send API requests
    sheet.update_values(spreadsheet_id,
                        range_='A1:Z',
                        grid=with_headers)
    sheet.batch_update(spreadsheet_id, [dropdown_request,
                                        protected_range_request,
                                        hide_request,
                                        freeze_request,
                                        resize_request,
                                        colors_request,
                                        rename_request])


# ------------------------------------------------------------------
# Update important files like Master
# ------------------------------------------------------------------

@command_line.log(start_message='Updating formulas in Master.',
                  end_message='Master formulas updated.\n')
def update_master_formulas(file_id_map: IdMap) -> None:
    """
    Link master to all of the rosters and attendance sheets.
    """
    master_values = sheet.get_values(file_id_map['master'], 'A2:Z')
    # generate columns
    generate_master_formula = functools.partial(formulas.generate_adaptive_row_index,
                                                num_rows=len(master_values))
    service_column = generate_master_formula(
            formula=sheet_formulas.master_service(engagement_id=file_id_map['participation']['engagement']))
    civil_mil_column = generate_master_formula(
            formula=sheet_formulas.master_civil_mil(engagement_id=file_id_map['participation']['engagement']))
    committee_attendance_column = generate_master_formula(
            formula=sheet_formulas.master_committee_attendance(committee_id_map=file_id_map['committee_attendance']))
    mt_attendance_column = generate_master_formula(
            formula=sheet_formulas.master_mt_attendance(mt_id_map=file_id_map['mission_team_attendance']))
    all_student_column = generate_master_formula(
            formula=sheet_formulas.master_all_student(all_student_id=file_id_map['participation']['all_students']))
    no_show_column = generate_master_formula(
            formula=sheet_formulas.master_no_shows(no_shows_id=file_id_map['participation']['no_shows']))
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
    sheet.update_values(file_id_map['master'], range_='A2:Z', grid=result)


# -------------------------------------
# Run script
# -------------------------------------

if __name__ == '__main__':
    main()
