from flask import Blueprint
from flask_restful import Api

from grocery_store.routes.users import Users
from grocery_store.routes.goods import Goods
from grocery_store.routes.stores import Stores

users = Blueprint("users", __name__)
goods = Blueprint("goods", __name__)
stores = Blueprint("stores", __name__)
api_users = Api(users)
api_goods = Api(goods)
api_stores = Api(stores)

api_users.add_resource(Users, "/users", "/users/<user_id>")
api_goods.add_resource(Goods, "/goods", "/goods/<good_id>")
api_stores.add_resource(Stores, "/stores", "/stores/<store_id>")
