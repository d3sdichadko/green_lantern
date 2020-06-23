import inject
from flask import Blueprint, request, jsonify

goods_bl = Blueprint("goods", __name__)


@goods_bl.route('/goods', methods=['POST'])
def create_goods():
    db = inject.instance('DB')
    number_of_created_goods = db.goods.add_many(request.json)
    return jsonify({'number of items created': number_of_created_goods}), 201


@goods_bl.route('/goods')
def get_goods():
    db = inject.instance('DB')
    return jsonify(db.goods.get_all())
