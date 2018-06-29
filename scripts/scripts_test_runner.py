#!/usr/bin/env python3.6

"""
Utility to test this scripts package itself.

Usage:
    test...
            run tests: `./tests_runner.py test`
            check types: `./tests_runner.py types`
"""

import os
import sys
from pathlib import Path

# path hack, https://chrisyeh96.github.io/2017/08/08/definitive-guide-python-imports.html
current_file_path = Path(os.path.realpath(__file__))
sys.path.append(str(current_file_path.parents[1]))

from scripts.utils import pipenv, sys_calls, command_line


def main() -> None:
    parser = command_line.create_parser(command_map)
    args = parser.parse_args()
    check_prereqs_installed()
    command_line.execute_command(args, command_map)


# -------------------------------------
# Required software
# -------------------------------------

def check_prereqs_installed() -> None:
    """
    Confirms all required software installed.
    """
    command_line.check_prereqs_installed()
    sys_calls.check_prereqs_installed()
    pipenv.check_prereqs_installed()


# -------------------------------------
# Test commands
# -------------------------------------

def check_types() -> None:
    """
    Calls MyPy to check for type errors.
    """
    pipenv.run(["mypy", "--strict-optional", "--ignore-missing-imports",
                   "--package", "scripts"])


def test() -> None:
    """
    Run unit tests.
    """
    sys_calls.run_python(['-m', 'unittest', 'discover', 'scripts/tests'])


# -------------------------------------
# Command line options
# -------------------------------------
command_map = command_line.CommandMap({'test': test,
                                       'types': check_types,
                                       })

# -------------------------------------
# Run script
# -------------------------------------

if __name__ == '__main__':
    main()
