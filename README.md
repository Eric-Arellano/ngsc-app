# NGSC App
App to allow students in NGSC program to check their participation status, internships, and upcoming events in the program. 

Uses React for frontend, Python 3 and Flask for backend server, and Google Docs API for data source.

## Prerequisites

### Install software on Mac
1. HomeBrew package manager: `/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`
1. Git: `brew install git`
1. Python 3.7: `brew install python3`
1. Pipenv: `pip3 install pipenv`
1. Node.js: `brew install node`
1. Yarn package manager: `brew install yarn`
1. Heroku: `brew install heroku`

### Install software on PC
See [this PowerPoint](https://docs.google.com/presentation/d/1pAoLLMqqH6JGG9ILwlhKMwVzUVzux9bFmZINPJWeW9Q/edit?usp=sharing) 
for further context on how to get this project working effectively on a PC.

1. Git & Git Bash, https://git-scm.com/downloads
    1. Accept every default setting, except for choosing your default text editor:
        1. The default, Vim, is great but confusing if you've never used it.
        1. Recommended to download the app Visual Studio Code and then choose that as your option.
1. Python 3.7, https://www.python.org/downloads/ 
    1. Check on the option to add python.exe to your PATH variable.
1. Pipenv: `pip install pipenv`
1. Node.js, https://nodejs.org/en/ 
    1. Choose the most current version
    1. Accept default settings
1. Yarn, installer from https://yarnpkg.com/en/docs/install
1. Heroku, 64 bit installer from https://devcenter.heroku.com/articles/heroku-cli
    1. Accept defaults
    
### Running commands on PC
Use Git Bash instead of Command Prompt, because Git Bash offers Unix-style tools.

## Basic Usage

#### First time setup
`./ngsc install`

#### Run app
1. `./ngsc`, starts the app at `localhost:3000` (go to this in your browser)
1. `./ngsc stop`, stops the app

#### Making changes
1. `./ngsc green`, make sure your changes pass tests and linters

## Advanced Usage
There are many different ways to run this application, such as only starting the backend server or only starting the frontend server.

#### Understanding the below syntax
You will encounter these symbols:
* `a|b` = a or b. You must choose one.
* `[a]` = a is optional. You can add it as an argument if you'd like, otherwise the defaults will be used. 

#### Targeting environment
Most of these commands default to running on every possible environment (scripts, backend, and frontend). 
You can often specify a specific target with `--backend` (`-b`), `--frontend` (`-f`), or `--scripts` (`-s`).

### Install
* first-time setup: `./ngsc install [--backend|frontend]`
* reinstall: `./ngsc reinstall [--backend|frontend]`

### Run
* Start app: `./ngsc [--backend|frontend]`
    * Targeting the `backend` or `frontend` will output the status of the server to the console, unlike how we normally 
    hide it with `./ngsc`. This is really useful for debugging!
* Stop app: `./ngsc stop [--backend|frontend]`

### Test
* Run all tests & linters `./ngsc green [--backend|frontend|scripts]`
* Run unit tests: `./ngsc test [--backend|fronted|scripts]`
* Check types: `./ngsc types [--backend|frontend|scripts]`


### Deploy
`./ngsc deploy`

### Update static student info
Whenever a change happens to the Master spreadsheet, this script needs to be called.

1. `./ngsc student-info`
1. `./ngsc deploy`

### Setup new semester
Run these scripts to setup the new semester's Google Drive system.

1. `./ngsc setup-semester`
1. `./ngsc share-drive`

If you need to rebuild the rosters, e.g. after freshmen are assigned to their committees:

`./ngsc rebuild-rosters`

### Dependency management
* View outdated dependencies: `./ngsc outdated [--backend|frontend]`
* View dependency tree: `./ngsc deptree [--backend]` (not supported on frontend)
* Add package(s): `./ngsc add package1 [package2...] --backend|frontend`
* Upgrade package(s): `./ngsc upgrade package1 [package2...] --backend|frontend`
* Remove package(s): `./ngsc remove package1 [package2...] --backend|frontend`
