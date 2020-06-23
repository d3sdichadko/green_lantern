from flask import Blueprint

module_1 = Blueprint('module_1', __name__)


@module_1.route("/")
def get_method():
    return "Hello from module 1"
