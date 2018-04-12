"""
Setup the Google Drive for a new semester.
"""
from backend.src.data import column_indexes, file_ids
from backend.src.drive_commands import create
from backend.src.sheets_commands import columns, display, formulas, sheet


def create_empty_folders() -> None:
    """
    Set up the folder structure.
    """
    # Root level
    root = create.folder('Spring 2018')
    create.folder('Templates', parent_folder_id=root)
    # All students
    all_students = create.folder('All students', parent_folder_id=root)
    create.folder('On Leadership', parent_folder_id=all_students)
    create.folder('Summit', parent_folder_id=all_students)
    create.folder('Participation', parent_folder_id=all_students)
    # Leadership
    leadership = create.folder('Leadership', parent_folder_id=root)
    create.folder('Staff Briefings', parent_folder_id=leadership)
    # Sections & MTs
    sections = create.folder('Sections', parent_folder_id=root)
    for section_index in range(1, 11):
        section_folder_id = create.folder(f'Section {section_index}', parent_folder_id=sections)
        for mt_index in range(1, 4):
            mt_number = mt_index + (3 * (section_index - 1))
            create.folder(f'Mission Team {mt_number}', parent_folder_id=section_folder_id)
    # Committees
    committees = create.folder('Committees', parent_folder_id=root)
    engagement = create.folder('Engagement', parent_folder_id=committees)
    education = create.folder('Education', parent_folder_id=committees)
    culture = create.folder('Culture', parent_folder_id=committees)
    create.folder('Admin', parent_folder_id=committees)
    create.folder('Transfers', parent_folder_id=engagement)
    create.folder('Civil-Mil', parent_folder_id=engagement)
    create.folder('Service', parent_folder_id=engagement)
    create.folder('Training', parent_folder_id=education)
    create.folder('Mentorship', parent_folder_id=education)
    create.folder('Ambassadors', parent_folder_id=education)
    create.folder('Communications', parent_folder_id=culture)
    create.folder('Events', parent_folder_id=culture)
    create.folder('Social', parent_folder_id=culture)


def create_rosters() -> None:
    """
    Create rosters for committees and mission teams, pulling data from Master.
    """
    spreadsheet = '1SvUhsqnIiMwozc_toDCBpHWoeqNKQMrbTIseuIYF0-A'
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
                                      target_index=column_indexes.master['mt'],
                                      target_value='1')
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
                                                                num_rows=len(blank_participation))
    sheet.update_values(spreadsheet_id=spreadsheet,
                        range_='B2:B',
                        values=participation_column)
    # TODO: add attendance dropdown
    # modify display
    display.hide_columns(spreadsheet, start_index=0, end_index=1)
    display.freeze(spreadsheet, num_rows=1)
    display.auto_resize(spreadsheet)


def copy_important_files() -> None:
    """
    Copy the Master, all-student attendance, no shows, & templates.
    """
    raise NotImplementedError


def add_permissions() -> None:
    """
    Share folders within student leadership.
    """
    raise NotImplementedError
