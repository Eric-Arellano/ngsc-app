import os

from apiclient import discovery
from httplib2 import Http
from oauth2client.service_account import ServiceAccountCredentials

scopes = ['https://www.googleapis.com/auth/sqlservice.admin', 'https://www.googleapis.com/auth/spreadsheets.readonly']

def build_service():
    credentials = get_credentials()
    http_auth = credentials.authorize(Http())
    discoveryUrl = ('https://sheets.googleapis.com/$discovery/rest?'
                    'version=v4')
    return discovery.build('sheets', 'v4', http=http_auth,
                           discoveryServiceUrl=discoveryUrl)


def get_credentials():
    current_dir = os.getcwd()
    credential_path = os.path.join(current_dir, 'service_key.json')
    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        credential_path, scopes)
    return credentials