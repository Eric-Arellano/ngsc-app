#!/usr/bin/env bash
# usage:
#   run: `./frontend.sh`
#   run detached: `./frontend.sh detached`
#   kill detached: `./frontend.sh kill`
#   install: `./frontend.sh install`
#   build: `./frontend.sh build`
#   types: `./frontend.sh types`

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
  elif [ "$flag" == "build" ]; then
    build
  elif [ "$flag" == "types" ]; then
    check_types
  else
    run
  fi
}

run() {
  yarn start
}

run_detached() {
  run &>/dev/null &
}

kill_detached() {
  lsof -n -i4TCP:3000 | grep LISTEN | awk '{ print $2 }' | xargs kill
}

install() {
  yarn install
}


build() {
  yarn build
}

check_types() {
  yarn flow
}



cd frontend/
main "$@"
cd ../
