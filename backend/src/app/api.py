import json

import flask

from backend.src.app import attendance, calculator, demographics, engagement

app_api = flask.Blueprint("app_api", __name__)


@app_api.route("/demographics/all_students")
def api_get_all_demographics():
    result = demographics.get_all()
    return flask.jsonify(result)


@app_api.route("/demographics/all_students_encrypted")
def api_get_all_demographics_encrypted():
    result = demographics.get_all_encrypted()
    return flask.jsonify(result)


@app_api.route("/demographics/<asurite>")
def api_get_name(asurite: str):
    result = demographics.get(asurite)
    return return_json(result)


@app_api.route("/engagement/<asurite>")
def api_get_engagement(asurite: str):
    result = engagement.get(asurite)
    return return_json(result)


@app_api.route("/attendance/<asurite>")
def api_get_attendance(asurite: str):
    result = attendance.get(asurite)
    return return_json(result)


@app_api.route("/scholarship", methods=["POST"])
def api_post_scholarship():
    payload = flask.request.get_json()
    award_amount = calculator.calculate_award(
        residency_status=calculator.Residency(payload["residency"]),
        scholarship_amounts=payload["scholarships"],
    )
    return flask.jsonify({"award_amount": award_amount})


def return_json(result):
    if result is None:
        flask.abort(404)
    else:
        return json.dumps(result), 200
