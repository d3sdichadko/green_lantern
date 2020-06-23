from flask import Flask
from flask_migrate import MigrateCommand
from flask_script import Server, Manager

from grocery_store.config import Config
from grocery_store.routes import users, goods, stores
from grocery_store.db import db


def make_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.register_blueprint(users)
    app.register_blueprint(goods)
    app.register_blueprint(stores)
    return app


def make_db(app):
    db.init_app(app)
    return db


def make_manager(app):
    manager = Manager(app)
    manager.add_command('runserver', Server(host=Config.HOST, port=Config.PORT))
    manager.add_command('db', MigrateCommand)
    return manager
