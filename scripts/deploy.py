#!/usr/bin/env python3.7

import os
import sys
from pathlib import Path

# path hack, https://chrisyeh96.github.io/2017/08/08/definitive-guide-python-imports.html
current_file_path = Path(os.path.realpath(__file__))
sys.path.append(str(current_file_path.parents[1]))

from scripts.utils import heroku, git, command_line


def main() -> None:
    check_prereqs_installed()
    check_remote_added()
    check_logged_in()
    resolve_git_issues()
    confirm_code_quality()
    deploy()


def check_prereqs_installed() -> None:
    """
    Confirms all required software installed.
    """
    command_line.check_prereqs_installed()
    heroku.check_prereqs_installed()
    git.check_prereqs_installed()


def check_remote_added() -> None:
    """
    Add Heroku remote if not already exists.
    """
    if not git.is_remote_added("heroku"):
        git.add_remote("heroku", "https://git.heroku.com/ngsc-app.git")


def check_logged_in() -> None:
    """
    Exit script if not logged in to Heroku CLI.
    """
    if not heroku.is_logged_in():
        raise SystemExit(
            "You must first login to Heroku using `heroku login`. "
            "Ask Eric (ecarell1@asu.edu) for his Heroku credentials."
        )


def resolve_git_issues() -> None:
    """
    Confirm on master branch, branch is clean, and check for changes from remote.
    """
    git.assert_clean_local()
    if not git.is_on_branch("master"):
        git.checkout("master")
    git.fast_forward("origin", "master")
    git.fast_forward("heroku", "master")


def confirm_code_quality() -> None:
    """
    Ask if they have confirmed the project is ready to deploy.
    """
    if not command_line.ask_yes_no("Have you tested the project adequately?"):
        raise SystemExit("You should test the project before deploying.")


def deploy() -> None:
    """
    Push to GitHub origin master and Heroku origin master.
    """
    git.push("origin", "master")
    git.push("heroku", "master")


if __name__ == "__main__":
    main()
