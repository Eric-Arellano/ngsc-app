# TODO: convert this to Flask Plus
import flask

from backend.src.sheets_commands import hide_values

app = flask.Flask(__name__,
                  static_folder="../../frontend/build/static",
                  template_folder="../../frontend/build")
app.url_map.strict_slashes = False


@app.route('/api/sheets/hide_ids')
def api_copy_file():
    hide_values.hide_all_ids()
