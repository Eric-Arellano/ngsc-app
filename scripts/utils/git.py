"""
Utilities to interface with Git.
"""

from textwrap import dedent
from typing import List, Optional

from scripts.utils import prereq_checker, sys_calls

Branch = str
Remote = str
RemoteURL = str


# -----------------------------------------------------------------
# Check prereqs installed
# -----------------------------------------------------------------


def check_prereqs_installed() -> None:
    """
    Confirm all required software installed.
    """
    prereq_checker.check_is_installed(["git"])
    sys_calls.check_prereqs_installed()


# -----------------------------------------------------------------
# Check status
# -----------------------------------------------------------------


def is_on_branch(target_branch: Branch) -> bool:
    """
    Returns true if current branch is same as target branch.
    """
    return get_current_branch() == target_branch


def is_remote_added(remote: Remote) -> bool:
    """
    Returns true if remote is linked to on local machine.
    """
    remotes = sys_calls.get_stdout(["git", "remote"])
    return remote in remotes


def is_clean_local() -> bool:
    """
    Returns True if there are no differences on local that need to be committed.
    """
    response = sys_calls.run(["git", "diff-index", "--quiet", "HEAD", "--"])
    return response.returncode == 0


def remote_branch_exists(remote: Remote, branch: Branch) -> bool:
    """
    Returns True if branch exists on the remote.
    """
    response = sys_calls.get_stdout(["git", "ls-remote", "--heads", remote, branch])
    return branch in response


# -----------------------------------------------------------------
# Assert status
# -----------------------------------------------------------------


def assert_clean_local(*, error_message: str = "") -> None:
    """
    Raise exception if not clean local.
    """
    if not error_message:
        error_message = (
            "Error: You must first commit your changes before running this command."
        )
    if not is_clean_local():
        raise SystemExit(error_message)


def assert_on_branch(
    target_branch: Branch, *, error_message: Optional[str] = None
) -> None:
    """Raise excpetion if not already on target branch."""
    if error_message is None:
        error_message = f"Error: you must be on the branch {target_branch}."
    if not is_on_branch(target_branch):
        raise SystemExit(error_message)


def assert_remote_branch_exists(
    remote: Remote, branch: Branch, *, error_message: str = ""
) -> None:
    """
    Raise exception if remote branch not added.
    """
    if not error_message:
        error_message = (
            f"Error: The branch {branch} has not been added to the remote {remote}."
        )
    if not remote_branch_exists(remote, branch):
        raise SystemExit(error_message)


# -----------------------------------------------------------------
# Get current environment
# -----------------------------------------------------------------


def get_current_branch() -> Branch:
    """
    Finds current git branch.
    """
    return sys_calls.get_stdout(["git", "rev-parse", "--abbrev-ref", "HEAD"])


def get_file_hash(file: str) -> str:
    """
    Checks HEAD for the hash of given file. Allows for comparisons if file has changed.
    """
    return sys_calls.get_stdout(["git", "rev-parse", f"HEAD:{file}"])


# -----------------------------------------------------------------
# Primitive Git commands
# -----------------------------------------------------------------


def fast_forward(remote: Remote, branch: Branch) -> None:
    """
    Checks given remote for any changes and attempts to fast-forward.
    """
    sys_calls.run(["git", "fetch", remote, branch])
    sys_calls.run(["git", "merge", "--ff-only"], check=True)


def checkout(branch: Branch) -> None:
    """
    Simple checkout to given branch.
    """
    sys_calls.run(["git", "checkout", branch])


def add(files: List[str]) -> None:
    """
    Add given files / glob.
    """
    sys_calls.run(["git", "add"] + files)


def commit(message: str) -> None:
    """
    Commit with message.
    """
    if sys_calls.is_windows_environment():
        # Windows must wrap message with "" because of how bash expansion works
        message = f'"{message}"'
    sys_calls.run(["git", "commit", "-m", message])


def push(remote: Remote, remote_branch: Branch) -> None:
    """
    Push to given remote.
    """
    sys_calls.run(["git", "push", remote, remote_branch])


def add_remote(remote: Remote, url: RemoteURL) -> None:
    """
    Add given remote to local git.
    """
    sys_calls.run(["git", "remote", "add", remote, url])


# -----------------------------------------------------------------
# Custom Git commands
# -----------------------------------------------------------------


def fast_forward_and_diff(remote: Remote, branch: Branch, files: List[str]) -> bool:
    """
    Fast forward to remote and return True if the given files were modified.
    """
    old_file_hashes = [get_file_hash(file) for file in files]
    fast_forward(remote, branch)
    new_file_hashes = [get_file_hash(file) for file in files]
    return old_file_hashes != new_file_hashes


# -----------------------------------------------------------------
# Commit reminder
# -----------------------------------------------------------------


def remind_to_commit(file_names: str) -> None:
    """
    Prints reminder to commit to Git the specified files.
    """
    reminder = _generate_commit_reminder(file_names)
    print(reminder)


def _generate_commit_reminder(file_names: str) -> str:
    return dedent(
        f"""
    -----------------------------------------------------------------

    Remember to commit and push your changes to {file_names}.
    """
    )
