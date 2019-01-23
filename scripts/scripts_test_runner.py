from glob import glob
from typing import List

from scripts import python_code_quality
from scripts.utils import pipenv, sys_calls, command_line

# -------------------------------------
# Required software
# -------------------------------------


def check_prereqs_installed() -> None:
    """
    Confirms all required software installed.
    """
    command_line.check_prereqs_installed()
    sys_calls.check_prereqs_installed()
    pipenv.check_prereqs_installed()


# -------------------------------------
# Test commands
# -------------------------------------


def _get_targets() -> List[str]:
    return glob("scripts/**/*.py", recursive=True)


def green(ci: bool = False) -> None:
    """
    Call all tests and linters.
    """
    fmt(ci=ci)
    test()
    check_types()
    lint()


def check_types() -> None:
    """
    Calls MyPy to check for type errors.
    """
    python_code_quality.check_types(targets=_get_targets())


def test() -> None:
    """
    Run unit tests.
    """
    python_code_quality.test(root_directory="scripts")


def fmt(ci: bool = False) -> None:
    """
    Auto-formats script code.
    """
    python_code_quality.fmt(targets=_get_targets(), ci=ci)


def lint() -> None:
    """
    Catches errors and potential bugs.
    """
    python_code_quality.lint(targets=_get_targets())
