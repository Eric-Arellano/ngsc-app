#!/usr/bin/env python3

"""
Utility to deploy app to GitHub and Heroku.
"""
import os
import subprocess
import sys

# path hack, https://chrisyeh96.github.io/2017/08/08/definitive-guide-python-imports.html
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from scripts import helper


def main() -> None:
    check_prereqs()
    check_remote_added()
    check_logged_in()
    resolve_git_issues()
    deploy()


def check_prereqs() -> None:
    """
    Confirms all required software installed.
    """
    helper.check_prereqs_installed(['git', 'heroku'])


def check_remote_added() -> None:
    """
    Add Heroku remote if not already exists.
    """
    remotes = helper.get_stdout(['git', 'remote'])
    if 'heroku' not in remotes:
        subprocess.run(['git', 'remote', 'add', 'heroku',
                        'https://git.heroku.com/ngsc-service-hours.git'])


def check_logged_in() -> None:
    """
    Exit script if not logged in to Heroku CLI.
    """
    auth = helper.get_stdout(['heroku', 'auth:whoami'])
    if 'not logged in' in auth:
        raise SystemExit('You must first login to Heroku using `heroku login`. '
                         'Ask Eric (ecarell1@asu.edu) for his Heroku credentials.')


def resolve_git_issues() -> None:
    """
    Confirm on master branch, branch is clean, and check for changes from remote.
    """
    if not helper.is_on_branch('master'):
        subprocess.run(['git', 'checkout', 'master'])
    if not helper.is_clean_local():
        raise SystemExit('Make sure the branch is clean before running this script.')
    helper.fast_forward_remote('origin', 'master')
    helper.fast_forward_remote('heroku', 'master')


def deploy() -> None:
    """
    Push to GitHub origin master and Heroku origin master.
    """
    subprocess.run(['git', 'push', 'origin', 'master'])
    subprocess.run(['git', 'push', 'heroku', 'master'])


if __name__ == '__main__':
    main()
