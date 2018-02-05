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
# Commands
# -----------------------------------------------------------------

def get_stdout(command: List[str]) -> str:
    """
    Performs the given command and returns the stdout as a string.
    """
    return subprocess.run(command,
                          stdout=subprocess.PIPE,
                          encoding='utf-8').stdout.strip()


def is_windows_environment() -> bool:
    """
    Return True if on Windows, else on Posix.
    """
    return os.name == 'nt'


def source_file(*, file: str, path: str) -> None:
    """
    Mirrors the source command by adding values to local environment.

    See https://stackoverflow.com/questions/3503719/emulating-bash-source-in-python
    """
    process = subprocess.Popen(['bash', '-c', f'source {file} && env'],
                               stdout=subprocess.PIPE,
                               cwd=path)
    for line in process.stdout:
        (key, _, value) = line.decode("utf-8").strip().partition("=")
        os.environ[key] = value
    process.communicate()
