from __future__ import print_function
import flask
import json

from .queries import get_all_demographics, get_demographics, get_engagement, get_attendance_data

app = flask.Flask(__name__,
                  static_folder="../../frontend/build/static",
                  template_folder="../../frontend/build")
app.url_map.strict_slashes = False


@app.route('/')
def render_react():
    return flask.send_from_directory('../../frontend/build', 'index.html')


@app.route('/api/test')
def api_test():
    return 'Server is running! Good luck debugging :O'


@app.route('/api/all_demographics/')
def api_get_all_demographics():
    result = get_all_demographics()
    return flask.jsonify(result)


@app.route('/api/demographics/<int:id>')
def api_get_name(id: int):
    result = get_demographics(id)
    return return_json(result)


@app.route('/api/engagement/<int:id>')
def api_get_engagement(id: int):
    result = get_engagement(id)
    return return_json(result)

@app.route('/api/attendance/<int:id>')
def api_get_attendance(id: int):
    result = get_attendance_data(id)
    return return_json(result)

def return_json(result):
    if result is None:
        flask.abort(404)
    else:
        return json.dumps(result), 200
