from flask import Flask, jsonify, request

import inject


class NoSuchUserError(Exception):
    def __init__(self, user_id):
        self.message = f"No such user_id {user_id}"


class NoSuchGoodError(Exception):
    def __init__(self, good_id):
        self.message = f"No such good_id {good_id}"


class NoSuchStoreError(Exception):
    def __init__(self, store_id):
        self.message = f"No such store_id {store_id}"


app = Flask(__name__)


@app.errorhandler(NoSuchUserError)
def my_error_handler(e):
    return jsonify({'error': e.message}), 404


@app.errorhandler(NoSuchGoodError)
def my_error_handler(e):
    return jsonify({'error': e.message}), 404


@app.errorhandler(NoSuchStoreError)
def my_error_handler(e):
    return jsonify({'error': e.message}), 404


@app.route('/users', methods=['POST'])  # POST /users
def create_user():
    # __import__("pdb").set_trace()
    db = inject.instance('DB')
    user_id = db.users.add(request.json)
    return jsonify({'user_id': user_id}), 201


@app.route('/users/<int:user_id>')  # GET /users/id
def get_user(user_id):
    db = inject.instance('DB')
    user = db.users.get_user_by_id(user_id)
    return jsonify(user), 200


@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    db = inject.instance('DB')
    db.users.update_user_by_id(user_id, request.json)
    return jsonify({'status': 'success'})


# Goods
@app.route('/goods', methods=['POST'])  # POST /goods
def create_goods():
    db = inject.instance('DB')
    good_id = db.goods.add(request.json)
    return jsonify({'good_id': good_id})


@app.route('/goods/<int:good_id>')  # GET /goods
def get_good(good_id):
    # __import__("pdb").set_trace()
    db = inject.instance('DB')
    good = db.goods.get_good_by_id(good_id)
    return jsonify(good), 200


@app.route('/goods/<int:good_id>', methods=['PUT'])  # PUT /goods/id
def update_good(good_id):
    db = inject.instance('DB')
    db.goods.update_good_by_id(good_id, request.json)
    return jsonify({'successfully_updated': good_id})


# Stores
@app.route('/store', methods=['POST'])  # POST /stores
def create_stores():
    db = inject.instance('DB')
    store_id = db.store.add(request.json)
    return jsonify({'store_id': store_id})


@app.route('/store/<int:store_id>')  # GET /goods
def get_store(store_id):
    # __import__("pdb").set_trace()
    db = inject.instance('DB')
    store = db.store.get_store_by_id(store_id)
    return jsonify(store), 200


@app.route('/store/<int:store_id>', methods=['PUT'])  # PUT /store/id
def update_store(store_id):
    db = inject.instance('DB')
    db.store.update_store_by_id(store_id, request.json)
    return jsonify({'successfully_updated': store_id})
