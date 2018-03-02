import os

import flask
import flask_sslify

from backend.src.app_queries.api import app_api
from backend.src.drive_commands.api import drive_api
from backend.src.sheets_commands.api import sheets_api

app = flask.Flask(__name__,
                  static_folder="../../frontend/build/static",
                  template_folder="../../frontend/build")

# allow slash after endpoint
app.url_map.strict_slashes = False

# force HTTPS
if 'DYNO' in os.environ:
    sslify = flask_sslify.SSLify(app)

# register sub-APIs
app.register_blueprint(app_api, url_prefix='/api/app')
app.register_blueprint(drive_api, url_prefix='/api/drive')
app.register_blueprint(sheets_api, url_prefix='/api/sheets')


@app.route('/')
@app.route('/<path:path>')
def render_react(path):
    return flask.send_from_directory('../../frontend/build', 'index.html')


@app.route('/api/test')
def api_test():
    return 'Server is running! Good luck debugging :O'
