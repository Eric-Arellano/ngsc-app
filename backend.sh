#!/usr/bin/env bash
# usage:
#   run: `./backend.sh`
#   run detached: `./backend.sh detached`
#   kill detached: `./backend.sh kill`
#   install: `./backend.sh install`
#   types: `./backend.sh types`


# -------------------------------------
# Check prereqs installed
# -------------------------------------
hash python3 2>/dev/null || hash python 2>/dev/null || { echo >&2 "Python (3+) must be installed."; exit 1; }

hash lsof 2>/dev/null || { support_linux_tools_error lsof; exit 1; }
hash grep 2>/dev/null || { support_linux_tools_error grep; exit 1; }
hash awk 2>/dev/null || { support_linux_tools_error awk; exit 1; }
hash xargs 2>/dev/null || { support_linux_tools_error xargs; exit 1; }

support_linux_tools_error() {
  echo >&2 "$1 must be installed. If on PC, please use Windows Subsytem for Linux."
}

# -------------------------------------
# Determine run option
# -------------------------------------

if [ $# -gt 0 ]; then
  flag=$1
fi;

main() {
  if [ "$flag" == "detached" ]; then
    run_detached
  elif [ "$flag" == "kill" ]; then
    kill_detached
  elif [ "$flag" == "install" ]; then
    install
  elif [ "$flag" == "types" ]; then
    check_types
  else
    run
  fi
}


# -------------------------------------
# Commands
# -------------------------------------

run() {
  source backend/bin/activate
  export FLASK_APP=backend/src/app.py
  flask run
}

run_detached() {
  run &>/dev/null &
}

kill_detached() {
  lsof -n -i4TCP:5000 | grep LISTEN | awk '{ print $2 }' | xargs kill
}

install() {
  cd backend/
  python3 -m venv ./
  cd ../
  source backend/bin/activate
  pip install -r requirements.txt
}

check_types() {
  source backend/bin/activate
  cd backend/
  mypy --strict-optional --ignore-missing-imports --package src
  cd ../
}


main "$@"
