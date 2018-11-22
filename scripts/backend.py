from glob import glob

from typing import List
from scripts import env_variables, python_code_quality
from scripts.utils import (
    prereq_checker,
    process_management,
    git,
    sys_calls,
    pipenv,
    command_line,
)

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
    env_variables.set_backend()
    try:
        pipenv.run(["flask", "run"])
    except KeyboardInterrupt:
        pass


def run_detached() -> None:
    """
    Start backend server in detached mode, meaning it will not output anything.

    Must later kill process.
    """
    env_variables.set_backend()
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


def _get_targets() -> List[str]:
    return glob("backend/src/**/*.py", recursive=True)


def green(ci: bool = False) -> None:
    """
    Call all tests and linters.
    """
    fmt(ci=ci)
    test()
    check_types()
    lint()


def test() -> None:
    """
    Run unit tests.
    """
    python_code_quality.test(root_directory="backend/src")


def check_types() -> None:
    """
    Calls MyPy to check for type errors.
    """
    python_code_quality.check_types(targets=_get_targets())


def fmt(ci: bool = False) -> None:
    """
    Auto-formats backend code.
    """
    python_code_quality.fmt(targets=_get_targets(), ci=ci)


def lint() -> None:
    """
    Catches errors and potential bugs.
    """
    python_code_quality.lint(targets=_get_targets())


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
    sys_calls.run(["pipenv", "install", "--keep-outdated"] + dependencies)


def add_dev(dependencies: List[Dependency]) -> None:
    """
    Add one or more pip packages to dev.
    """
    sys_calls.run(["pipenv", "install", "--dev", "--keep-outdated"] + dependencies)


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
