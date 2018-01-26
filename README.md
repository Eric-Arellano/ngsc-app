# NGSC Service Hours
App to allow students in NGSC program to check their participation and  service hours. 

Uses React for frontend, Python 3 and Flask for backend server, and Google Docs API for data source.

## To install

### Install software
1. Git
1. Python 3.6
    1. With Mac, use HomeBrew and `brew install python3`
    2. With Windows, download at https://www.python.org/downloads/ 
        1. Make sure to _check off the option to add python.exe to your PATH variable._
1. NVM (Node Version Manager) 
    1. Installation instructions for Mac/Linux at https://github.com/creationix/nvm/blob/master/README.md
    2. If you're using Windows, installation instructions at https://github.com/coreybutler/nvm-windows
1. Node.js (use NVM):
    1. `nvm install 8.1.4`
    1. `nvm use 8.1.4`
1. Yarn
    1. `npm install --global yarn`
1. Heroku CLI (command line interface)
1. JQ utility
    1. On Mac, `brew install jq`
    1. On PC, go to https://stedolan.github.io/jq/download/

### Install scripts (Mac)
1. `backend.sh install`
1. `frontend.sh install`

### Backend (PC)
1. Change terminal/command prompt location to the `backend` directory (e.g. Run `cd backend/` if coming from the root directory for this code)
1. Make a virtual environment, `python -m venv ./`
1. `cd ../`
1. activate virtual environment, `backend\Scripts\activate.bat`
1. Install dependencies,`pip install -r requirements.txt`

### Frontend (PC)
1. Change terminal/command prompt location to the `frontend` directory (e.g. run `cd frontend/` if coming from the root directory for this code)
1. `yarn install`

## To start

#### On Mac
1. `./backend.sh`
1. `./frontend.sh`

#### Backend (PC)
1. Activate virtual environment, `backend\Scripts\activate.bat`
1. Set the FLASK_APP environment variable, `set FLASK_APP=backend/src/app.py`
1. Start the Flask server - `flask run`

#### Frontend (PC)
1. Change terminal/command prompt location to the `frontend` directory (e.g. run `cd frontend/` if coming from the root directory for this code)
1. Start Yarn server - `yarn start`

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
