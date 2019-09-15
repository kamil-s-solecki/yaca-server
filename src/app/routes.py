from flask import Blueprint
from flask_restful import Api
from app.resources.item import ItemResource

blueprint = Blueprint('app', __name__)
api = Api(blueprint)

api.add_resource(ItemResource, '/items')
