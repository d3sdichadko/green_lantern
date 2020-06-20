import datetime
from flask_login import UserMixin

from sqlalchemy import DateTime

from grocery_store.database import db


class User(db.Model, UserMixin):
    __tablename__ = "users"

    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    email = db.Column(db.String(), nullable=False)
    password = db.Column(db.String(), nullable=False)

    orders = db.relationship('Order', backref='user')
    manage_stores = db.relationship('Store', backref='user')

    def __repr__(self):
        return f"<id: {self.user_id}, name: {self.name}, email: {self.email}>"

    def get_id(self):
        return self.user_id


class Good(db.Model):
    __tablename__ = "goods"

    good_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    brand = db.Column(db.String(), nullable=False)
    price = db.Column(db.Integer, nullable=False)


class Store(db.Model):
    __tablename__ = "stores"

    store_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    city = db.Column(db.String(), nullable=False)
    address = db.Column(db.String(), nullable=False)
    manager_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable=False)

    orders = db.relationship('Order', backref='store')


class Order(db.Model):
    __tablename__ = "orders"

    order_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable=False)
    created_time = db.Column(DateTime, default=datetime.datetime.utcnow)
    store_id = db.Column(db.Integer, db.ForeignKey("stores.store_id"), nullable=False)

    order_lines = db.relationship('OrderLine', backref='order')


class OrderLine(db.Model):
    __tablename__ = "order_lines"

    order_line_id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey("orders.order_id"), nullable=False)
    good_id = db.Column(db.Integer, db.ForeignKey("goods.good_id"), nullable=False)

    good = db.relationship('Good')
