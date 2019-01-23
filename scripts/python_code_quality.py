from typing import List

from scripts.utils import pipenv


def test(*, root_directory: str) -> None:
    """
    Run unit tests.
    """
    pipenv.run(["pytest", "--quiet", root_directory])


def check_types(targets: List[str]) -> None:
    """
    Calls MyPy to check for type errors.
    """
    pipenv.run(["mypy", "--config-file", "backend/mypy.ini"] + targets)


def lint(targets: List[str]) -> None:
    """
    Run Pylint.
    """
    pipenv.run(["pylint", "--rcfile=backend/.pylintrc"] + targets)


def fmt(targets: List[str], ci: bool = False) -> None:
    """
    Autoformat code.
    """
    black_command = ["black", "--py36"]
    if ci:
        black_command.append("--check")
    pipenv.run(black_command + targets)
