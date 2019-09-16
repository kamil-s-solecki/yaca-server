from flask_restful import Resource
from app.domain.token import generate_token
from app.request_data.user import UserRequestData
from app.models.user import User


class UserResource(Resource):
    def post(self):
        data = UserRequestData().parse_request()
        token = generate_token()
        user = User(None, data['username'], token)
        user.store()
        return user.json()
