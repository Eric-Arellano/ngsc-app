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

import subprocess
from typing import List

import helper


def main() -> None:
    parser = helper.create_parser(command_map)
    args = parser.parse_args()
    check_prereqs()
    helper.execute_command(args, command_map)


# -------------------------------------
# Required software
# -------------------------------------

def check_prereqs() -> None:
    """
    Confirms all required software installed.
    """
    helper.check_prereqs_installed(['yarn', 'npm', 'node', 'grep', 'awk'])
    helper.check_prereqs_installed(['lsof', 'kill'], windows_support=False)
    helper.check_prereqs_installed(['netstat', 'tskill', 'findstr'], posix_support=False)


# -------------------------------------
# Run commands
# -------------------------------------

def run() -> None:
    """
    Start frontend server normally.
    """
    try:
        subprocess.run(["yarn", "start"], cwd='frontend/')
    except KeyboardInterrupt:
        pass


def run_detached() -> None:
    """
    Start frontend server in detached mode, meaning it will not output anything.

    Must later kill process.
    """
    subprocess.run("yarn start &>/dev/null &",
                   shell=True, cwd='frontend/')
    print("Frontend server started at localhost:3000. Remember to kill it after.")


def kill() -> None:
    """
    Kill detached frontend server by searching PID on port 3000 and then killing process.
    """
    pid = helper.find_pid_on_port(3000)
    helper.kill_process(pid)
    print("Frontend server killed at localhost:3000.")


# -------------------------------------
# Install commands
# -------------------------------------

def install() -> None:
    """
    Downloads & installs all dependencies for the frontend.
    """
    subprocess.run(["yarn", "install"], cwd='frontend/')


def build() -> None:
    """
    Builds frontend into two minified files, allowing the backend to render frontend.
    """
    subprocess.run(["yarn", "build"], cwd='frontend/')


# -------------------------------------
# Test commands
# -------------------------------------

def check_types() -> None:
    """
    Calls Flow to check for type errors.
    """
    subprocess.run(["yarn", "flow"], cwd='frontend/')


# -------------------------------------
# Test commands
# -------------------------------------
Dependency = str  # type alias


def catchup() -> None:
    """
    Check if any new npm dependencies added from others remotely, and then install them if so.
    """
    # TODO: actually check for differences in package.json
    subprocess.run(["yarn", "install"], cwd='frontend/')


def list_outdated() -> None:
    """
    List npm packages that should be updated.
    """
    subprocess.run(["yarn", "outdated"], cwd='frontend/')


def add(dependencies: List[Dependency]) -> None:
    """
    Add one or more npm packages.
    """
    subprocess.run(["yarn", "add"] + dependencies, cwd='frontend/')
    helper.remind_to_commit("package.json and yarn.lock")


def upgrade(dependencies: List[Dependency]) -> None:
    """
    Upgrade one or more out-of-date npm packages.
    """
    subprocess.run(["yarn", "upgrade"] + dependencies, cwd='frontend/')
    helper.remind_to_commit("package.json and yarn.lock")


def remove(dependencies: List[Dependency]) -> None:
    """
    Remove one or more npm packages.
    """
    subprocess.run(["yarn", "remove"] + dependencies, cwd='frontend/')
    helper.remind_to_commit("package.json and yarn.lock")


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

# -------------------------------------
# Run script
# -------------------------------------

if __name__ == '__main__':
    main()
