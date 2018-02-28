import flask

from backend.src.sheets_commands import asurite, hide_values, update_phones

sheets_api = flask.Blueprint('sheets_api', __name__)


@sheets_api.route('/hide/all_ids')
def api_hide_all_ids():
    hide_values.hide_all_ids()


@sheets_api.route('/asurite/all_attendance')
def api_convert_asurite():
    asurite.convert_all_ids_to_asurite()
    return "Success."


@sheets_api.route('/update_phones/all_attendance')
def api_update_phones():
    update_phones.update_all_phone_numbers()
    return "Success."
