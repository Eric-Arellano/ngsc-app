# NGSC Service Hours
App to allow students in NGSC program to check their participation and  service hours. 

Uses React for frontend, Python 3 and Flask for backend server, and Google Docs API for data source.

## To install

### PC setup
https://docs.google.com/presentation/d/1pAoLLMqqH6JGG9ILwlhKMwVzUVzux9bFmZINPJWeW9Q/edit?usp=sharing

### Install software
1. Git, https://git-scm.com/downloads
    1. On PC, accept every default setting, except for choosing your default text editor:
        1. Default, Vim, is great but really really confusing
        1. Recommended to download the app Visual Studio Code and then choose that as your option.
1. Python 3.6
    1. On Mac, use HomeBrew `brew install python3`
    2. On Windows, download at https://www.python.org/downloads/ 
        1. Make sure to _check ON the option to add python.exe to your PATH variable._
1. Node.js & NPM, https://nodejs.org/en/
    1. Choose the most current version
    1. Accept default settings
1. Yarn, https://yarnpkg.com/en/docs/install
    1. On Mac, use Homebrew `brew install yarn`
    1. On PC, probably easiest to download the installer
1. Heroku CLI (command line interface)

### Install app
1. `backend.sh install`
1. `frontend.sh install`


## To start

### Run normally
1. `./backend.sh`
1. In a new tab also in the root directory, `./frontend.sh`


### Run in detached mode
This means it doesn't output to the console, and you can still use that terminal for other things. For example, you only need one terminal to run the app this way, unlike normally where you need two.
1. `backend.sh detached`
1. `frontend.sh detached`
1. When you're done, `backend.sh kill`
1. When you're done, `frontend.sh kill`

## To test

### Check types
We use tools to check the data types of the app, since JavaScript and Python are both "dynamic." 
1. `backend.sh types`
1. `frontend.sh types`

## To update static student info data
We are saving everyone's IDs, names, committees, mission teams, etc into a Python dictionary to avoid having to make an 
API call for that info, since it doesn't change often. Whenever a change happens to the Master spreadsheet, this 
needs to be updated.

1. `./update-demographics.sh`

## To deploy
1. make a commit on master
1. login in to Heroku CLI (ask Eric for credentials)
1. add Heroku as a git repo, `git remote add heroku https://git.heroku.com/ngsc-service-hours.git`
1. `git push heroku master`
