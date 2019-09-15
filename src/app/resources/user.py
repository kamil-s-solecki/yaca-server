from flask_restful import Resource
from flask import request
from app.domain.token import generate_token


class UserResource(Resource):
    def post(self):
        json = request.get_json()
        return {
            'token': generate_token(),
            'username': json['username']
        }
