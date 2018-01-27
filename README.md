# NGSC Service Hours
App to allow students in NGSC program to check their participation and  service hours. 

Uses React for frontend, Python 3 and Flask for backend server, and Google Docs API for data source.

## To install

### PC setup
See this PowerPoint, and particularly the slides on Solution 2: Git Bash, for instructions on downloading Git Bash and setting up your PC to run this program https://docs.google.com/presentation/d/1pAoLLMqqH6JGG9ILwlhKMwVzUVzux9bFmZINPJWeW9Q/edit?usp=sharing.

### Mac setup
You're highly recommended to use HomeBrew, which is a package manager that makes it really easy to install and update software. Install HomeBrew with `/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"` pasted into a Termianl window.

### Install software
1. Git
    1. On Mac, `brew install git`
    1. On PC, download at https://git-scm.com/downloads
        1. Accept every default setting, except for choosing your default text editor:
            1. The default, Vim, is great but really confusing if you've never used it.
            1. Recommended to download the app Visual Studio Code and then choose that as your option.
1. Python 3.6
    1. On Mac, use HomeBrew `brew install python3`
    2. On Windows, download at https://www.python.org/downloads/ 
        1. Make sure to _check ON the option to add python.exe to your PATH variable._
1. Node.js & NPM
    1. On Mac, `brew install node`
    1. On PC, download at https://nodejs.org/en/ 
        1. Choose the most current version
        1. Accept default settings
1. Yarn
    1. On Mac, use Homebrew `brew install yarn`
    1. On PC, download the installer from https://yarnpkg.com/en/docs/install
1. Heroku CLI (command line interface)
    1. On Mac, use Homebrew `brew install heroku`
    1. On PC, download the 64 bit installer from https://devcenter.heroku.com/articles/heroku-cli
        1. Accept defaults

### Install app
1. `./backend.sh install`
1. `./frontend.sh install`

### Update app (whenever new dependencies added)
1. `./backend.sh update`
1. `./frontend.sh update`


## To start

### Run normally
1. `./backend.sh`
1. `./frontend.sh` (in a new tab, since the backend server will have taken over the first terminal)

### Run in detached mode
This means it doesn't output to the console, and you can still use that terminal for other things. For example, you only need one terminal to run the app this way, unlike normally where you need two.
1. `./backend.sh detached`
1. `./frontend.sh detached`
1. When you're done, `./backend.sh kill`
1. When you're done, `./frontend.sh kill`

## To test

### Check types
We use tools to check the data types of the app, since JavaScript and Python are both dynamic and don't enforce type safety. 
1. `./backend.sh types`
1. `./frontend.sh types`

## To update static student info data
We are saving everyone's IDs, names, committees, mission teams, etc into a Python dictionary to avoid having to make an 
API call for that info, since it doesn't change often. Whenever a change happens to the Master spreadsheet, this 
needs to be updated.

1. `./update-demographics.sh`

## To deploy
1. `./deploy.sh`
