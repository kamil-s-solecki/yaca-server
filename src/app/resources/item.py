from flask_restful import Resource
from app.models.item import ItemModel


class ItemResource(Resource):
    def get(self):
        items = ItemModel.query.all()
        return {'items': [i.json() for i in items]}
