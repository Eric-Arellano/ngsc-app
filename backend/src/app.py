from __future__ import print_function
import flask
import json

from .models import Requirement
from .queries import get_name, get_engagement

app = flask.Flask(__name__)


@app.route('/')
def hello_world():
    r1 = Requirement(name="PT", type_="Civil-Mil", hours=3, status="Accepted")
    return r1.name


@app.route('/api/student_info/<int:id>')
def api_get_name(id: int):
    result = get_name(id)
    return return_json(result)


@app.route('/api/engagement/<int:id>')
def api_get_engagement(id: int):
    result = get_engagement(id)
    return return_json(result)


def return_json(result):
    if result is None:
        flask.abort(404)
    else:
        return json.dumps(result), 200
