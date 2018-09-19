"""
Authentication to connect to Google API.
"""

import os

import httplib2
from oauth2client import service_account

scopes = [
    "https://www.googleapis.com/auth/sqlservice.admin",
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive",
]


def get_auth() -> httplib2.Http:
    """
    Authenticate credentials.
    """
    credentials = get_credentials()
    return credentials.authorize(httplib2.Http())


def get_credentials() -> service_account.ServiceAccountCredentials:
    """
    Load API keys.
    """
    current_dir = os.getcwd()
    credential_path = os.path.join(current_dir, "backend/service_key.json")
    credentials = service_account.ServiceAccountCredentials.from_json_keyfile_name(
        credential_path, scopes
    )
    return credentials
