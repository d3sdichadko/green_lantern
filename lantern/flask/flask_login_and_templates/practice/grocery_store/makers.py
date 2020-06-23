from flask import Flask
from flask_migrate import MigrateCommand
from flask_script import Server, Manager
from flask_login import LoginManager

from grocery_store.config import Config
from grocery_store.models import User
from grocery_store.routes import users, goods, stores, auth, main, goods_page
from grocery_store.database import db
from grocery_store.commands import Populate, PopulateOrders


def make_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.register_blueprint(users)
    app.register_blueprint(goods)
    app.register_blueprint(stores)
    app.register_blueprint(auth)
    app.register_blueprint(main)
    app.register_blueprint(goods_page)
    return app


def make_db(app):
    db.init_app(app)
    return db


def make_manager(app):
    manager = Manager(app)
    manager.add_command('runserver', Server(host=Config.HOST, port=Config.PORT))
    manager.add_command('db', MigrateCommand)
    manager.add_command('populate', Populate)
    manager.add_command('populate_orders', PopulateOrders)
    return manager


def make_login_manager(app):
    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    return login_manager
