"""
Authentication to connect to Google Sheets API.
"""

import os

from googleapiclient import discovery
from httplib2 import Http
from oauth2client.service_account import ServiceAccountCredentials

scopes = ['https://www.googleapis.com/auth/sqlservice.admin',
          'https://www.googleapis.com/auth/spreadsheets',
          'https://www.googleapis.com/auth/drive']


def build_sheets_service() -> discovery.Resource:
    """
    Instantiate Google Sheets service with correct credentials and API keys.
    """
    credentials = get_credentials()
    http_auth = credentials.authorize(Http())
    discovery_url = ('https://sheets.googleapis.com/$discovery/rest?'
                     'version=v4')
    return discovery.build('sheets', 'v4', http=http_auth,
                           discoveryServiceUrl=discovery_url)


def build_drive_service() -> discovery.Resource:
    """
    Instantiate Google Drive service with correct credentials and API keys.
    """
    credentials = get_credentials()
    http_auth = credentials.authorize(Http())
    return discovery.build('drive', 'v3', http=http_auth)


def get_credentials() -> ServiceAccountCredentials:
    """
    Load API keys for Google Sheets.
    """
    current_dir = os.getcwd()
    credential_path = os.path.join(current_dir, 'backend/service_key.json')
    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        credential_path, scopes)
    return credentials
