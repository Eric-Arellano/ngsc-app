#!/usr/bin/env python3.6

"""
CLI script to share Google Drive folders with new leadership.

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
from backend.src.data.new_semester import new_folder_ids


def main() -> None:
    confirm_sharing()
    check_files_exist()
    add_permissions()
    transfer_ownership()


# ------------------------------------------------------------------
# CLI
# ------------------------------------------------------------------

def confirm_sharing() -> None:
    """
    Make sure drive & leadership contact info set up.
    """
    semester_link = generate_link.folder(new_folder_ids.semester_root)
    command_line.ask_confirmation(question=textwrap.dedent(f'''\
                    1. Open up the new semester's drive at {semester_link}
                    2. Check the committee and mission team folders to make sure everything is good to go.
                    (Reminder: this script will email everyone in new leadership immediately.)'''),
                                  default_to_yes=True)
    command_line.ask_confirmation(question=textwrap.dedent('''\
                    3. Open up the file `backend/src/data/new_semester/new_leadership.py`
                    4. Add the emails for everyone in new student leadership.'''),
                                  default_to_yes=True)


def check_files_exist() -> None:
    """
    Checks for required files.
    """
    required_files = ['backend/src/data/new_leadership.py', 'backend/src/data/new_folder_ids.py']
    do_exist = files.do_exist(required_files)
    if not do_exist:
        raise SystemExit(
                textwrap.dedent(f'''\
                        One of the required files was not found: {' or '.join(required_files)}
                        These files should have had been created after running `./run.py setup-semester`.'''))


# ------------------------------------------------------------------
# Add permissions & share
# ------------------------------------------------------------------

@command_line.log(start_message='Adding permissions & sharing Drive folders with new leadership.',
                  end_message='Folders shared.\n')
def add_permissions() -> None:
    """
    Share folders within student leadership.
    """
    raise NotImplementedError


# ------------------------------------------------------------------
# Transfer ownership
# ------------------------------------------------------------------

@command_line.log(start_message='Transferring ownership of files to new Admin Chair.',
                  end_message='Ownership transferred.\n')
def transfer_ownership() -> None:
    """
    Share folders within student leadership.
    """
    raise NotImplementedError


# ------------------------------------------------------------------
# Run script
# ------------------------------------------------------------------

if __name__ == '__main__':
    main()
