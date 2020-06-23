from flask import Flask
from application.module1 import simple_page
from config import runtime_config


def create_app():
    """Initialize the core application."""
    app = Flask(__name__)
    app.config.from_object(runtime_config())
    app.register_blueprint(simple_page)
    return app
