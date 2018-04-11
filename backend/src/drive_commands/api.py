import flask

from backend.src.drive_commands import copy, create, move, remove, rename

drive_api = flask.Blueprint('drive_api', __name__)


@drive_api.route('/test')
def api_test():
    """
    Throw away text connecting google drive api
    """
    create.folder(folder_name='new folder')
    return create.file(file_name='new document')
    # service = build_drive_service()
    # results = service.files().list(
    #     pageSize=10, fields="nextPageToken, files(id, name)").execute()
    # items = results.get('files', [])
    # if not items:
    #     return 'No files found.'
    # else:
    #     output = 'Files:'
    #     for item in items:
    #         output += f"{item['name']} {item['id']}"
    #     return output


@drive_api.route('/copy/file', methods=['POST'])
def api_copy_file():
    data = flask.request.get_json()
    copy.file(data)


@drive_api.route('/copy/folder', methods=['POST'])
def api_copy_folder():
    data = flask.request.get_json()
    copy.folder(data)


@drive_api.route('/create/file', methods=['POST'])
def api_create_file():
    data = flask.request.get_json()
    create.file(data)


@drive_api.route('/create/folder', methods=['POST'])
def api_create_folder():
    data = flask.request.get_json()
    return create.folder(data)


@drive_api.route('/move/file', methods=['POST'])
def api_move_file():
    data = flask.request.get_json()
    move.file(data)


@drive_api.route('/move/folder', methods=['POST'])
def api_move_folder():
    data = flask.request.get_json()
    move.folder(data)


@drive_api.route('/rename/file', methods=['POST'])
def api_rename_file():
    data = flask.request.get_json()
    rename.file(data)


@drive_api.route('/rename/folder', methods=['POST'])
def api_rename_folder():
    data = flask.request.get_json()
    rename.folder(data)


@drive_api.route('/remove/file', methods=['POST'])
def api_remove_file():
    data = flask.request.get_json()
    remove.file(data)


@drive_api.route('/remove/folder', methods=['POST'])
def api_remove_folder():
    data = flask.request.get_json()
    remove.folder(data)
