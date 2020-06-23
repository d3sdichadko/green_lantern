from flask import request
from flask_restful import Resource, marshal

from grocery_store.models import Store
from grocery_store.db import db
from grocery_store.routes.marshal_structure import stores_structure


class Stores(Resource):
    def get(self, store_id=None):
        if store_id:
            store = Store.query.get(store_id)
            if store:
                return marshal(store, stores_structure)
            return f"No such store with id: {store_id}"
        return marshal(Store.query.all(), stores_structure)

    def post(self):
        store = Store(**request.json)
        db.session.add(store)
        db.session.commit()
        return f"Successfully added a new store {store}"

    def put(self, store_id):
        store = Store.query.get(store_id)
        store.name = request.json.get("name", store.name)
        store.city = request.json.get("city", store.city)
        store.address = request.json.get("address", store.address)
        store.manager_id = request.json.get("manager_id", store.manager_id)
        db.session.commit()
        return f"Successfully updated Store with id: {store_id}"

    def delete(self, store_id):
        store = Store.query.get(store_id)
        db.session.delete(store)
        db.session.commit()
        return f"Successfully deleted Store with id: {store_id}"
