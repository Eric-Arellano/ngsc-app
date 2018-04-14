"""
Setup the Google Drive for a new semester.
"""
import pprint
from typing import Dict, Union

from backend.src.data import column_indexes, file_ids, folder_ids, formulas
from backend.src.drive_commands import copy, create
from backend.src.sheets_commands import columns, display, formulas, sheet, validation


def setup_semester() -> None:
    # create resources
    folder_id_map = create_empty_folders()
    roster_ids = create_empty_rosters(folder_id_map)
    important_files = copy_important_files(folder_id_map)
    # save to hardcoded files
    save_folder_ids(folder_id_map)
    save_file_ids({**roster_ids, **important_files})
    # prepare files
    prepare_all_rosters(roster_ids)
    # update_master_links()
    # return remaining steps


# ------------------------------------------------------------------
# Create resources
# ------------------------------------------------------------------

ResourceID = str
IdMap = Dict[str, Union[ResourceID, Dict[str, ResourceID]]]


def create_empty_folders() -> IdMap:
    """
    Set up the folder structure and return their IDs.
    """
    # NGSC root level
    id_map = {
        'ngsc_root': folder_ids.ngsc_root,
        'drive_playground': folder_ids.drive_playground
    }
    # Semester root
    root = create.folder('Spring 2018')
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


def create_empty_rosters(folder_id_map: IdMap) -> IdMap:
    """
    Create the roster spreadsheets (not set up) and save their IDs.
    """
    id_map = {
        'committee_attendance': {},
        'mission_team_attendance': {}
    }
    # Committee rosters
    for committee, committee_folder_id in folder_id_map['committees'].items():
        committee_roster_id = create.file(file_name=f'Attendance - {committee} - Fall 2018',
                                          mime_type='spreadsheet',
                                          parent_folder_id=committee_folder_id)
        id_map['committee_attendance'][committee] = committee_roster_id
    # Mission team rosters
    for mt_number, mt_folder_id in folder_id_map['mission_teams'].items():
        mt_roster_id = create.file(file_name=f'Attendance - Mission Team {mt_number} - Fall 2018',
                                   mime_type='spreadsheet',
                                   parent_folder_id=mt_folder_id)
        id_map['mission_team_attendance'][mt_number] = mt_roster_id
    return id_map


def copy_important_files(folder_id_map: IdMap) -> IdMap:
    """
    Copy the Master, schedule, all-student attendance, no shows, & templates.
    """
    id_map = {}
    # master
    master = copy.file(origin_file_id=file_ids.master,
                       parent_folder_id=folder_id_map['semester_root'],
                       copy_name='Master - Fall 2018')
    id_map['master'] = master
    # schedule
    schedule = copy.file(origin_file_id=file_ids.schedule,
                         parent_folder_id=folder_id_map['semester_root'],
                         copy_name='Schedule - Fall 2018')
    id_map['schedule'] = schedule
    # participation   TODO: copying the spreadsheet doesn't copy form. Will have to manually link form?
    engagement = copy.file(origin_file_id=file_ids.participation['engagement'],
                           parent_folder_id=folder_id_map['all_students']['participation'],
                           copy_name='Engagement - Fall 2018')
    no_shows = copy.file(origin_file_id=file_ids.participation['no_shows'],
                         parent_folder_id=folder_id_map['all_students']['participation'],
                         copy_name='No Shows - Fall 2018')
    all_students = copy.file(origin_file_id=file_ids.participation['all_students'],
                             parent_folder_id=folder_id_map['all_students']['participation'],
                             copy_name='All Students - Fall 2018')
    id_map['participation'] = {
        'all_students': all_students,
        'engagement': engagement,
        'no_shows': no_shows
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

def save_folder_ids(ids: IdMap) -> None:
    """
    Write the given folder IDs to the file `data/folder_ids.py`.
    """
    output = _format_id_output(ids)
    with open('backend/src/data/folder_ids_new.py', 'w') as file:
        file.writelines(output)


def save_file_ids(ids: IdMap) -> None:
    """
    Write the given file IDs to the file `data/file_ids.py`.
    """
    output = _format_id_output(ids)
    with open('backend/src/data/file_ids_new.py', 'w') as file:
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
# Prepare rosters
# ------------------------------------------------------------------

def prepare_all_rosters(file_id_map: IdMap) -> None:
    """
    Setup every roster with data and formatting.
    """
    for mt_number, mt_roster_id in file_id_map['mission_team_attendance'].items():
        prepare_roster(spreadsheet_id=mt_roster_id,
                       filter_column_index=column_indexes.master['mt'],
                       filter_value=str(mt_number),
                       master_spreadsheet_id=file_id_map['master'])
    for committee, committee_roster_id in file_id_map['committee_attendance'].items():
        prepare_roster(spreadsheet_id=committee_roster_id,
                       filter_column_index=column_indexes.master['committee'],
                       filter_value=committee,
                       master_spreadsheet_id=file_id_map['master'])


def prepare_roster(spreadsheet_id: str, *,
                   filter_column_index: int,
                   filter_value: str,
                   master_spreadsheet_id: str = file_ids.master) -> None:
    """
    Setup provided roster's data and formatting, pulling data from Master.
    """
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
    sheet.update_values(spreadsheet_id=spreadsheet_id,
                        range_='A1:1',
                        values=headers)
    # add data
    master = sheet.get_values(master_spreadsheet_id, 'Master!A2:Z')
    filtered = columns.filter_by_cell(all_cells=master,
                                      target_index=filter_column_index,
                                      target_value=filter_value)
    reordered = columns.reorder(all_cells=filtered,
                                new_order=[column_indexes.master['id'],
                                           column_indexes.master['first'],
                                           column_indexes.master['last'],
                                           column_indexes.master['status'],
                                           column_indexes.master['email'],
                                           column_indexes.master['phone'],
                                           column_indexes.master['campus'],
                                           column_indexes.master['cohort']])
    no_status = columns.remove(all_cells=reordered, target_indexes=[3])
    blank_participation = columns.add_blank(all_cells=no_status, target_index=1)
    sheet.update_values(spreadsheet_id=spreadsheet_id,
                        range_='A2:Z',
                        values=blank_participation)

    # add participation formula
    participation_column = formulas.generate_adaptive_row_index(formula=formulas.rosters['participation'],
                                                                num_rows=len(blank_participation) + 10)
    sheet.update_values(spreadsheet_id=spreadsheet_id,
                        range_='B2:B',
                        values=participation_column)
    # add attendance dropdown
    attendance_options = ['yes', 'no', 'remote', 'excused']
    validation.dropdown_options(spreadsheet_id=spreadsheet_id,
                                options=attendance_options,
                                row_start_index=1,
                                row_end_index=len(blank_participation) + 10,
                                column_start_index=8,
                                column_end_index=25)
    # TODO: lock first 2 columns
    # modify display
    display.hide_columns(spreadsheet_id, start_index=0, end_index=1)
    display.freeze(spreadsheet_id, num_rows=1)
    display.auto_resize(spreadsheet_id)
    display.alternating_colors(spreadsheet_id)


# ------------------------------------------------------------------
# Update important files like Master
# ------------------------------------------------------------------

def update_master_links() -> None:
    """
    Link master to all of the rosters and attendance sheets.
    """
    raise NotImplementedError


# ------------------------------------------------------------------
# Share & add permissions
# ------------------------------------------------------------------

def add_permissions() -> None:
    """
    Share folders within student leadership.
    """
    raise NotImplementedError
