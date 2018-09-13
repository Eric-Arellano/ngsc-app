# NGSC App
App to allow students in NGSC program to check their participation status, leadership, and upcoming events in the program. 

Uses React.js for frontend, Python 3 and Flask for backend server, and Google Docs API for data source.

## Prerequisites
See [the install guide](install_guide.md) for what must be installed.

## Usage

#### First time setup
`./ngsc install`

#### Run app
1. `./ngsc`, starts the app at `localhost:3000` (go to this in your browser)
1. `./ngsc stop`, stops the app

#### After making changes
`./ngsc green`, make sure your changes pass tests and linters

#### Additional commands
`./ngsc --help`, lists all possible commands

#### Specifying target
Most commands default to running on every possible environment (scripts, backend, and frontend). 
You can often specify a specific target with `--backend` (`-b`), `--frontend` (`-f`), or `--scripts` (`-s`).
