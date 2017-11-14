# NGSC Service Hours
Simple app to expose students' service hours through Google Docs API.

## To install

### Requirements
1. Python 3.6
    1. With Mac, use HomeBrew and `brew install python3`
1. NVM (Node Version Manager) 
1. Node.js (use NVM)
    1. `nvm install 8.1.4`
    1. `nvm use 8.1.4`
1. Yarn
    1. `npm install -g yarn`

#### Backend
1. `cd backend/`
1. Make a virtual environment
    1. On Mac, `python3 -m venv ./`
    1. On Windows, `c:\Python35\python -m venv ./` 
1. `pip install -r requirements.txt`

#### Frontend
1. `cd frontend/`
1. `yarn install`

## To start

#### Backend
1. `cd backend/`
1. activate virtual environment
    1. On Mac, `source bin/activate`
    1. On Windows, `\Scripts\activate.bat`
1. `export FLASK_APP=src/app.py`
1. `flask run`

#### Frontend
1. `cd frontend/`
1. `yarn start`
