from flask import Blueprint
from flask_restful import Api
from app.resources.user import UserResource

blueprint = Blueprint('app', __name__)
api = Api(blueprint)

api.add_resource(UserResource, '/users', '/users/')
