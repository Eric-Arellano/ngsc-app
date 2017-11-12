from __future__ import print_function
import os
import flask
import json
import requests

from apiclient import discovery
from flask import render_template
from httplib2 import Http
from oauth2client import tools
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

MASTER_2017_ID = '1H5leinJFGT1SDfb2hqbDpQgSC_2GYr1HFwKPpzFZ1Js'
ENGAGEMENT_2017_ID = '1FBDR19w831QQ8XTFMns6qVzGEGTv1UU7NAoomTaJRLA'

app = flask.Flask(__name__)

@app.route('/test')
def test_api_request():
    print("Testing testing")
    return True

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

# @app.route('/api/engagement/<int:student_id>')
# def get_engagement(student_id):


@app.route('/api/student_id/<int:id>')
def get_name(id):
    credentials = get_credentials()
    http_auth = credentials.authorize(Http())
    discoveryUrl = ('https://sheets.googleapis.com/$discovery/rest?'
                    'version=v4')
    service = discovery.build('sheets', 'v4', http=http_auth,
                              discoveryServiceUrl=discoveryUrl)
    result = get_name_by_id(service, id)

    if result is None:
        flask.abort(404)
    else:
        return json.dumps(result), 200

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
    spreadsheet_id = MASTER_2017_ID
    range_name = 'Master!A2:C'
    result = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id, range=range_name).execute()
    return result.get('values', [])

def get_name_by_id(service, id):
    results = get_names(service)
    for row in results:
        if row[2] == id:
            return {'id': id, 'name' : {'first' : row[1], 'last' : row[2] }}
    return None

def get_events(service):
    spreadsheet_id = ENGAGEMENT_2017_ID
    range_name = 'Responses!A2:Q'
    result = service.spreadsheets().values().get(
        spreadsheet_id=spreadsheet_id, range=range_name).execute()
    return result.get('values', [])

# def get_event_by_id(service, id):
#     events = get_events(service)
#     approved_service_hours = 0
#     approved_civil_mil_event_count = 0
#     all_events = []
#     for row in events:
#         if row[6] == id:
#             eventDict = {}
#             if row[2] == 'Service':
#                 eventDict.append('type', 'Service')
#                 if row[1] == 'Approved':
#
#                 approved_service_hours += int(float(row[16]))
#

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

