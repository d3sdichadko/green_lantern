import inject
from flask import Flask

from errors import NoSuchUserError, my_error_handler, NoSuchStoreError
from fake_storage import FakeStorage
from routes import users_bl, goods_bl, stores_bl


def configure(binder):
    db = FakeStorage()
    binder.bind('DB', db)


def make_app():
    # configure our database
    inject.clear_and_configure(configure)

    app = Flask(__name__)
    # register blueprints and error handlers
    app.register_blueprint(users_bl)
    app.register_blueprint(goods_bl)
    app.register_blueprint(stores_bl)

    app.register_error_handler(NoSuchUserError, my_error_handler)
    app.register_error_handler(NoSuchStoreError, my_error_handler)
    return app
