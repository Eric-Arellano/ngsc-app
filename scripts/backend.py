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

import os
import subprocess
from typing import List

from scripts import helper


def main() -> None:
    # setup parser
    parser = helper.create_parser(command_map)
    args = parser.parse_args()
    # check prereqs
    helper.check_prereqs_installed(['grep', 'awk'])
    helper.check_prereqs_installed(['python3', 'lsof', 'kill'], windows_support=False)
    helper.check_prereqs_installed(['python', 'netstat', 'tskill', 'findstr'], posix_support=False)
    # run
    helper.execute_command(args, command_map)


# -------------------------------------
# venv (virtual environment)
# -------------------------------------

def activate_venv() -> None:
    """
    Activates venv (virtual environment) for Python, which allows using locally installed packages as binaries.
    """
    # find `activate/`
    if helper.is_windows_environment():
        path = 'backend/Scripts/'
    else:
        path = 'backend/bin'
    # source `activate/`
    proc = subprocess.Popen(['bash', '-c', 'source activate && env'],
                            stdout=subprocess.PIPE,
                            cwd=path)
    # convert to environment, see https://stackoverflow.com/questions/3503719/emulating-bash-source-in-python
    for line in proc.stdout:
        (key, _, value) = line.decode("utf-8").strip().partition("=")
        os.environ[key] = value
    proc.communicate()


# -------------------------------------
# Run commands
# -------------------------------------

def run() -> None:
    """
    Start backend server normally.
    """
    activate_venv()
    os.environ['FLASK_APP'] = 'backend/src/app.py'
    try:
        subprocess.run(["flask", "run"])
    except KeyboardInterrupt:
        pass


def run_detached() -> None:
    """
    Start backend server in detached mode, meaning it will not output anything.

    Must later kill process.
    """
    activate_venv()
    os.environ['FLASK_APP'] = 'backend/src/app.py'
    subprocess.run("flask run &>/dev/null &",
                   shell=True)
    print("Backend server started at localhost:5000. Remember to kill it after.")


def kill() -> None:
    """
    Kill detached backend server by searching PID on port 5000 and then killing process.
    """
    pid = helper.find_pid_on_port(5000)
    helper.kill_process(pid)
    print("Backend server killed at localhost:5000.")


# -------------------------------------
# Install commands
# -------------------------------------

def install() -> None:
    """
    Downloads & installs all dependencies for the backend.
    """
    command = ['-m', 'venv', 'backend/']
    if helper.is_windows_environment():
        subprocess.run(['python'] + command)
    else:
        subprocess.run(['python3'] + command)
    activate_venv()
    subprocess.run(["pip", "install", "-r", "requirements.txt"])


# -------------------------------------
# Test commands
# -------------------------------------

def check_types() -> None:
    """
    Calls MyPy to check for type errors.
    """
    activate_venv()
    subprocess.run(["mypy", "--strict-optional", "--ignore-missing-imports",
                    "--package", "src"], cwd='backend/')


# -------------------------------------
# Dependency management commands
# -------------------------------------
Dependency = str  # type alias


def _freeze_requirements() -> None:
    """
    Updates the requirements.txt file with new dependencies.
    """
    with open('requirements.txt', 'w') as requirements:
        subprocess.run(['pip', 'freeze'], stdout=requirements)
    helper.remind_to_commit("requirements.txt")


def catchup() -> None:
    """
    Check if any new pip dependencies added from others remotely, and then install them if so.
    """
    # TODO: actually check for differences in requirements.txt
    activate_venv()
    subprocess.run(["pip", "install", "-r", "requirements.txt"])


def list_outdated() -> None:
    """
    List pip packages that should be updated.
    """
    activate_venv()
    subprocess.run(["pip", "list", "--outdated", "--format=columns"])


def dependency_tree() -> None:
    """
    Visualize which dependencies depend upon which.
    """
    activate_venv()
    subprocess.run(["pipdeptree"])


def add(dependencies: List[Dependency]) -> None:
    """
    Add one or more pip packages.
    """
    activate_venv()
    subprocess.run(["pip", "install"] + dependencies)
    _freeze_requirements()


def upgrade(dependencies: List[Dependency]) -> None:
    """
    Upgrade one or more out-of-date pip packages.
    """
    activate_venv()
    subprocess.run(["pip", "install", "--upgrade"] + dependencies)
    _freeze_requirements()


def remove(dependencies: List[Dependency]) -> None:
    """
    Remove one or more pip packages.
    """
    activate_venv()
    subprocess.run(["pip", "uninstall"] + dependencies)
    _freeze_requirements()


# -------------------------------------
# Command line options
# -------------------------------------
command_map = {'run': run,
               'detached': run_detached,
               'kill': kill,
               'install': install,
               'types': check_types,
               'catchup': catchup,
               'outdated': list_outdated,
               'deptree': dependency_tree,
               'add': add,
               'upgrade': upgrade,
               'remove': remove
               }

# -------------------------------------
# Run script
# -------------------------------------

if __name__ == '__main__':
    main()
