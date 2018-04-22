import flask

from backend.src.data import mime_types
from backend.src.drive_commands import find

admin_api = flask.Blueprint('admin_api', __name__)


@admin_api.route('/test')
def api_test():
    """
    Throw away text connecting google drive api
    """
    return find.resource(file_name='Same same but different',
                         parent_folder_id='1QOsOQq3FMYfpXau6v3ubem5wrC97yWwo',
                         mime_type=mime_types.gdoc)


@admin_api.route('/copy/file', methods=['POST'])
def api_copy_file():
    raise NotImplementedError


@admin_api.route('/copy/folder', methods=['POST'])
def api_copy_folder():
    raise NotImplementedError


@admin_api.route('/create/file', methods=['POST'])
def api_create_file():
    raise NotImplementedError


@admin_api.route('/create/folder', methods=['POST'])
def api_create_folder():
    raise NotImplementedError


@admin_api.route('/move/file', methods=['POST'])
def api_move_file():
    raise NotImplementedError


@admin_api.route('/move/folder', methods=['POST'])
def api_move_folder():
    raise NotImplementedError


@admin_api.route('/rename/file', methods=['POST'])
def api_rename_file():
    raise NotImplementedError


@admin_api.route('/rename/folder', methods=['POST'])
def api_rename_folder():
    raise NotImplementedError


@admin_api.route('/remove/file', methods=['POST'])
def api_remove_file():
    raise NotImplementedError


@admin_api.route('/remove/folder', methods=['POST'])
def api_remove_folder():
    raise NotImplementedError
