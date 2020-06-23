from flask_restful import fields

users_structure = {
    "user_id": fields.Integer,
    "name": fields.String,
    "email": fields.String,
}

goods_structure = {
    "good_id": fields.Integer,
    "name": fields.String,
    "brand": fields.String,
    "price": fields.Integer,
}
stores_structure = {
    "store_id": fields.Integer,
    "name": fields.String,
    "city": fields.String,
    "address": fields.String,
    "manager_id": fields.Integer,
}
