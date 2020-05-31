import logging

from flask import Flask
from sqlalchemy_utils import create_database, database_exists

from .config import Config
from .models import db, User, Good, Store
from .populate_data import get_users, get_goods, get_stores


def get_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)-6s %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    with app.app_context():
        if not database_exists(db.engine.url):
            logging.info(f'Database "{Config.DB_NAME}" does not exist')
            create_database(db.engine.url)
            logging.info(f'Creating database "{Config.DB_NAME}"...')
            logging.info("Database successfully created")
        db.create_all()
        logging.info(f'Database "{Config.DB_NAME}" exists')
        logging.info("Connection to database...")
        logging.info("Connection succeeded!")

    with app.app_context():
        users = get_users()
        goods = get_goods()
        stores = get_stores()
        for user in users:
            db.session.add(User(**user))
        for good in goods:
            db.session.add(Good(**good))
        for store in stores:
            db.session.add(Store(**store))
        db.session.commit()
        logging.info(f"Data added to database successfully")

    return app
