
from __future__ import unicode_literals, print_function, absolute_import

import flask
import os
import os.path
import json
import sjoh.flask
import logging
import asgard


app = asgard.Asgard(__name__, flask_parameters={"static_folder": None})

# load configuration about files and folders
folder = os.path.dirname(__file__)
fc = os.path.join(folder, "filesconfig.json")
with open(fc, "rb") as file_:
    fc_content = file_.read().decode("utf8")
files_config = json.loads(fc_content)
# register static folders
for s in files_config["static_folders"]:
    def gen_fct(folder):
        def static_route(path):
            return flask.send_from_directory(folder, path)
        return static_route
    route = "/" + s + "/<path:path>"
    app.web_app.add_url_rule(route, "static:"+s, gen_fct(s))

@app.web_app.route("/")
def main():
    return flask.render_template("index.html", files_config=files_config)

@app.web_app.json("/hello")
def hello():
    return "Hello"

