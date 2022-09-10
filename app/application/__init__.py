from flask import Flask
from flask_cors import CORS
from flask_smorest import Api
from . import routes, api

# init plugins
my_api = Api()


def init_app() -> Flask:
    # init app object
    app = Flask(__name__, static_folder="../../build", static_url_path="/")
    app.config.from_object("config.Config")

    # attach plugins
    my_api.init_app(app)

    with app.app_context():
        # return app object

        app.register_blueprint(routes.route_blueprint)
        my_api.register_blueprint(api.blp)

        CORS(app)
        return app
