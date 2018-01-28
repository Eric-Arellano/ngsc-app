import os
import shutil
import subprocess
from contextlib import contextmanager
from textwrap import dedent
from typing import List


# -------------------------------------
# File navigation
# -------------------------------------

@contextmanager
def cd(new_dir: str):
    """
    Temporarily changes into directory, then changes back to original after context ends.

    Invoke as a context, aka `with cd(path):`.
    """
    prev_dir = os.getcwd()
    os.chdir(os.path.expanduser(new_dir))
    try:
        yield
    finally:
        os.chdir(prev_dir)


# -------------------------------------
# Determine environment
# -------------------------------------

def is_windows_environment() -> bool:
    """
    Return True if on Windows, else on Posix.
    """
    return os.name == 'nt'


def activate_venv() -> None:
    """
    Activates venv (virtual environment) for Python, which allows using locally installed packages.
    """
    if is_windows_environment():
        with cd('backend/Scripts/'):
            os.system('source activate')
    else:
        with cd('backend/bin/'):
            os.system('source activate')


# -------------------------------------
# Check prereqs installed
# -------------------------------------

ProgramName = str


def check_prereqs_installed(prereqs: List[ProgramName], *,
                            windows_support=True,
                            posix_support=True) -> None:
    """
    Raise error if dependencies are not installed on environment.

    Can conditionally only check Windows or Posix systems.
    """
    # universal programs
    if windows_support and posix_support:
        _check_prereqs(prereqs)
    # windows only programs
    elif windows_support and is_windows_environment():
        _check_prereqs(prereqs)
    # posix only programs
    elif posix_support and not is_windows_environment():
        _check_prereqs(prereqs)


def _check_prereqs(prereqs: List[ProgramName]) -> None:
    """
    Raise system error if any of the programs not installed on system.
    """
    for prereq in prereqs:
        if not _is_installed(prereq):
            raise SystemExit(f'{prereq} must be installed.')


def _is_installed(prereq: ProgramName) -> bool:
    """
    Boolean check if program installed on computer or not.
    """
    return shutil.which(prereq) is not None


# -------------------------------------
# Task management
# -------------------------------------

Port = int
PID = int


def find_pid_on_port(port: Port) -> PID:
    if is_windows_environment():
        pid = subprocess.check_output(f"netstat -aon | findstr :{port} | awk '{ print $5 }'",
                                      shell=True)
    else:
        pid = subprocess.check_output(f"lsof -n -i4TCP:{port} | grep LISTEN | awk '{ print $2 }'",
                                      shell=True)
    return pid.rstrip()


def kill_process(pid: PID) -> None:
    if is_windows_environment():
        return subprocess.run(["tskill", pid])
    else:
        return subprocess.run(["kill", pid])


# -------------------------------------
# Git helper
# -------------------------------------

def remind_to_commit(file_names: str) -> None:
    reminder = dedent(f'''
    -----------------------------------------------------------------

    Remember to commit and push your changes to {file_names}.
    ''')
    print(reminder)
