"""
Utilities to interface with processes and ports.
"""

import subprocess
from typing import NewType

from scripts.utils import prereq_checker, sys_calls


Port = NewType('Port', int)
PID = NewType('PID', int)


# -----------------------------------------------------------------
# Check prereqs installed
# -----------------------------------------------------------------

def check_prereqs_installed() -> None:
    """
    Confirm all required software installed.
    """
    prereq_checker.check_is_installed(['grep', 'awk'])
    prereq_checker.check_is_installed(['lsof', 'kill'], windows_support=False)
    prereq_checker.check_is_installed(['netstat', 'tskill', 'findstr'], posix_support=False)
    sys_calls.check_prereqs_installed()


# -----------------------------------------------------------------
# Networking
# -----------------------------------------------------------------

def find_pid_on_port(port: Port) -> PID:
    """
    Finds and returns PID of process listening on specified port.
    """
    # determine environment
    if sys_calls.is_windows_environment():
        command = f"netstat -aon | findstr :{port} | awk '{{ print $5 }}'"
    else:
        command = f"lsof -n -i4TCP:{port} | grep LISTEN | awk '{{ print $2 }}'"
    # find PID
    pid = subprocess.check_output(command, shell=True).strip()
    if not pid:
        raise SystemExit(f'No process found running on port {port}.')
    return pid


# -----------------------------------------------------------------
# Manage processes
# -----------------------------------------------------------------

def kill_process(pid: PID) -> None:
    """
    Kills the specified PID.
    """
    if sys_calls.is_windows_environment():
        command = 'tskill'
    else:
        command = 'kill'
    subprocess.run([command, pid])
