#!/usr/bin/env bash
# usage:
#   run: `./backend.sh`
#   run detached: `./backend.sh detached`
#   kill detached: `./backend.sh kill`
#   install: `./backend.sh install`
#   types: `./backend.sh types`

if [ $# -gt 0 ]; then
  flag=$1
fi;

main() {
  source backend/bin/activate
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

run() {
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
  cd backend/
  mypy --strict-optional --ignore-missing-imports --package src
  cd ../
}


main "$@"
