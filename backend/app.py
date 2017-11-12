from __future__ import print_function
import os
import flask
import json

from apiclient import discovery
from httplib2 import Http
from oauth2client import tools
from oauth2client.service_account import ServiceAccountCredentials

app = flask.Flask(__name__)

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


@app.route('/test')
def test_api_request():
    print("Testing testing")
    return True


# @app.route('/api/engagement/<int:student_id>')
# def get_engagement(student_id):


@app.route('/api/student_info/<int:id>')
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
    current_dir = os.getcwd()
    credential_path = os.path.join(current_dir, 'service_key.json')
    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        credential_path, scopes)
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
            return {'id': id, 'name': {'first': row[1], 'last': row[2]}}
    return None


def get_events(service):
    spreadsheet_id = ENGAGEMENT_2017_ID
    range_name = 'Responses!A2:Q'
    result = service.spreadsheets().values().get(
        spreadsheet_id=spreadsheet_id, range=range_name).execute()
    return result.get('values', [])


def get_approved_events(service):
    spreadsheet_id = ENGAGEMENT_2017_ID
    range_name = 'Requirements!A2:C'
    result = service.spreadsheets().values().get(
        spreadsheet_id=spreadsheet_id, range=range_name).execute()
    return result.get('values', [])


def get_events_by_id(service, id):
    events = get_events(service)
    all_events = []
    for row in events:
        if int(float(row[6])) == id:
            event_dict = {}
            event_dict.append('type', row[2])
            if row[1] == 'Accepted' or 'Reclassified':
                if row[2] == 'Service':
                    event_dict.append('hours', int(float(row[16])))
                elif row[2] == 'Civil-Mil':
                    event_dict.append('hours', 1)
                elif row[2] == 'Civil-Mil OR Service':
                    event_dict.append('hours', int(float(row[15])))
            event_dict.append('status', row[1])
            if row[12]:
                event_dict.append('name', row[12])
            elif row[13]:
                event_dict.append('name', row[13])
            elif row[14]:
                event_dict.append('name', row[14])
            all_events.append(event_dict)
    accepted_requirements = get_approved_events(service)
    accepted_service_hours = 0
    accepted_civil_mil = 0
    accepted_hours_found = False
    for row in accepted_requirements:
        if int(float(row[0])) == id:
            accepted_service_hours = row[1]
            accepted_civil_mil = row[2]
            accepted_hours_found = True
    if not accepted_hours_found:
        return None
    elif len(all_events) == 0:
        return None
    else:
        return {"id": id, "approvedService": accepted_service_hours, "approvedCivilMil": accepted_civil_mil,
                "requirements": event_dict}

#
# def main():
#     credentials = get_credentials()
#     # delegated_credentials = credentials.create_delegated('dkchen1@asu.edu')
#     http_auth = credentials.authorize(Http())
#     discoveryUrl = ('https://sheets.googleapis.com/$discovery/rest?'
#                     'version=v4')
#     service = discovery.build('sheets', 'v4', http=http_auth,
#                               discoveryServiceUrl=discoveryUrl)
#     values = get_names(service)
#
#     if not values:
#         print('No data found.')
#     else:
#         print('Last Name, First Name, Student ID:')
#         for row in values:
#             # Print columns A and E, which correspond to indices 0 and 4.
#             print('%s, %s, %s' % (row[0], row[1], row[2]))
#
#
# if __name__ == '__main__':
#     main()
