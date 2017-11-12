from __future__ import print_function
import httplib2
import os
import flask
import requests

from apiclient import discovery
from flask import render_template
from httplib2 import Http
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage
from oauth2client.service_account import ServiceAccountCredentials

scopes = ['https://www.googleapis.com/auth/sqlservice.admin', 'https://www.googleapis.com/auth/spreadsheets.readonly']

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

class Event:
    def __init__(self, name, type, hours, status):
        self.name = name
        self.type = type
        self.hours = hours
        self.status = status

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/sheets.googleapis.com-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Google Sheets API Python Quickstart'

app = flask.Flask(__name__)

@app.route('/test')
def test_api_request():
    print("Testing testing")
    return True

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

@app.route('/engagement/get_hours/<int:student_id>')
def get_hours(student_id):
    hours = 0
    return hours

@app.route('/engagement/get_all_events/<int:student_id>')
def get_all_events(student_id):
    events = Event()
    return events

@app.route('/engagement/get_civil_mil/<int:student_id>')
def get_civil_mil(student_id):
    return 0

@app.route('/verify_id/<int:student_id>')
def verify_id(student_id):
    return True

def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    current_dir = os.getcwd()
    credential_path = os.path.join(current_dir, 'service_key.json')
    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        credential_path, scopes)
    # credential_dir = os.path.join(home_dir, '.credentials')
    # if not os.path.exists(credential_dir):
    #     os.makedirs(credential_dir)
    # credential_path = os.path.join(credential_dir,
    #                                'sheets.googleapis.com-python-quickstart.json')
    #
    # store = Storage(credential_path)
    # credentials = store.get()
    # if not credentials or credentials.invalid:
    #     flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
    #     flow.user_agent = APPLICATION_NAME
    #     if flags:
    #         credentials = tools.run_flow(flow, store, flags)
    #     else: # Needed only for compatibility with Python 2.6
    #         credentials = tools.run(flow, store)
    #     print('Storing credentials to ' + credential_path)
    return credentials

def get_names(service):
    spreadsheetId = '1H5leinJFGT1SDfb2hqbDpQgSC_2GYr1HFwKPpzFZ1Js'
    rangeName = 'Master!A2:C'
    result = service.spreadsheets().values().get(
        spreadsheetId=spreadsheetId, range=rangeName).execute()
    return result.get('values', [])

def main():
    """Shows basic usage of the Sheets API.

    Creates a Sheets API service object and prints the names and majors of
    students in a sample spreadsheet:
    https://docs.google.com/spreadsheets/d/1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms/edit
    """
    credentials = get_credentials()
    # delegated_credentials = credentials.create_delegated('dkchen1@asu.edu')
    http_auth = credentials.authorize(Http())
    discoveryUrl = ('https://sheets.googleapis.com/$discovery/rest?'
                    'version=v4')
    service = discovery.build('sheets', 'v4', http=http_auth,
                              discoveryServiceUrl=discoveryUrl)
    values = get_names(service)

    if not values:
        print('No data found.')
    else:
        print('Last Name, First Name, Student ID:')
        for row in values:
            # Print columns A and E, which correspond to indices 0 and 4.
            print('%s, %s, %s' % (row[0], row[1], row[2]))


if __name__ == '__main__':
    main()

