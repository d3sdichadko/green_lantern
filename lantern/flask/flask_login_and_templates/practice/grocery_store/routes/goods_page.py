from flask_restful import Resource, marshal
from flask import Blueprint


from grocery_store.models import Good
from grocery_store.routes.marshal_structure import goods_structure


goods_page = Blueprint('goods_page', __name__)


class Goods(Resource):
    def get(self, good_id=None):
        if good_id:
            good = Good.query.get(good_id)
            if good:
                return marshal(good, goods_structure)
            return f"No such good with id: {good_id}"
        return marshal(Good.query.all(), goods_structure)
