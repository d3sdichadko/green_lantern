from flask import Flask, Blueprint
from flask_restful import Api, Resource, reqparse, fields, marshal_with

from module1 import module_1

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser(bundle_errors=True)
parser.add_argument('name', required=True, action='append', type=int)
parser.add_argument('number', required=True, type=int)

parser_1 = parser.copy()
parser_1.replace_argument('filter')


def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")

    return wrapper


class Cars(Resource):
    method_decorators = {"get": [my_decorator]}

    def get(self):
        args = parser_1.parse_args()
        return args

    def post(self):
        return "Hello from post"

    def put(self):
        return "Hello from put"

    def patch(self):
        return "patch"

    def delete(self, value):
        return {'task': 'Hello world'}, 201, {'Etag': 'some-opaque-string'}


api.add_resource(Cars, "/cars", "/cars/<value>")


class People:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.phones = [11, 11],
        self.address = {
            "city": "Kyiv",
            "district": "Podil"
        }


class Upper(fields.Raw):
    def format(self, value):
        return value.upper()


address_structure = {
    "city": fields.String,
    "district": fields.String
}

person_structure = {
    "name": Upper,
    "age": fields.Integer,
    "phones": fields.List(fields.String),
    "address": fields.Nested(address_structure)
}


class PeopleResource(Resource):
    @marshal_with(person_structure)
    def get(self):
        person_1 = People("Jack", 12)
        return person_1


api.add_resource(PeopleResource, "/people")

app.register_blueprint(module_1)

cars_blueprint = Blueprint("cars", __name__)
cars_blueprint_api = Api(cars_blueprint)


class Cars(Resource):
    method_decorators = {"get": [my_decorator]}

    def get(self):
        args = parser_1.parse_args()
        return args

    def post(self):
        return "Hello from post"

    def put(self):
        return "Hello from put"

    def patch(self):
        return "patch"

    def delete(self, value):
        return {'task': 'Hello world'}, 201, {'Etag': 'some-opaque-string'}


cars_blueprint_api.add_resource(Cars, "/cars", "/cars/<value>")
app.register_blueprint(cars_blueprint)

if __name__ == "__main__":
    app.run(debug=True)
