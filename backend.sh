#!/usr/bin/env bash
# usage:
# run...
#     run: `./backend.sh`
#     run detached: `./backend.sh detached`
#     kill detached: `./backend.sh kill`
# install...
#     install: `./backend.sh install`
# test...
#   check types: `./backend.sh types`
# dependency management...
#   catchup to server changes: `./backend.sh catchup`
#   view outdated: `./backend.sh outdated`
#   view dependency tree: `./backend.sh deptree`
#   add: `./backend.sh add [pip-package]`
#   upgrade: `./backend.sh upgrade [pip-package]`
#   remove: `./backend.sh remove [pip-package]`


# -------------------------------------
# Check prereqs installed & if Windows
# -------------------------------------
# determine if Windows
[[ $(uname -s) == MINGW64_NT* ]] && WINDOWS=true || WINDOWS=false

# Check non-Windows requirements
if [ "$WINDOWS" = false ] ; then
  hash python3 2>/dev/null || { echo >&2 "Python 3 must be installed."; exit 1; }
  hash lsof 2>/dev/null || { echo >&2 "lsof linux utility should be installed."; exit 1; }
fi

# Check Windows requirements
if [ "$WINDOWS" = true ] ; then
  hash python 2>/dev/null || { echo >&2 "Python must be installed and on your path."; exit 1; }
  hash netstat 2>/dev/null || { echo >&2 "netstat must be installed."; exit 1; }
  hash findstr 2>/dev/null || { echo >&2 "findstr must be installed."; exit 1; }
fi

# Check linux tools
support_linux_tools_error() {
  echo >&2 "$1 must be installed. If on PC, Git Bash should come installed with these!"
}
hash grep 2>/dev/null || { support_linux_tools_error "grep"; exit 1; }
hash awk 2>/dev/null || { support_linux_tools_error "awk"; exit 1; }
hash xargs 2>/dev/null || { support_linux_tools_error "xargs"; exit 1; }

# Venv helper
activate_venv() {
  if [ "$WINDOWS" = true ] ; then
    source backend/Scripts/activate
  else
    source backend/bin/activate
  fi
}


# -------------------------------------
# Run commands
# -------------------------------------

run() {
  activate_venv
  export FLASK_APP=backend/src/app.py
  flask run
}

run_detached() {
  run &>/dev/null &
}

kill_detached() {
  if [ "$WINDOWS" = true ] ; then
    netstat -aon | findstr :5000 | awk '{ print $5 }' | xargs tskill
  else
    lsof -n -i4TCP:5000 | grep LISTEN | awk '{ print $2 }' | xargs kill
  fi
}

# -------------------------------------
# Install commands
# -------------------------------------

install() {
  cd backend/
  if [ "$WINDOWS" = true ] ; then
    python -m venv ./
  else
    python3 -m venv ./
  fi
  cd ../
  activate_venv
  pip install -r requirements.txt
}

# -------------------------------------
# Test commands
# -------------------------------------

check_types() {
  activate_venv
  cd backend/
  mypy --strict-optional --ignore-missing-imports --package src
  cd ../
}

# -------------------------------------
# Dependency management commands
# -------------------------------------

check_for_requirements_divergence() {
  activate_venv
  # if diff $(pip freeze) requirements.txt; then    # TODO: fix comparison
    pip freeze | xargs pip uninstall -y
    pip install -r requirements.txt
  # fi
}

freeze_requirements() {
  activate_venv
  pip freeze > requirements.txt
  commit_message="
  -----------------------------------------------------------
  
  Remember to commit and push your changes made to requirements.txt."
  echo "$commit_message"
}

catchup() {
  activate_venv
  pip install -r requirements.txt
}

list_outdated() {
  activate_venv
  pip list --outdated --format=columns
}

dependency_tree() {
  activate_venv
  pipdeptree
}

add_dependency() {
  activate_venv
  check_for_requirements_divergence
  pip install $1
  freeze_requirements
}

upgrade_dependency() {
  activate_venv
  check_for_requirements_divergence
  pip install --upgrade $1
  freeze_requirements
}

remove_dependency() {
  activate_venv
  check_for_requirements_divergence
  pip uninstall $1
  freeze_requirements
}


# -------------------------------------
# Determine run option
# -------------------------------------

if [ $# -gt 0 ]; then
  flag=$1
fi;

main() {
  # run
  if [ "$flag" == "detached" ]; then
    run_detached
  elif [ "$flag" == "kill" ]; then
    kill_detached
  # install
  elif [ "$flag" == "install" ]; then
    install
  # test
  elif [ "$flag" == "types" ]; then
    check_types
  # dependency managment
  elif [ "$flag" == "catchup" ]; then
    catchup
  elif [ "$flag" == "outdated" ]; then
    list_outdated
  elif [ "$flag" == "deptree" ]; then
    dependency_tree
  elif [ "$flag" == "add" ]; then
    add_dependency $2
  elif [ "$flag" == "upgrade" ]; then
    upgrade_dependency $2
  elif [ "$flag" == "remove" ]; then
    remove_dependency $2
  # run pt 2
  else
    run
  fi
}

main "$@"
