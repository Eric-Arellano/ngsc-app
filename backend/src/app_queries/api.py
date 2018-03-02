import json

import flask

from backend.src.app_queries import attendance, demographics, engagement

app_api = flask.Blueprint('app_api', __name__)


@app_api.route('/demographics/all_students')
def api_get_all_demographics():
    result = demographics.get_all()
    return flask.jsonify(result)


@app_api.route('/demographics/<int:student_id>')
def api_get_name(student_id: int):
    result = demographics.get(student_id)
    return return_json(result)


@app_api.route('/engagement/<int:student_id>')
def api_get_engagement(student_id: int):
    result = engagement.get(student_id)
    return return_json(result)


@app_api.route('/attendance/<int:student_id>')
def api_get_attendance(student_id: int):
    result = attendance.get(student_id)
    return return_json(result)


def return_json(result):
    if result is None:
        flask.abort(404)
    else:
        return json.dumps(result), 200
