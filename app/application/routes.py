import os
from flask import Blueprint, send_from_directory

route_blueprint = Blueprint("route_blueprint", __name__, static_folder="../../build", static_url_path="/")


@route_blueprint.route("/", defaults={"path": ""}, methods=["GET"])
@route_blueprint.route("/<path:path>")
def serve_react_app(path):
    if path != "" and os.path.exists(route_blueprint.static_folder + "/" + path):
        return send_from_directory(route_blueprint.static_folder, path)
    else:
        return send_from_directory(route_blueprint.static_folder, "index.html")