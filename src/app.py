from flask import Flask

from src.constants import HEALTH_MSG


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)

    @app.route("/health")
    def api_health():
        return HEALTH_MSG

    return app
