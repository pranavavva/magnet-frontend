from flask import Flask

# init plugins

def init_app():
    # init app object
    app = Flask(__name__)
    app.config.from_object("config.Config")

    @app.route("/")
    def hello_world():
        return "<p>Hello World!</p>"

    # attach plugins

    # return app object
    return app
