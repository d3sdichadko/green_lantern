import csv
import logging
import os

from grocery_store.models import User, Good, Store, Order, OrderLine
from grocery_store.config import FIXTURES_DIR, Config
from sqlalchemy_utils import create_database, drop_database, database_exists

from random import randint, choice, sample, randrange

from flask_script import Command


USERS_FILENAME = os.path.join(FIXTURES_DIR, "users.csv")
GOODS_FILENAME = os.path.join(FIXTURES_DIR, "goods.csv")
STORES_FILENAME = os.path.join(FIXTURES_DIR, "stores.csv")
logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)-6s %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        # filename="logfile.log",  # if you want!!!
    )


def get_users():
    with open(USERS_FILENAME, "r") as f:
        reader = csv.DictReader(f)
        users = [user for user in reader]
    return users


def get_goods():
    with open(GOODS_FILENAME, "r") as f:
        reader = csv.DictReader(f)
        goods = [good for good in reader]
    return goods


def get_stores():
    with open(STORES_FILENAME, "r") as f:
        reader = csv.DictReader(f)
        stores = [store for store in reader]
    return stores


class Populate(Command):
    def run(self):
        from grocery_store import app, db
        with app.app_context():
            users = get_users()
            goods = get_goods()
            stores = get_stores()
            for user in users:
                db.session.add(User(**user))
            db.session.commit()
            for good in goods:
                db.session.add(Good(**good))
            db.session.commit()
            for store in stores:
                db.session.add(Store(**store))
            db.session.commit()
            logging.info("Data added to database successfully")


class PopulateOrders(Command):
    def run(self):
        from grocery_store import app, db
        with app.app_context():
            users = User.query.all()
            goods = Good.query.all()
            stores = Store.query.all()
            for user in users:
                number_of_orders = randint(1, 5)
                for _ in range(number_of_orders):
                    number_of_goods = randint(1, 10)
                    order = Order()
                    order_lines = [OrderLine(good=good) for good in sample(goods, number_of_goods)]
                    order.order_lines = order_lines
                    order.user = user
                    order.store = choice(stores)
                    db.session.add(order)
            db.session.commit()
