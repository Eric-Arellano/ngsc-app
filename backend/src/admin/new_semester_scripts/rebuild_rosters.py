#!/usr/bin/env python3.6

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

from scripts.utils import command_line
from backend.src.drive_commands import generate_link
from backend.src.data.new_semester import new_file_ids
from backend.src.admin.new_semester_scripts import setup_semester


def main() -> None:
    setup_semester.check_new_ids_different()
    confirm_rebuild()
    check_master_updated()
    roster_targets = choose_rosters()
    setup_semester.prepare_all_rosters(include_committees=roster_targets.committees,
                                       include_mission_teams=roster_targets.mission_teams,
                                       add_colors=False)


def confirm_rebuild() -> None:
    """
    Make sure user really does want to overwrite all rosters.
    """
    confirmation = command_line.ask_yes_no(
            question=textwrap.dedent('''\
                    This script will overwrite ALL data on the new semester\'s rosters.
                    Are you sure you want to continue?'''),
            default='no')
    if confirmation is False:
        raise SystemExit('Canceling. The rosters will be kept as is.')


def check_master_updated() -> None:
    """
    Make sure information is ready to be copied.
    """
    master_link = generate_link.gsheet(new_file_ids.master)
    command_line.ask_confirmation(question=textwrap.dedent(f'''\
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

    def is_valid_option(answer: str) -> bool:
        return answer in ['1', '2', '3']

    option = command_line.ask_input(
            prompt=textwrap.dedent('''\
                        Which rosters do you want to rebuild?
                        1. All rosters
                        2. Committees only
                        3. Mission teams only
                        
                        Enter as a whole number.'''),
            is_valid=is_valid_option)
    if option == '1':
        return RosterTargets(committees=True, mission_teams=True)
    elif option == '2':
        return RosterTargets(committees=True, mission_teams=False)
    elif option == '3':
        return RosterTargets(committees=False, mission_teams=True)
    else:
        return RosterTargets(committees=False, mission_teams=False)


if __name__ == '__main__':
    main()
