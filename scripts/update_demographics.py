#!/usr/bin/env python3.7

import json
import os
import pprint
import sys
from pathlib import Path

# path hack, https://chrisyeh96.github.io/2017/08/08/definitive-guide-python-imports.html
current_file_path = Path(os.path.realpath(__file__))
sys.path.append(str(current_file_path.parents[1]))

from textwrap import dedent
from scripts.utils import git, sys_calls, prereq_checker


def main() -> None:
    check_prereqs_installed()
    resolve_git_issues()
    update_student_ids_file()
    check_valid_update()
    commit_changes()


def check_prereqs_installed() -> None:
    """
    Confirms all required software installed.
    """
    prereq_checker.check_is_installed(['curl'])
    git.check_prereqs_installed()
    sys_calls.check_prereqs_installed()


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
    raw_json = sys_calls.get_stdout(['curl',
                                     'https://ngsc-app.org/api/app/demographics/all_students_encrypted',
                                     '--silent'])
    parsed_json = json.loads(raw_json)
    formatted_json = pprint.pformat(parsed_json, width=1)
    with open('backend/src/data/demographics.py', 'w') as file:
        file.write(f'demographics_data = {formatted_json}')


def check_valid_update() -> None:
    """
    Check file correctly updated and ready to be deployed.
    """
    num_lines = sum(1 for line in open('backend/src/data/demographics.py'))
    if num_lines < 3_000:
        raise SystemExit(dedent('''\
                It appears there was an issue with writing to demographics.py. 
                Check and consider reverting any changes.
                '''))


def commit_changes() -> None:
    """
    Commit changes and deploy to GitHub and Heroku.
    """
    git.add(['backend/src/data/demographics.py'])
    git.commit('update demographics')
    print('Deploy with `./run.py deploy`')


if __name__ == '__main__':
    main()
