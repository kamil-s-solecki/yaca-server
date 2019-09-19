from flask import Blueprint
from flask_restful import Api
from app.resources.user import UserResource
from app.resources.contact import ContactTokenResource, ContactPinResource

blueprint = Blueprint('app', __name__)
api = Api(blueprint)

api.add_resource(UserResource, '/users', '/users/')
api.add_resource(ContactTokenResource, '/contacts/tokens/init',
                 '/contacts/tokens/init/')
api.add_resource(ContactPinResource, '/contacts/pins',
                 '/contacts/pins/')
