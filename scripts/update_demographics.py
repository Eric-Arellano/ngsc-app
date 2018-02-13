#!/usr/bin/env python3.6

"""
Utility to update hardcoded file of student information.
"""
import os
import sys

# path hack, https://chrisyeh96.github.io/2017/08/08/definitive-guide-python-imports.html
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from scripts import deploy
from scripts.utils import git, sys_calls, prereq_checker


def main() -> None:
    check_prereqs_installed()
    resolve_git_issues()
    update_student_ids_file()
    redeploy()


def check_prereqs_installed() -> None:
    """
    Confirms all required software installed.
    """
    prereq_checker.check_is_installed(['curl'])
    git.check_prereqs_installed()
    sys_calls.check_prereqs_installed()
    deploy.check_prereqs_installed()


def resolve_git_issues() -> None:
    """
    Confirm on master branch, branch is clean, and check for changes from remote.
    """
    git.assert_clean_local()
    if not git.is_on_branch('master'):
        git.checkout('master')
    git.fast_forward('origin', 'master')


def update_student_ids_file() -> None:
    """
    Get JSON from API and write it to hardcoded file.
    """
    json = sys_calls.get_stdout(['curl',
                                 'http://ngsc-app.org/api/demographics/all_students',
                                 '--silent'])
    with open('backend/src/data/demographics.py', 'w') as file:
        file.write(f'demographics_data = {json}')


def redeploy() -> None:
    """
    Commit changes and deploy to GitHub and Heroku.
    """
    git.add(['backend/src/data/demographics.py'])
    git.commit('update demographics')
    deploy.main()


if __name__ == '__main__':
    main()
