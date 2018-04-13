"""
Setup the Google Drive for a new semester.
"""
from typing import Dict, List, Union

from backend.src.data import column_indexes, file_ids
from backend.src.drive_commands import create
from backend.src.sheets_commands import columns, display, formulas, sheet, validation


# ------------------------------------------------------------------
# Create folders
# ------------------------------------------------------------------

def setup_folder_system() -> None:
    create_empty_folders()
    save_folder_ids({})
    raise NotImplementedError


ResourceID = str
IdMap = Dict[str, Union[ResourceID, Dict[str, ResourceID]]]


def create_empty_folders() -> IdMap:
    """
    Set up the folder structure and return their IDs.
    """
    id_map: IdMap = {}
    # Root level
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
    id_map['committee_chairs'] = {
        'admin': admin,
        'transfers': transfers,
        'civil_mil': civil_mil,
        'service': service,
        'training': training,
        'mentorship': mentorship,
        'ambassadors': ambassadors,
        'communications': communications,
        'events': events,
        'social': social
    }
    return id_map


def save_folder_ids(ids: IdMap) -> None:
    """
    Write the given folder IDs to the file `data/folder_ids.py`.
    """
    raise NotImplementedError


# ------------------------------------------------------------------
# Create rosters
# ------------------------------------------------------------------

def setup_rosters() -> None:
    """
    Will create, set up, and save the IDs for rosters for committees & mission teams.
    """
    roster_file_ids = create_empty_rosters()
    save_roster_file_ids(roster_file_ids)
    raise NotImplementedError


def create_empty_rosters() -> IdMap:
    """

    """
    raise NotImplementedError


def save_roster_file_ids(ids: IdMap) -> None:
    """
    Write the given folder IDs to the file `data/file_ids.py`.
    """
    raise NotImplementedError


def prepare_roster(*, spreadsheet: str,
                   filter_column_index: int,
                   filter_value: str) -> None:
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
    sheet.update_values(spreadsheet_id=spreadsheet,
                        range_='A1:1',
                        values=headers)
    # add data
    master = sheet.get_values(file_ids.master, 'Master!A2:Z')
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
    sheet.update_values(spreadsheet_id=spreadsheet,
                        range_='A2:Z',
                        values=blank_participation)

    # add participation formula
    def count_if(criterion: str) -> str:
        return f'COUNTIF(I$:AA$, "{criterion}")'  # `$` replaced with row index

    participation_formula = f'''=TO_PERCENT(IFERROR(
            ({count_if("yes")} + {count_if("remote")} + {count_if("excused")}) / 
            ({count_if("yes")} + {count_if("no")} + {count_if("remote")} + {count_if("excused")})
            , ""))'''
    participation_column = formulas.generate_adaptive_row_index(formula=participation_formula,
                                                                num_rows=len(blank_participation) + 10)
    sheet.update_values(spreadsheet_id=spreadsheet,
                        range_='B2:B',
                        values=participation_column)
    # add attendance dropdown
    attendance_options = ['yes', 'no', 'remote', 'excused']
    validation.dropdown_options(spreadsheet_id=spreadsheet,
                                options=attendance_options,
                                row_start_index=1,
                                row_end_index=len(blank_participation) + 10,
                                column_start_index=8,
                                column_end_index=25)
    # TODO: lock first 2 columns
    # modify display
    display.hide_columns(spreadsheet, start_index=0, end_index=1)
    display.freeze(spreadsheet, num_rows=1)
    display.auto_resize(spreadsheet)
    display.alternating_colors(spreadsheet)


# ------------------------------------------------------------------
# Setup important files like Master
# ------------------------------------------------------------------

def copy_important_files() -> None:
    """
    Copy the Master, all-student attendance, no shows, & templates.
    """
    raise NotImplementedError


def save_important_file_ids(ids: List[Dict[str, str]]) -> None:
    """
    Write the given folder IDs to the file `data/file_ids.py`.
    """
    raise NotImplementedError


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
