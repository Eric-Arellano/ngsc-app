# TODO: convert this to Flask Plus

import flask

from backend.src.drive_commands import copy, create, move, remove, rename

app = flask.Flask(__name__,
                  static_folder="../../frontend/build/static",
                  template_folder="../../frontend/build")
app.url_map.strict_slashes = False


@app.route('/api/drive/copy/file', methods=['POST'])
def api_copy_file():
    data = flask.request.get_json()
    copy.file(data)


@app.route('/api/drive/copy/folder', methods=['POST'])
def api_copy_folder():
    data = flask.request.get_json()
    copy.folder(data)


@app.route('/api/drive/create/file', methods=['POST'])
def api_create_file():
    data = flask.request.get_json()
    create.file(data)


@app.route('/api/drive/create/folder', methods=['POST'])
def api_create_folder():
    data = flask.request.get_json()
    create.folder(data)


@app.route('/api/drive/move/file', methods=['POST'])
def api_move_file():
    data = flask.request.get_json()
    move.file(data)


@app.route('/api/drive/move/folder', methods=['POST'])
def api_move_folder():
    data = flask.request.get_json()
    move.folder(data)


@app.route('/api/drive/rename/file', methods=['POST'])
def api_rename_file():
    data = flask.request.get_json()
    rename.file(data)


@app.route('/api/drive/rename/folder', methods=['POST'])
def api_rename_folder():
    data = flask.request.get_json()
    rename.folder(data)


@app.route('/api/drive/remove/file', methods=['POST'])
def api_remove_file():
    data = flask.request.get_json()
    remove.file(data)


@app.route('/api/drive/remove/folder', methods=['POST'])
def api_remove_folder():
    data = flask.request.get_json()
    remove.folder(data)
