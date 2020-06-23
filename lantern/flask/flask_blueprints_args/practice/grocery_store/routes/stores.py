import inject
from flask import Blueprint, request, jsonify

stores_bl = Blueprint("stores", __name__)


@stores_bl.route('/store', methods=['POST'])
def create_store():
    db = inject.instance('DB')
    store_id = db.stores.add(request.json)
    return jsonify({'store_id': store_id}), 201


@stores_bl.route('/store/<int:store_id>')
def get_store(store_id):
    db = inject.instance('DB')
    store = db.stores.get_store_by_id(store_id)
    return jsonify(store)


@stores_bl.route('/store/<int:store_id>', methods=['PUT'])
def update_store(store_id):
    db = inject.instance('DB')
    db.stores.update_store_by_id(store_id, request.json)
    return jsonify({'status': 'success'})
