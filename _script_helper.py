import argparse
import os
import shutil
import subprocess
from contextlib import contextmanager
from textwrap import dedent
from typing import Callable, Dict, List


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
# Command line argument parsing
# -------------------------------------

def create_parser(command_map: Dict[str, Callable]) -> argparse.ArgumentParser:
    """
    Setups command line argument parser and assigns defaults and help statements.
    """
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('command',
                        default='run',
                        nargs='?',  # must specify 0-1 argument
                        choices=command_map.keys())
    parser.add_argument('dependency',
                        default='',
                        nargs='*',  # can specify 0-many arguments
                        help='Dependency(ies) you want to modify.')
    return parser


def execute_command(args: argparse.Namespace, command_map: Dict[str, Callable]) -> None:
    """
    Determines which command was passed and then executes the command.
    """
    func = command_map[args.command]
    if args.dependency:
        func(args.dependency)
    else:
        func()


# -------------------------------------
# Determine environment
# -------------------------------------

def is_windows_environment() -> bool:
    """
    Return True if on Windows, else on Posix.
    """
    return os.name == 'nt'


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
    """
    Finds and returns PID of process listening on specified port.
    """
    # determine environment
    if is_windows_environment():
        command = f"netstat -aon | findstr :{port} | awk '{{ print $5 }}'"
    else:
        command = f"lsof -n -i4TCP:{port} | grep LISTEN | awk '{{ print $2 }}'"
    # find PID
    pid = subprocess.check_output(command, shell=True)
    if not pid:
        raise SystemExit(f'No process found running on port {port}.')
    return pid.rstrip()


def kill_process(pid: PID) -> None:
    """
    Kills the specified PID.
    """
    if is_windows_environment():
        command = 'tskill'
    else:
        command = 'kill'
    subprocess.run([command, pid])


# -------------------------------------
# Git helper
# -------------------------------------

def remind_to_commit(file_names: str) -> None:
    """
    Prints reminder to commit to Git the specified files.
    """
    reminder = dedent(f'''
    -----------------------------------------------------------------

    Remember to commit and push your changes to {file_names}.
    ''')
    print(reminder)
