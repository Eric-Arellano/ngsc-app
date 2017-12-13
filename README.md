# NGSC Service Hours
Simple app to expose students' service hours through Google Docs API.

## To install

### Requirements
1. Python 3.6
    1. With Mac, use HomeBrew and `brew install python3`
    2. With Windows, download at https://www.python.org/downloads/ Make sure to _check off the option to add python.exe to your PATH variable._
1. NVM (Node Version Manager) 
    1. Installation instructions for Mac/Linux at https://github.com/creationix/nvm/blob/master/README.md
    2. If you're using Windows, installation instructions at https://github.com/coreybutler/nvm-windows
1. Node.js (use NVM):
    1. `nvm install 8.1.4`
    1. `nvm use 8.1.4`
1. Yarn
    1. `npm install --global yarn`

#### Backend
1. Change terminal/command prompt location to the `backend` directory (e.g. Run `cd backend/` if coming from the root directory for this code)
1. Make a virtual environment
    1. On Mac, `python3 -m venv ./`
    1. On Windows, `c:\Python35\python -m venv ./`
1. `cd ../`
1. activate virtual environment
    1. On Mac, `source backend/bin/activate`
    1. On Windows, `backend\Scripts\activate.bat`
1. `pip install -r requirements.txt`

#### Frontend
1. Change terminal/command prompt location to the `frontend` directory (e.g. Run `cd frontend/` if coming from the root directory for this code)
1. `yarn install`
1. `yarn build`

## To start

#### Backend
1. Activate virtual environment
    1. On Mac, `source backend/bin/activate`
    1. On Windows, `backend\Scripts\activate.bat`
1. Set the FLASK_APP environment variable
    1. On Mac, `export FLASK_APP=backend/src/app.py`
    1. On Windows, `set FLASK_APP=backend/src/app.py`
1. Start the Flask server - `flask run`

#### Frontend
1. Change terminal/command prompt location to the `frontend` directory (e.g. Run `cd frontend/` if coming from the root directory for this code)
1. `yarn start`

## To update static student info data
We are saving everyones' IDs, names, committees, mission teams, etc into a Python dictionary to avoid having to make an api call for that info, since it doesn't change often. Every month or two, we should update the values because we do sometimes make changes within the program.

To do so:
1. go to `/api/all_demographics`
1. copy this output into the file `backend/src/student_ids.py`
1. redeploy the app 

## To deploy
1. make a commit on master
1. login in to heroku CLI (ask Eric for credentials)
1. `git push heroku master`
