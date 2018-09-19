"""
Given ResourceID, generate accompanying link.
"""

ResourceID = str
URL = str


def gdoc(file_id: ResourceID) -> URL:
    return f"https://docs.google.com/document/d/{file_id}/edit"


def gsheet(file_id: ResourceID) -> URL:
    return f"https://docs.google.com/spreadsheets/d/{file_id}/edit"


def gslides(file_id: ResourceID) -> URL:
    return f"https://docs.google.com/presentation/d/{file_id}/edit"


def gform(file_id: ResourceID) -> URL:
    return f"https://docs.google.com/forms/d/{file_id}/edit"


def folder(folder_id: ResourceID) -> URL:
    return f"https://drive.google.com/drive/u/0/folders/{folder_id}"
