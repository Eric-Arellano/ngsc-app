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

from scripts.utils import command_line, files
from backend.src.drive_commands import generate_link
from backend.src.data.new_semester import new_file_ids


def main() -> None:
    confirm_rebuild()
    check_files_exist()
    rebuild()


# ------------------------------------------------------------------
# CLI
# ------------------------------------------------------------------

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
    master_link = generate_link.gsheet(new_file_ids.master)
    command_line.ask_confirmation(question=textwrap.dedent(f'''\
                    1. Open up the new semester's master spreadsheet at {master_link}
                    2. Make sure all the information is up-to-date, e.g. the \'Leave of Absence\' tab is up-to-date.'''),
                                  default_to_yes=True)


def check_files_exist() -> None:
    """
    Checks for required files.
    """
    required_files = ['backend/src/data/new_folder_ids.py', 'backend/src/data/new_file_ids.py']
    do_exist = files.do_exist(required_files)
    if not do_exist:
        raise SystemExit(
                textwrap.dedent(f'''\
                        One of the required files was not found: {' or '.join(required_files)}
                        These files should have had been created after running `./run.py setup-semester`.'''))


# ------------------------------------------------------------------
# Add permissions & share
# ------------------------------------------------------------------

@command_line.log(start_message='Rebuilding all rosters.',
                  end_message='Rosters rebuilt.\n')
def rebuild() -> None:
    """
    Share folders within student leadership.
    """
    raise NotImplementedError


# ------------------------------------------------------------------
# Run script
# ------------------------------------------------------------------

if __name__ == '__main__':
    main()
