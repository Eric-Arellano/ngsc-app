#!/usr/bin/env python3.7

import os
import sys
from pathlib import Path
from glob import glob

# path hack, https://chrisyeh96.github.io/2017/08/08/definitive-guide-python-imports.html
current_file_path = Path(os.path.realpath(__file__))
sys.path.append(str(current_file_path.parents[1]))

from typing import List
from scripts.utils import (
    prereq_checker,
    process_management,
    git,
    sys_calls,
    pipenv,
    command_line,
)


def main() -> None:
    parser = command_line.create_parser(
        command_options, description="Run and manage the Flask backend."
    )
    args = parser.parse_args()
    check_prereqs()
    pipenv.remove_old_venv()
    command_line.execute_command(args, command_options)


# -------------------------------------
# Required software
# -------------------------------------


def check_prereqs() -> None:
    """
    Confirms all required software installed.
    """
    prereq_checker.check_is_installed(["python3"], windows_support=False)
    prereq_checker.check_is_installed(["python"], posix_support=False)
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
    sys_calls.export("FLASK_APP", "backend/src/server.py")
    try:
        pipenv.run(["flask", "run"])
    except KeyboardInterrupt:
        pass


def run_detached() -> None:
    """
    Start backend server in detached mode, meaning it will not output anything.

    Must later kill process.
    """
    sys_calls.export("FLASK_APP", "backend/src/server.py")
    pipenv.run_detached(["flask", "run"])
    print("Backend server started at localhost:5000. Remember to stop it after.")


def stop() -> None:
    """
    Stop detached backend server by searching PID on port 5000 and then killing process.
    """
    pid = process_management.find_pid_on_port("5000")
    process_management.kill_process(pid)
    print("Backend server stopped at localhost:5000.")


# -------------------------------------
# Install commands
# -------------------------------------


def install() -> None:
    """
    Downloads & installs all dependencies for the backend.
    """
    pipenv.create()
    sys_calls.run(["pipenv", "install", "--ignore-pipfile", "--dev"])


def reinstall() -> None:
    """
    Deletes original virtual environment and re-installs everything.
    """
    pipenv.remove()
    install()


# -------------------------------------
# Test commands
# -------------------------------------


def green() -> None:
    """
    Call all tests and linters.
    """
    test()
    check_types()
    fmt()


def test() -> None:
    """
    Run unit tests.
    """
    pipenv.run(["pytest", "-q"], cwd="backend/src")


def check_types() -> None:
    """
    Calls MyPy to check for type errors.
    """
    pipenv.run(
        ["mypy", "--strict-optional", "--ignore-missing-imports", "--package", "src"],
        cwd="backend/",
    )


def fmt() -> None:
    """
    Auto-formats backend code.
    """
    targets_from_root = glob("backend/src/**/*.py", recursive=True)
    pipenv.run(["black", "--py36"] + targets_from_root)


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
    sys_calls.run(["pipenv", "graph"])


def add(dependencies: List[Dependency]) -> None:
    """
    Add one or more pip packages.
    """
    sys_calls.run(["pipenv", "install"] + dependencies)


def upgrade(dependencies: List[Dependency]) -> None:
    """
    Upgrade one or more out-of-date pip packages.
    """
    sys_calls.run(["pipenv", "update"] + dependencies)


def remove(dependencies: List[Dependency]) -> None:
    """
    Remove one or more pip packages.
    """
    sys_calls.run(["pipenv", "uninstall"] + dependencies)


# -------------------------------------
# Command line options
# -------------------------------------


def create_command_option(
    name: str, command: command_line.Command
) -> command_line.CommandOption:
    return command_line.CommandOption(name=name, command=command, help=command.__doc__)


command_options = [
    create_command_option("run", run),
    create_command_option("detached", run_detached),
    create_command_option("stop", stop),
    create_command_option("install", install),
    create_command_option("reinstall", reinstall),
    create_command_option("green", green),
    create_command_option("test", test),
    create_command_option("types", check_types),
    create_command_option("fmt", fmt),
    create_command_option("outdated", list_outdated),
    create_command_option("deptree", dependency_tree),
    create_command_option("add", add),
    create_command_option("upgrade", upgrade),
    create_command_option("remove", remove),
]

# -------------------------------------
# Run script
# -------------------------------------

if __name__ == "__main__":
    main()
