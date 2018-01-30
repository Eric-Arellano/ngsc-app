#!/usr/bin/env python3

"""
Utility to test this scripts package itself.

Usage:
    test...
            run tests: `./tests_runner.py test`
            check types: `./tests_runner.py types`
"""

import os
import subprocess
import sys

# path hack, https://chrisyeh96.github.io/2017/08/08/definitive-guide-python-imports.html
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from scripts import helper, backend


def main() -> None:
    parser = helper.create_parser(command_map)
    args = parser.parse_args()
    check_prereqs()
    helper.execute_command(args, command_map)


# -------------------------------------
# Required software
# -------------------------------------

def check_prereqs() -> None:
    """
    Confirms all required software installed.
    """
    helper.check_prereqs_installed(['grep', 'awk'])
    helper.check_prereqs_installed(['python3', 'lsof', 'kill'], windows_support=False)
    helper.check_prereqs_installed(['python', 'netstat', 'tskill', 'findstr'], posix_support=False)


# -------------------------------------
# Test commands
# -------------------------------------

def check_types() -> None:
    """
    Calls MyPy to check for type errors.
    """
    backend.activate_venv()
    subprocess.run(["mypy", "--strict-optional", "--ignore-missing-imports",
                    "--package", "scripts"])


def test() -> None:
    """
    Run unit tests.
    """
    if helper.is_windows_environment():
        py = 'python'
    else:
        py = 'python3'
    subprocess.run([py, '-m', 'unittest', 'discover', 'scripts'])


# -------------------------------------
# Command line options
# -------------------------------------
command_map = {'test': test,
               'types': check_types,
               }

# -------------------------------------
# Run script
# -------------------------------------

if __name__ == '__main__':
    main()

