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
    pipenv.run(["mypy", "--strict-optional", "--ignore-missing-imports"] + targets)


def lint(targets: List[str]) -> None:
    """
    Run Pylint.
    """
    pipenv.run(["pylint"] + targets)


def fmt(targets: List[str]) -> None:
    """
    Autoformat code.
    """
    black_command = ["black", "--py36"]
    pipenv.run(black_command + targets)
