#!/usr/bin/env python3.7

"""
CLI script to rebuild rosters with updated student info.

Should be run locally, not on the server.
"""
import os
import sys
from pathlib import Path

# path hack, https://chrisyeh96.github.io/2017/08/08/definitive-guide-python-imports.html
current_file_path = Path(os.path.realpath(__file__))
sys.path.append(str(current_file_path.parents[1]))
sys.path.append(str(current_file_path.parents[4]))

import textwrap
from typing import NamedTuple

from googleapiclient import discovery

from scripts.utils import command_line
from backend.src.google_apis import sheets_api
from backend.src.drive_commands import generate_link
from backend.src.data.new_semester import new_file_ids
from backend.src.admin import _environment_chooser
from backend.src.admin.new_semester_scripts import setup_semester
from backend.src.sheets_commands import tab, sheet


def main() -> None:
    # check preconditions
    setup_semester.check_new_ids_different()
    override = ask_if_override()
    check_master_updated()
    # choose target
    roster_targets = choose_rosters()
    # execute
    sheets_service = sheets_api.build_service()
    if not override:
        create_legacy_tabs(include_committees=roster_targets.committees,
                           include_mission_teams=roster_targets.mission_teams)
    setup_semester.prepare_all_rosters(include_committees=roster_targets.committees,
                                       include_mission_teams=roster_targets.mission_teams,
                                       add_colors=False,
                                       sheets_service=sheets_service)
    setup_semester.update_participation_id_list(sheets_service=sheets_service)


# ---------------------------------------------------------------
# Options & Instructions
# --------------------------------------------------------------

def ask_if_override() -> bool:
    """
    Make sure user really does want to overwrite all rosters.
    """
    return command_line.ask_yes_no(
            question=textwrap.dedent('''\
                    Would you like to override the old values? Otherwise it will create a new tab on each roster 
                    saving the old values.
                    (You should override in general, unless the semester has already started. Remember to delete the 
                    legacy tabs a week after this change.)'''))


def check_master_updated() -> None:
    """
    Make sure information is ready to be copied.
    """
    master_link = generate_link.gsheet(new_file_ids.master)
    command_line.ask_confirmation(instructions=textwrap.dedent(f'''\
                    1. Open up the new semester's master spreadsheet at {master_link}
                    2. Make sure all the information is up-to-date, e.g. the \'Leave of Absence\' tab is up-to-date.
                    (Reminder: this script will pull Master for the updated roster info.)'''),
                                  default_to_yes=True)


class RosterTargets(NamedTuple):
    committees: bool
    mission_teams: bool


def choose_rosters() -> RosterTargets:
    """
    Ask if user wants to rebuild committees, mission teams, or both.
    """
    option = command_line.ask_input(
            prompt=textwrap.dedent('''\
                        Which rosters do you want to rebuild?
                        1. All rosters
                        2. Committees only
                        3. Mission teams only
                        
                        Enter as a whole number.'''),
            is_valid=lambda x: x in ['1', '2', '3'])
    if option == '1':
        return RosterTargets(committees=True, mission_teams=True)
    elif option == '2':
        return RosterTargets(committees=True, mission_teams=False)
    elif option == '3':
        return RosterTargets(committees=False, mission_teams=True)
    else:
        return RosterTargets(committees=False, mission_teams=False)


# ---------------------------------------------------------------
# Save old data
# --------------------------------------------------------------

@command_line.log(start_message='Copying old rosters into legacy tabs.',
                  end_message='Old rosters copied over.\n')
def create_legacy_tabs(*,
                       include_committees: bool,
                       include_mission_teams: bool,
                       sheets_service: discovery.Resource = None) -> None:
    legacy_tab_id = 999_999

    def create(spreadsheet_id: str) -> None:
        tab.new(spreadsheet_id=spreadsheet_id,
                tab_name='OLD DATA',
                tab_id=legacy_tab_id,
                sheets_service=sheets_service)
        grid = sheet.get_values(spreadsheet_id=spreadsheet_id,
                                range_='C:Z',
                                sheets_service=sheets_service)
        sheet.update_values(spreadsheet_id=spreadsheet_id,
                            range_="'OLD DATA'!A:Z",
                            grid=grid,
                            sheets_service=sheets_service)
    if include_committees:
        _environment_chooser.operate_on_all_committee_attendance(create)
    if include_mission_teams:
        _environment_chooser.operate_on_all_mission_team_attendance(create)


if __name__ == '__main__':
    main()
