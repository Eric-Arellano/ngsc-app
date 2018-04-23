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

from scripts.utils import command_line
from backend.src.drive_commands import generate_link, share
from backend.src.data.new_semester import new_folder_ids, new_leadership
from backend.src.data import leadership
from backend.src.admin.new_semester_scripts import setup_semester


def main() -> None:
    # preconditions
    confirm_emails_added()
    confirm_sharing()
    setup_semester.check_new_ids_different()
    check_new_leadership_different()
    # preview message
    prompt_to_warn_leadership()
    confirm_email_message_good()
    # share
    add_permissions()
    # remaining steps
    explain_ownership()


# ------------------------------------------------------------------
# Preconditions
# ------------------------------------------------------------------

def confirm_emails_added() -> None:
    """
    Make sure leadership contact info was set up *before* the script was called.
    """
    updated = command_line.ask_yes_no(
            question=textwrap.dedent('''\
                Does `backend/src/data/new_leadership.py` have all of new leaderships' emails?
                This must have been updated *before* starting this script.'''),
            default='no')
    if not updated:
        raise SystemExit('Please update this file, and then restart the script.')


def confirm_sharing() -> None:
    """
    Make sure drive & leadership contact info set up.
    """
    semester_link = generate_link.folder(new_folder_ids.semester_root)
    answer = command_line.ask_yes_no(question=textwrap.dedent(f'''\
                    This script will email everyone in new leadership immediately. 
                    
                    Before sending, you should do the following:
                    1. Open up the new semester's drive at {semester_link}
                    2. Check the committee and mission team folders to make sure everything is good to go.
                    3. If you want to add any files to their drive first, use the tool at ngsc-app.org/admin
                    
                    Are you sure you want to send?'''),
                                     default='no')
    if answer is False:
        raise SystemExit('Aborting script. Rerun when you are ready to share.')


def check_new_leadership_different() -> None:
    """
    Check new and old leadership are different, or intentionally have the same entries.
    """
    leadership_different = (leadership.chief_of_staff != new_leadership.chief_of_staff) \
                           and (leadership.committee_chairs != new_leadership.committee_chairs) \
                           and (leadership.committee_leads != new_leadership.committee_leads) \
                           and (leadership.section_leads != new_leadership.section_leads) \
                           and (leadership.mission_team_leaders != new_leadership.mission_team_leaders)
    if not leadership_different:
        answer = command_line.ask_yes_no(
                question=textwrap.dedent('''\
                At least one leadership position is the same as the current semester.
                Is this expected?'''),
                default='yes')
        if answer is False:
            raise SystemExit(textwrap.dedent('''\
                   Please update `backend/src/data/new_semester/new_leadership.py'''))


# ------------------------------------------------------------------
# Preview email
# ------------------------------------------------------------------

email_message = textwrap.dedent('''\
    Hello NGSC leadership,
    
    This is your Google Drive folder for the semester. 
    You will find your roster, and, throughout the semester, we will add additional resources, such as training materials.
    
    You can add on to this however you'd like, and are encouraged to make this a resource for your team by adding new files and folders. 
    Please do not, however, modify the provided files and folders, such as renaming the folders provided.
    
    *You should bookmark this folder in your browser.* You will be using it a lot.''')


def prompt_to_warn_leadership() -> None:
    """
    Encourage sending email to leadership explaining random email.
    """
    print(textwrap.dedent('''\
            The email will come from the Google Service Account.
            It has has a strange address of 'ngsc-322@numeric-arena-185116.iam.gserviceaccount.com', so you may want to email leadership to let them know this is not phishing or spam.
            Also remind them to *bookmark* their folder, and that they will be using it a lot.\n'''))


def confirm_email_message_good() -> None:
    """
    Preview the email that will be sent to everyone.
    """
    print(
            'This is the email everyone will get from ngsc-322@numeric-arena-185116.iam.gserviceaccount.com:\n\n' +
            email_message + '\n\n')
    answer = command_line.ask_yes_no(question='Is this good to go?',
                                     default='yes')
    if answer is False:
        raise SystemExit(textwrap.dedent('''\
            Edit the message by opening `backend/src/admin/new_semester_scripts/share_drive.py`.
            Change the variable email_message to contain what you want.
            You must then restart the script.'''))


# ------------------------------------------------------------------
# Add permissions & share
# ------------------------------------------------------------------

@command_line.log(start_message='Adding permissions & sharing Drive folders with new leadership.',
                  end_message='Folders shared.\n')
def add_permissions() -> None:
    """
    Share folders within student leadership.
    """
    committee_leads = [share.BatchArgument(resource_id=new_folder_ids.committee_leads[position],
                                           emails=[new_leadership.committee_leads[position]])
                       for position in new_leadership.committee_leads.keys()]
    chairs = [share.BatchArgument(resource_id=new_folder_ids.committees[position],
                                  emails=[new_leadership.committee_chairs[position]])
              for position in new_leadership.committee_chairs.keys()]
    section_leads = [share.BatchArgument(resource_id=new_folder_ids.sections[number],
                                         emails=[new_leadership.section_leads[number]])
                     for number in new_leadership.section_leads.keys()]
    mt_leaders = [share.BatchArgument(resource_id=new_folder_ids.mission_teams[number],
                                      emails=[new_leadership.mission_team_leaders[number]])
                  for number in new_leadership.mission_team_leaders.keys()]
    share.batch(committee_leads + chairs + section_leads + mt_leaders,
                uniform_email_message=email_message,
                uniform_send_email=True)


# ------------------------------------------------------------------
# Remaining steps
# ------------------------------------------------------------------

def explain_ownership() -> None:
    """
    Explain why service account remains the owner.
    """
    print(textwrap.dedent('''\
        The semester's drive is shared with new leadership!
        
        Note that the Google service account is the owner of all folders and files created in the `./run.py setup-semester` script.
        This is so that it retains the ability to permanently delete files. 
        
        If this becomes an issue, it is possible to modify this script to transfer ownership to someone else, such as the admin chair.
        The functions in `drive_commands/share.py` already support this functionality - call them with the transfer_ownership parameter.
        '''))


# ------------------------------------------------------------------
# Run script
# ------------------------------------------------------------------

if __name__ == '__main__':
    main()
