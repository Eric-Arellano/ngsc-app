# TODO: convert this to Flask Plus
import json

import flask

from backend.src.app_queries import attendance, demographics, engagement

app = flask.Flask(__name__,
                  static_folder="../../frontend/build/static",
                  template_folder="../../frontend/build")


@app.route('/api/app/demographics/all_students')
def api_get_all_demographics():
    result = demographics.get_all()
    return flask.jsonify(result)


@app.route('/api/app/demographics/<int:student_id>')
def api_get_name(student_id: int):
    result = demographics.get(student_id)
    return return_json(result)


@app.route('/api/app/engagement/<int:student_id>')
def api_get_engagement(student_id: int):
    result = engagement.get(student_id)
    return return_json(result)


@app.route('/api/app/attendance/<int:student_id>')
def api_get_attendance(student_id: int):
    result = attendance.get(student_id)
    return return_json(result)


def return_json(result):
    if result is None:
        flask.abort(404)
    else:
        return json.dumps(result), 200
