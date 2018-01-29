import argparse
import os
import shutil
import subprocess
from textwrap import dedent
from typing import Callable, Dict, List


# -------------------------------------
# System calls
# -------------------------------------

def get_stdout(command: List[str]) -> str:
    return subprocess.run(command,
                          stdout=subprocess.PIPE,
                          encoding='utf-8').stdout.strip()


# -------------------------------------
# Command line argument parsing
# -------------------------------------

def create_parser(command_map: Dict[str, Callable], *,
                  accept_target_environment: bool = False) -> argparse.ArgumentParser:
    """
    Setups command line argument parser and assigns defaults and help statements.
    """
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    if accept_target_environment:
        parser.add_argument('target',
                            default='all',
                            nargs='?',  # must specify 0-1 argument
                            choices=['all', 'backend', 'frontend', 'script'])
    parser.add_argument('command',
                        default='run',
                        nargs='?',  # must specify 0-1 argument
                        choices=command_map.keys())
    parser.add_argument('dependencies',
                        default='',
                        nargs='*',  # can specify 0-many arguments
                        help='Dependency(ies) you want to modify.')
    return parser


def execute_command(args: argparse.Namespace, command_map: Dict[str, Callable]) -> None:
    """
    Determines which command was passed and then executes the command.

    Passes any additional parameters, such as target environment or dependencies.
    """
    func = command_map[args.command]
    # convert arguments to dict
    passed_arguments = vars(args)
    # remove empty values
    additional_arguments = {k: v for k, v in passed_arguments.items() if v}
    # remove command
    del additional_arguments['command']
    # unpack additional arguments into function as named parameters
    func(**additional_arguments)


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
Branch = str
Remote = str


def remind_to_commit(file_names: str) -> None:
    """
    Prints reminder to commit to Git the specified files.
    """
    reminder = dedent(f'''
    -----------------------------------------------------------------

    Remember to commit and push your changes to {file_names}.
    ''')
    print(reminder)


def is_on_branch(target_branch: Branch = 'master') -> bool:
    """
    Returns true if current branch is same as target branch.
    """
    current_branch = get_stdout(['git', 'rev-parse', '--abbrev-ref', 'HEAD'])
    return current_branch == target_branch


def is_clean_local() -> bool:
    """
    Returns True if there are no differences on local that need to be committed.
    """
    response = subprocess.run(['git', 'diff-index', '--quiet', 'HEAD', '--'])
    return response.returncode == 0


def fast_forward_remote(remote: Remote = 'origin', branch: Branch = 'master') -> None:
    """
    Checks given remote for any changes and attempts to fast-forward.
    """
    subprocess.run(['git', 'fetch', remote, branch])
    subprocess.run(['git', 'merge', '--ff-only'], check=True)
