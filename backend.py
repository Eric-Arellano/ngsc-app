#!/usr/bin/env python3

"""
Utility to run, install, test, and manage dependencies for the Flask backend.

Usage:
    run...
            normal: `backend.py`
            detached mode: `backend.py detached`
            kill detached: `backend.py kill`
    install...
            install: `./backend.py install`
    test...
            check types: `./backend.py types`
    dependency management...
            catchup: `./backend.py catchup`
            view outdated: `./backend.py outdated`
            view dependency tree: `./backend.py deptree`
            add: `./backend.py add [package(s)]`
            upgrade: `./backend.py upgrade [package(s)]`
            remove: `./backend.py remove [package(s)]`
"""

import argparse
import subprocess
import os
from typing import List
import pprint

from _script_helper import (cd, check_prereqs_installed, find_pid_on_port, is_windows_environment, kill_process,
                            remind_to_commit)


def main() -> None:
    # setup parser
    parser = _create_parser()
    args = parser.parse_args()
    # check prereqs
    check_prereqs_installed(['grep', 'awk'])
    check_prereqs_installed(['python3', 'lsof', 'kill'], windows_support=False)
    check_prereqs_installed(['python', 'netstat', 'tskill', 'findstr'], posix_support=False)
    # run
    choose_command(args)


# -------------------------------------
# venv (virtual environment)
# -------------------------------------

def _activate_venv() -> None:
    """
    Activates venv (virtual environment) for Python, which allows using locally installed packages.
    """
    command = ['bash', '-c', 'source activate && env']
    # find & source activate/ file
    if is_windows_environment():
        with cd('backend/Scripts/'):
            proc = subprocess.run(command, stdout=subprocess.PIPE)
    else:
        with cd('backend/bin/'):
            proc = subprocess.Popen(command, stdout=subprocess.PIPE)
    # convert to environment
    for line in proc.stdout:
        (key, _, value) = line.decode().partition("=")
        os.environ[key] = value
    proc.communicate()


# -------------------------------------
# Run commands
# -------------------------------------

def run() -> None:
    """
    Start backend server normally.
    """
    _activate_venv()
    os.environ['FLASK_APP'] = 'backend/src/app.py'
    subprocess.run(["flask", "run"])


def run_detached() -> None:
    """
    Start backend server in detached mode, meaning it will not output anything.

    Must later kill process.
    """
    subprocess.check_output("yarn start &>/dev/null &",
                            shell=True)


def kill() -> None:
    """
    Kill detached backend server by searching PID on port 5000 and then killing process.
    """
    pid = find_pid_on_port(5000)
    kill_process(pid)


# -------------------------------------
# Install commands
# -------------------------------------

def install() -> None:
    """
    Downloads & installs all dependencies for the backend.
    """
    subprocess.run(["yarn", "install"])


def build() -> None:
    """
    Builds backend into two minified files, allowing the backend to render backend.
    """
    subprocess.run(["yarn", "build"])


# -------------------------------------
# Test commands
# -------------------------------------

def check_types() -> None:
    """
    Calls Flow to check for type errors.
    """
    subprocess.run(["yarn", "flow"])


# -------------------------------------
# Test commands
# -------------------------------------
Dependency = str  # type alias


def catchup() -> None:
    """
    Check if any new pip dependencies added from others remotely, and then install them if so.
    """
    # TODO: actually check for differences in requirements.txt
    subprocess.run(["yarn", "install"])


def list_outdated() -> None:
    """
    List pip packages that should be updated.
    """
    subprocess.run(["yarn", "outdated"])


def dependency_tree() -> None:
    """

    """


def add(dependencies: List[Dependency]) -> None:
    """
    Add one or more pip packages.
    """
    subprocess.run(["yarn", "add"] + dependencies)
    remind_to_commit("package.json and yarn.lock")


def upgrade(dependencies: List[Dependency]) -> None:
    """
    Upgrade one or more out-of-date pip packages.
    """
    subprocess.run(["yarn", "upgrade"] + dependencies)
    remind_to_commit("package.json and yarn.lock")


def remove(dependencies: List[Dependency]) -> None:
    """
    Remove one or more pip packages.
    """
    subprocess.run(["yarn", "remove"] + dependencies)
    remind_to_commit("package.json and yarn.lock")


# -------------------------------------
# Command line options
# -------------------------------------
command_map = {'run': run,
               'detached': run_detached,
               'kill': kill,
               'install': install,
               'build': build,
               'types': check_types,
               'catchup': catchup,
               'outdated': list_outdated,
               'deptree': dependency_tree,
               'add': add,
               'upgrade': upgrade,
               'remove': remove
               }


def _create_parser() -> argparse.ArgumentParser:
    """
    Setups command line argument parser and assigns defaults and help statements.
    """
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('command',
                        default='run',
                        nargs='?',  # must specify 0-1 argument
                        choices=command_map.keys())
    parser.add_argument('dependency',
                        default='',
                        nargs='*',  # can specify 0-many arguments
                        help='Dependency(ies) you want to modify.')
    return parser


def choose_command(args: argparse.Namespace) -> None:
    """
    Determines which command was passed and then executes the command.
    """
    func = command_map[args.command]
    if args.dependency:
        func(args.dependency)
    else:
        func()


# -------------------------------------
# Run script
# -------------------------------------

if __name__ == '__main__':
    main()
