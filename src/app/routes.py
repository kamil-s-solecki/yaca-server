from flask import Blueprint
from flask_restful import Api

blueprint = Blueprint('app', __name__)
api = Api(blueprint)
