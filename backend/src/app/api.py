import json

import flask

from backend.src.app import attendance, demographics, engagement

app_api = flask.Blueprint('app_api', __name__)


@app_api.route('/demographics/all_students')
def api_get_all_demographics():
    result = demographics.get_all()
    return flask.jsonify(result)


@app_api.route('/demographics/all_students_encrypted')
def api_get_all_demographics_encrypted():
    result = demographics.get_all_encrypted()
    return flask.jsonify(result)


@app_api.route('/demographics/<asurite>')
def api_get_name(asurite: str):
    result = demographics.get(asurite)
    return return_json(result)


@app_api.route('/engagement/<asurite>')
def api_get_engagement(asurite: str):
    result = engagement.get(asurite)
    return return_json(result)


@app_api.route('/attendance/<asurite>')
def api_get_attendance(asurite: str):
    result = attendance.get(asurite)
    return return_json(result)


def return_json(result):
    if result is None:
        flask.abort(404)
    else:
        return json.dumps(result), 200
