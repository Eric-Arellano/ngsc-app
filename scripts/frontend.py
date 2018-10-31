from glob import glob

from typing import List
from scripts.utils import (
    prereq_checker,
    process_management,
    git,
    command_line,
    sys_calls,
    files,
)


# -------------------------------------
# Required software
# -------------------------------------


def check_prereqs_installed() -> None:
    """
    Confirms all required software installed.
    """
    prereq_checker.check_is_installed(["yarn", "npm", "node"])
    command_line.check_prereqs_installed()
    git.check_prereqs_installed()
    process_management.check_prereqs_installed()
    sys_calls.check_prereqs_installed()
    files.check_prereqs_installed()


# -------------------------------------
# Run commands
# -------------------------------------


def run() -> None:
    """
    Start frontend server normally.
    """
    try:
        sys_calls.run(["yarn", "start"], cwd="frontend/")
    except KeyboardInterrupt:
        pass


def run_detached() -> None:
    """
    Start frontend server in detached mode, meaning it will not output anything.

    Must later kill process.
    """
    sys_calls.run_detached(["yarn", "start"], cwd="frontend/")
    print("Frontend server started at localhost:3000. Remember to stop it after.")


def stop() -> None:
    """
    Stop detached frontend server by searching PID on port 3000 and then killing process.
    """
    pid = process_management.find_pid_on_port("3000")
    process_management.kill_process(pid)
    print("Frontend server stopped at localhost:3000.")


# -------------------------------------
# Install commands
# -------------------------------------


def install() -> None:
    """
    Downloads & installs all dependencies for the frontend.
    """
    sys_calls.run(["yarn", "install"], cwd="frontend/")


def reinstall() -> None:
    """
    Deletes original packages and re-installs everything.
    """
    files.remove(["frontend/node_modules/"])
    install()


def build() -> None:
    """
    Builds frontend into two minified files, allowing the backend to render frontend.
    """
    sys_calls.run(["yarn", "build"], cwd="frontend/")


# -------------------------------------
# Test commands
# -------------------------------------


def _get_targets() -> List[str]:
    targets_from_root = glob("frontend/src/**/*.js", recursive=True)
    return [t[len("frontend/") :] for t in targets_from_root]


def green(ci: bool = False) -> None:
    """
    Calls all tests and linters.
    """
    test()
    check_types()
    fmt(ci=ci)
    lint()


def test() -> None:
    """
    Run unit tests.
    """
    sys_calls.run(["yarn", "test"], cwd="frontend/")


def check_types() -> None:
    """
    Calls Flow to check for type errors.
    """
    sys_calls.run(["yarn", "flow"], cwd="frontend/")

def lint() -> None:
    """
    Calls lint to check for type errors.
    """
    sys_calls.run(["yarn", "lint"] + _get_targets(), cwd="frontend/")

def fmt(ci: bool = False) -> None:
    """
    Auto-formats frontend code.
    """
    command = ["yarn", "fmt", "--write" if not ci else "--list-different"]
    sys_calls.run(command + _get_targets(), cwd="frontend")


# -------------------------------------
# Dependency management
# -------------------------------------
Dependency = str  # type alias


def list_outdated() -> None:
    """
    List npm packages that should be updated.
    """
    sys_calls.run(["yarn", "outdated"], cwd="frontend/")


def add(dependencies: List[Dependency]) -> None:
    """
    Add one or more npm packages.
    """
    sys_calls.run(["yarn", "add"] + dependencies, cwd="frontend/")
    git.remind_to_commit("package.json and yarn.lock")


def upgrade(dependencies: List[Dependency]) -> None:
    """
    Upgrade one or more out-of-date npm packages.
    """
    sys_calls.run(["yarn", "upgrade"] + dependencies, cwd="frontend/")
    git.remind_to_commit("package.json and yarn.lock")


def remove(dependencies: List[Dependency]) -> None:
    """
    Remove one or more npm packages.
    """
    sys_calls.run(["yarn", "remove"] + dependencies, cwd="frontend/")
    git.remind_to_commit("package.json and yarn.lock")
