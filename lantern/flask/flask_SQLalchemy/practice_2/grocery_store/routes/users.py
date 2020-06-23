from flask import request
from flask_restful import Resource, marshal

from grocery_store.models import User
from grocery_store.db import db
from grocery_store.routes.marshal_structure import users_structure


class Users(Resource):
    def get(self, user_id=None):
        if user_id:
            user = User.query.get(user_id)
            if user:
                return marshal(user, users_structure)
            return f"No such user with id: {user_id}"
        return marshal(User.query.all(), users_structure)

    def post(self):
        user = User(**request.json)
        db.session.add(user)
        db.session.commit()
        return f"Successfully added a new user {user}"

    def put(self, user_id):
        user = User.query.get(user_id)
        user.name = request.json.get("name", user.name)
        user.email = request.json.get("email", user.email)
        user.password = request.json.get("password", user.password)
        db.session.commit()
        return f"Successfully updated User with id: {user_id}"

    def delete(self, user_id):
        user = User.query.get(user_id)
        db.session.delete(user)
        db.session.commit()
        return f"Successfully deleted User with id: {user_id}"
