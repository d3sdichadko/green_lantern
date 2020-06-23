from flask import Blueprint, current_app

simple_page = Blueprint("simple_page", __name__)


@simple_page.route("/")
def get_simple_page():
    return current_app.config["CONFIG_VALUE"]
