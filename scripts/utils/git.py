"""
Utilities to interface with Git.
"""

import subprocess
from textwrap import dedent
from typing import List, NewType

from scripts.utils import sys_calls, prereq_checker

Branch = NewType('Branch', str)
Remote = NewType('Remote', str)
RemoteURL = NewType('RemoteURL', str)


# -----------------------------------------------------------------
# Check prereqs installed
# -----------------------------------------------------------------

def check_prereqs_installed() -> None:
    """
    Confirm all required software installed.
    """
    prereq_checker.check_is_installed(['git'])


# -----------------------------------------------------------------
# Check status
# -----------------------------------------------------------------

def is_on_branch(target_branch: Branch) -> bool:
    """
    Returns true if current branch is same as target branch.
    """
    current_branch = sys_calls.get_stdout(['git', 'rev-parse', '--abbrev-ref', 'HEAD'])
    return current_branch == target_branch


def is_remote_added(remote: Remote) -> bool:
    """
    Returns true if remote is linked to on local machine.
    """
    remotes = sys_calls.get_stdout(['git', 'remote'])
    return remote not in remotes


def is_clean_local() -> bool:
    """
    Returns True if there are no differences on local that need to be committed.
    """
    response = subprocess.run(['git', 'diff-index', '--quiet', 'HEAD', '--'])
    return response.returncode == 0


# -----------------------------------------------------------------
# Git commands
# -----------------------------------------------------------------

def fast_forward_remote(remote: Remote, branch: Branch) -> None:
    """
    Checks given remote for any changes and attempts to fast-forward.
    """
    subprocess.run(['git', 'fetch', remote, branch])
    subprocess.run(['git', 'merge', '--ff-only'], check=True)


def checkout(branch: Branch) -> None:
    """
    Simple checkout to given branch.
    """
    subprocess.run(['git', 'checkout', branch])


def add(files: List[str]) -> None:
    """
    Add given files / glob.
    """
    subprocess.run(['git', 'add'] + files)


def commit(message: str) -> None:
    """
    Commit with message.
    """
    subprocess.run(['git', 'commit', '-m', message])


def push(remote: Remote, remote_branch: Branch) -> None:
    """
    Push to given remote.
    """
    subprocess.run(['git', 'push', remote, remote_branch])


def add_remote(remote: Remote, url: RemoteURL) -> None:
    """
    Add given remote to local git.
    """
    subprocess.run(['git', 'remote', 'add', remote, url])


# -----------------------------------------------------------------
# Commit reminder
# -----------------------------------------------------------------

def remind_to_commit(file_names: str) -> None:
    """
    Prints reminder to commit to Git the specified files.
    """
    reminder = _generate_commit_reminder(file_names)
    print(reminder)


def _generate_commit_reminder(file_names: str) -> str:
    return dedent(f'''
    -----------------------------------------------------------------

    Remember to commit and push your changes to {file_names}.
    ''')
