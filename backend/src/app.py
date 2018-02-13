import json
import os

import flask
import flask_sslify

from backend.src.queries import attendance, demographics, engagement

app = flask.Flask(__name__,
                  static_folder="../../frontend/build/static",
                  template_folder="../../frontend/build")

# allow slash after endpoint
app.url_map.strict_slashes = False

# force HTTPS
if 'DYNO' in os.environ:
    sslify = flask_sslify.SSLify(app)


@app.route('/')
def render_react():
    return flask.send_from_directory('../../frontend/build', 'index.html')


@app.route('/api/test')
def api_test():
    return 'Server is running! Good luck debugging :O'


@app.route('/api/demographics/all_students')
def api_get_all_demographics():
    result = demographics.get_all()
    return flask.jsonify(result)


@app.route('/api/demographics/<int:student_id>')
def api_get_name(student_id: int):
    result = demographics.get(student_id)
    return return_json(result)


@app.route('/api/engagement/<int:student_id>')
def api_get_engagement(student_id: int):
    result = engagement.get(student_id)
    return return_json(result)


@app.route('/api/attendance/<int:student_id>')
def api_get_attendance(student_id: int):
    result = attendance.get(student_id)
    return return_json(result)


def return_json(result):
    if result is None:
        flask.abort(404)
    else:
        return json.dumps(result), 200
