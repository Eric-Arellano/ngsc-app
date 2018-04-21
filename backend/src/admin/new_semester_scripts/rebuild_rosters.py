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
    master_updated = command_line.ask_yes_no(
            question='Is all of the information on the new semester\'s master spreadsheet up-to-date?')
    if not master_updated:
        raise SystemExit('Please update the new semester\'s master before running this script.')


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
