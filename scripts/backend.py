#!/usr/bin/env python3.6

"""
Utility to run, install, test, and manage dependencies for the Flask backend.

Usage:
    run...
            normal: `backend.py`
            detached mode: `backend.py detached`
            stop detached: `backend.py stop`
    install...
            install: `./backend.py install`
            reinstall: `./backend.py reinstall`
            catchup: `./backend.py catchup`
    test...
            run unit tests: `./backend.py test`
            check types: `./backend.py types`
    dependency management...
            view outdated: `./backend.py outdated`
            view dependency tree: `./backend.py deptree`
            add: `./backend.py add [package(s)]`
            upgrade: `./backend.py upgrade [package(s)]`
            remove: `./backend.py remove [package(s)]`
"""

import os
import sys
from pathlib import Path

# path hack, https://chrisyeh96.github.io/2017/08/08/definitive-guide-python-imports.html
current_file_path = Path(os.path.realpath(__file__))
sys.path.append(str(current_file_path.parents[1]))

from typing import List
from scripts.utils import prereq_checker, process_management, git, sys_calls, pipenv, command_line


def main() -> None:
    parser = command_line.create_parser(command_map)
    args = parser.parse_args()
    check_prereqs()
    pipenv.remove_old_venv()
    command_line.execute_command(args, command_map)


# -------------------------------------
# Required software
# -------------------------------------

def check_prereqs() -> None:
    """
    Confirms all required software installed.
    """
    prereq_checker.check_is_installed(['python3'], windows_support=False)
    prereq_checker.check_is_installed(['python'], posix_support=False)
    command_line.check_prereqs_installed()
    process_management.check_prereqs_installed()
    git.check_prereqs_installed()
    sys_calls.check_prereqs_installed()
    pipenv.check_prereqs_installed()


# -------------------------------------
# Run commands
# -------------------------------------

def run() -> None:
    """
    Start backend server normally.
    """
    sys_calls.export('FLASK_APP', 'backend/src/server.py')
    try:
        pipenv.run(['flask', 'run'])
    except KeyboardInterrupt:
        pass


def run_detached() -> None:
    """
    Start backend server in detached mode, meaning it will not output anything.

    Must later kill process.
    """
    sys_calls.export('FLASK_APP', 'backend/src/server.py')
    pipenv.run_detached(['flask', 'run'])
    print('Backend server started at localhost:5000. Remember to stop it after.')


def stop() -> None:
    """
    Stop detached backend server by searching PID on port 5000 and then killing process.
    """
    pid = process_management.find_pid_on_port('5000')
    process_management.kill_process(pid)
    print('Backend server stopped at localhost:5000.')


# -------------------------------------
# Install commands
# -------------------------------------

def install() -> None:
    """
    Downloads & installs all dependencies for the backend.
    """
    pipenv.create()
    sys_calls.run(['pipenv', 'install'])


def reinstall() -> None:
    """
    Deletes original virtual environment and re-installs everything.
    """
    pipenv.remove()
    install()


def catchup() -> None:
    """
    Check server for changes, and install new dependencies if necessary.
    """
    git.assert_clean_local()
    git.assert_remote_branch_exists('origin', git.get_current_branch(),
                                    error_message='The current branch has not been added to GitHub, '
                                                  'so there is nothing to catchup.')
    files_changed = git.fast_forward_and_diff('origin', git.get_current_branch(),
                                              ['requirements.txt'])
    if files_changed:
        sys_calls.run(['pipenv', 'sync'])


# -------------------------------------
# Test commands
# -------------------------------------

def test() -> None:
    """
    Run unit tests.
    """
    pipenv.run(['pytest', '-q'], cwd='backend/src')


def check_types() -> None:
    """
    Calls MyPy to check for type errors.
    """
    pipenv.run(["mypy", "--strict-optional", "--ignore-missing-imports",
                "--package", "src"], cwd='backend/')


# -------------------------------------
# Dependency management commands
# -------------------------------------
Dependency = str  # type alias


def list_outdated() -> None:
    """
    List pip packages that should be updated.
    """
    sys_calls.run(["pipenv", "update", "--outdated"])


def dependency_tree() -> None:
    """
    Visualize which dependencies depend upon which.
    """
    sys_calls.run(['pipenv', 'graph'])


def add(dependencies: List[Dependency]) -> None:
    """
    Add one or more pip packages.
    """
    sys_calls.run(['pipenv', 'install'] + dependencies)


def upgrade(dependencies: List[Dependency]) -> None:
    """
    Upgrade one or more out-of-date pip packages.
    """
    sys_calls.run(['pipenv', 'update'] + dependencies)


def remove(dependencies: List[Dependency]) -> None:
    """
    Remove one or more pip packages.
    """
    sys_calls.run(['pipenv', 'uninstall'] + dependencies)


# -------------------------------------
# Command line options
# -------------------------------------
command_map = command_line.CommandMap({'run': run,
                                       'detached': run_detached,
                                       'stop': stop,
                                       'install': install,
                                       'reinstall': reinstall,
                                       'catchup': catchup,
                                       'test': test,
                                       'types': check_types,
                                       'outdated': list_outdated,
                                       'deptree': dependency_tree,
                                       'add': add,
                                       'upgrade': upgrade,
                                       'remove': remove
                                       })

# -------------------------------------
# Run script
# -------------------------------------

if __name__ == '__main__':
    main()
