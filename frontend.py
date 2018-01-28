#!/usr/bin/env python3

"""
Utility to run, install, test, and manage dependencies for the React frontend.

Usage:
    run...
            normal: `frontend.py`
            detached mode: `frontend.py detached`
            kill detached: `frontend.py kill`
    install...
            install: `./frontend.py install`
            build: `./frontend.py build`
    test...
            check types: `./frontend.py types`
    dependency management...
            catchup: `./frontend.py catchup`
            view outdated: `./frontend.py outdated`
            add: `./frontend.py add [package(s)]`
            upgrade: `./frontend.py upgrade [package(s)]`
            remove: `./frontend.py remove [package(s)]`
"""

import argparse
import subprocess
from typing import List

from _script_helper import (cd,
                            check_prereqs_installed,
                            find_pid_on_port,
                            kill_process,
                            remind_to_commit)


def main() -> None:
    # setup parser
    parser = _create_parser()
    args = parser.parse_args()
    # check prereqs
    check_prereqs_installed(['yarn', 'npm', 'node', 'grep', 'awk'])
    check_prereqs_installed(['lsof', 'kill'], windows_support=False)
    check_prereqs_installed(['netstat', 'tskill', 'findstr'], posix_support=False)
    # run
    with cd('frontend/'):
        choose_command(args)


# -------------------------------------
# Run commands
# -------------------------------------

def run() -> None:
    """
    Start frontend server normally.
    """
    subprocess.run(["yarn", "start"])


def run_detached() -> None:
    """
    Start frontend server in detached mode, meaning it will not output anything.

    Must later kill process.
    """
    subprocess.check_output("yarn start &>/dev/null &",
                            shell=True)


def kill() -> None:
    """
    Kill detached frontend server by searching PID on port 3000 and then killing process.
    """
    pid = find_pid_on_port(3000)
    kill_process(pid)


# -------------------------------------
# Install commands
# -------------------------------------

def install() -> None:
    """
    Downloads & installs all dependencies for the frontend.
    """
    subprocess.run(["yarn", "install"])


def build() -> None:
    """
    Builds frontend into two minified files, allowing the backend to render frontend.
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
    Check if any new npm dependencies added from others remotely, and then install them if so.
    """
    # TODO: actually check for differences in package.json
    subprocess.run(["yarn", "install"])


def list_outdated() -> None:
    """
    List npm packages that should be updated.
    """
    subprocess.run(["yarn", "outdated"])


def add(dependencies: List[Dependency]) -> None:
    """
    Add one or more npm packages.
    """
    subprocess.run(["yarn", "add"] + dependencies)
    remind_to_commit("package.json and yarn.lock")


def upgrade(dependencies: List[Dependency]) -> None:
    """
    Upgrade one or more out-of-date npm packages.
    """
    subprocess.run(["yarn", "upgrade"] + dependencies)
    remind_to_commit("package.json and yarn.lock")


def remove(dependencies: List[Dependency]) -> None:
    """
    Remove one or more npm packages.
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
