#!/usr/bin/env python3

"""
Utility to update hardcoded file of student information.
"""
import subprocess

import deploy
from _script_helper import (check_prereqs_installed, fast_forward_remote, get_stdout, is_clean_local,
                            is_on_branch)


def main() -> None:
    check_prereqs_installed(['git'])
    resolve_git_issues()
    update_student_ids_file()
    redeploy()


def resolve_git_issues() -> None:
    """
    Confirm on master branch, branch is clean, and check for changes from remote.
    """
    if not is_on_branch('master'):
        subprocess.run(['git', 'checkout', 'master'])
    if not is_clean_local():
        raise SystemExit('Make sure the branch is clean before running this script.')
    fast_forward_remote('origin', 'master')


def update_student_ids_file() -> None:
    """
    Get JSON from API and write it to hardcoded file.
    """
    json = get_stdout(['curl',
                       'http://ngsc-app.org/api/demographics/all_students',
                       '--silent'])
    with open('backend/src/student_ids.py', 'w') as file:
        file.write(f'student_ids = {json}')


def redeploy() -> None:
    """
    Commit changes and deploy to GitHub and Heroku.
    """
    subprocess.run(['git', 'add', 'backend/src/student_ids.py'])
    subprocess.run(['git', 'commit', '-m', 'update demographics'])
    deploy.main()


if __name__ == '__main__':
    main()