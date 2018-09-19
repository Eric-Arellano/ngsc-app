"""
Utilities to interface with Pipenv.
"""
from typing import List

from scripts.utils import files, prereq_checker, sys_calls


# -----------------------------------------------------------------
# Check prereqs installed
# -----------------------------------------------------------------


def check_prereqs_installed() -> None:
    """
    Confirm all required software installed.
    """
    prereq_checker.check_is_installed(["python3"], windows_support=False)
    prereq_checker.check_is_installed(["python"], posix_support=False)
    prereq_checker.check_is_installed(["pipenv"])
    sys_calls.check_prereqs_installed()
    files.check_prereqs_installed()


# -----------------------------------------------------------------
# Setup Commands
# -----------------------------------------------------------------


def create() -> None:
    """
    Create new Pipenv virtual environment in root if not already done.
    """
    if files.do_exist([".venv/"]):
        print("Pipenv already created.")
        return
    sys_calls.export("PIPENV_VENV_IN_PROJECT", "true")
    sys_calls.run(["pipenv", "--python", "3.7"])


def remove() -> None:
    """
    Deletes the virtual environment.
    """
    sys_calls.run(["pipenv", "--rm"])


def remove_old_venv() -> None:
    """
    Remove old venv in favor of Pipenv.
    """
    paths = ["pyvenv.cfg", "pip-selfcheck.json"]
    paths += (
        ["Scripts", "Include", "Lib", "lib64"]
        if sys_calls.is_windows_environment()
        else ["bin/", "include/", "lib/"]
    )
    paths = [f"backend/{path}" for path in paths]
    files.remove(paths)


# -----------------------------------------------------------------
# Run Python Commands within virtual environment
# -----------------------------------------------------------------


def run(command: List[str], **kwargs) -> None:
    """
    Run command with virtual environment activated.
    """
    sys_calls.run(["pipenv", "run"] + command, **kwargs)


def run_detached(command: List[str], **kwargs) -> None:
    """
    Run non-blocking command with virtual environment activated & output ignored.
    """
    sys_calls.run_detached(["pipenv", "run"] + command, **kwargs)
