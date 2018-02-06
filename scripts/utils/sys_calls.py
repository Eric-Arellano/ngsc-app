"""
Utilities to interface with the outside world.
"""

import os
import subprocess
from typing import List


# -----------------------------------------------------------------
# Check prereqs installed
# -----------------------------------------------------------------

def check_prereqs_installed() -> None:
    """
    Confirm all required software installed.
    """
    pass  # nothing required


# -----------------------------------------------------------------
# Determine environment
# -----------------------------------------------------------------

def is_windows_environment() -> bool:
    """
    Return True if on Windows, else on Posix.
    """
    return os.name == 'nt'


# -----------------------------------------------------------------
# Run commands
# -----------------------------------------------------------------

def run(command: List[str], **kwargs) -> subprocess.CompletedProcess:
    """
    Calls subprocess.run() and allows seamless support of both Windows and Unix.
    """
    if is_windows_environment():
        return subprocess.run(' '.join(command), shell=True, **kwargs)
    else:
        return subprocess.run(command, **kwargs)


def run_as_shell(command: str, **kwargs) -> subprocess.CompletedProcess:
    """
    Calls subprocess.run() with shell=True.
    """
    return subprocess.run(command, shell=True, **kwargs)


# -----------------------------------------------------------------
# Get StdOut of process
# -----------------------------------------------------------------

def get_stdout(command: List[str], **kwargs) -> str:
    """
    Performs the given command and returns the stdout as a string.
    """
    if is_windows_environment():
        return subprocess.run(' '.join(command),
                              shell=True,
                              stdout=subprocess.PIPE,
                              encoding='utf-8',
                              **kwargs).stdout.strip()
    else:
        return subprocess.run(command,
                              stdout=subprocess.PIPE,
                              encoding='utf-8',
                              **kwargs).stdout.strip()


def get_stdout_as_shell(command: str, **kwargs) -> str:
    """
    Performs the given command using Shell and returns the stdout as a string.
    """
    return subprocess.run(command,
                          shell=True,
                          stdout=subprocess.PIPE,
                          encoding='utf-8',
                          **kwargs).stdout.strip()


# -----------------------------------------------------------------
# Source file
# -----------------------------------------------------------------

def source_file(*, file: str, path: str) -> None:
    """
    Mirrors the source command by adding values to local environment.

    See https://stackoverflow.com/questions/3503719/emulating-bash-source-in-python
    """
    if is_windows_environment():
        command = ['cmd', '/C', f'{file} && set']
    else:
        command = ['bash', '-c', f'source {file} && env']
    process = subprocess.Popen(command,
                               stdout=subprocess.PIPE,
                               cwd=path)
    for line in process.stdout:
        (key, _, value) = line.decode("utf-8").strip().partition("=")
        os.environ[key] = value
    process.communicate()
