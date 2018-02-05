#!/usr/bin/env bash
# usage:
# run...
#     run: `./backend.sh`
#     run detached: `./backend.sh detached`
#     kill detached: `./backend.sh kill`
# install...
#     install: `./backend.sh install`
#     build: `./frontend.sh build`
# test...
#   check types: `./backend.sh types`
# dependency management...
#   catchup to server changes: `./backend.sh catchup`
#   view outdated: `./backend.sh outdated`
#   add: `./backend.sh add [pip-package]`
#   upgrade: `./backend.sh upgrade [pip-package]`
#   remove: `./backend.sh remove [pip-package]`


# -------------------------------------
# Check prereqs installed
# -------------------------------------
# determine if Windows
[[ $(uname -s) == MINGW64_NT* ]] && WINDOWS=true || WINDOWS=false

# Check universal requirements
hash node 2>/dev/null || { echo >&2 "Node.js must be installed."; exit 1; }
hash npm 2>/dev/null || { echo >&2 "NPM must be installed."; exit 1; }
hash yarn 2>/dev/null || { echo >&2 "Yarn must be installed."; exit 1; }

# Check non-Windows requirements
if [ "$WINDOWS" = false ] ; then
  hash lsof 2>/dev/null || { echo >&2 "lsof linux utility should be installed."; exit 1; }
fi

# Check Windows requirements
if [ "$WINDOWS" = true ] ; then
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


# -------------------------------------
# Run commands
# -------------------------------------

run() {
  yarn start
}

run_detached() {
  run &>/dev/null &
}

kill_detached() {
  if [ "$WINDOWS" = true ] ; then
    netstat -aon | findstr :3000 | awk '{ print $5 }' | xargs tskill
  else
    lsof -n -i4TCP:3000 | grep LISTEN | awk '{ print $2 }' | xargs kill
  fi
}

# -------------------------------------
# Install commands
# -------------------------------------

install() {
  yarn install
}

build() {
  yarn build
}

# -------------------------------------
# Test commands
# -------------------------------------

check_types() {
  yarn flow
}

# -------------------------------------
# Dependency management commands
# -------------------------------------

remind_to_commit() {
  commit_message="
  -----------------------------------------------------------

  Remember to commit and push your changes made to package.json & yarn.lock."
  echo "$commit_message"
}

catchup() {
  yarn install
}

list_outdated() {
  yarn outdated
}

add_dependency() {
  yarn add $1
  remind_to_commit
}

upgrade_dependency() {
  yarn upgrade $1
  remind_to_commit
}

remove_dependency() {
  yarn remove $1
  remind_to_commit
}

# -------------------------------------
# Determine run option
# -------------------------------------

if [ $# -gt 0 ]; then
  flag=$1
fi;

main() {
  cd frontend/
  # run
  if [ "$flag" == "detached" ]; then
    run_detached
  elif [ "$flag" == "kill" ]; then
    kill_detached
  # install
  elif [ "$flag" == "install" ]; then
    install
  elif [ "$flag" == "build" ]; then
    build
  # test
  elif [ "$flag" == "types" ]; then
    check_types
  # dependency managment
  elif [ "$flag" == "catchup" ]; then
    catchup
  elif [ "$flag" == "outdated" ]; then
    list_outdated
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
  cd ../
}


main "$@"
