from flask_restful import Resource
from app.domain.token import generate_token
from app.request_data.user import UserRequestData


class UserResource(Resource):
    def post(self):
        data = UserRequestData().parse_request()
        return {
            'token': generate_token(),
            'username': data['username']
        }
