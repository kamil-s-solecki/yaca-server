from flask_restful import Resource
from app.request_data.contact import (
    ContactTokenRequestData, GetContactPinRequestData,
    PostContactPinRequestData)
from app.domain.token import generate_token, generate_pin
from app.models.contact import Contact
from app.models.user import User


class ContactTokenResource(Resource):
    def get(self):
        data = ContactTokenRequestData().parse_request()
        user = User.query.filter_by(token=data['user_token']).first()
        contact = Contact(None, generate_token(), user)
        contact.store()
        return {"contact_init_token": contact.init_token}


class ContactPinResource(Resource):
    def get(self):
        data = GetContactPinRequestData().parse_request()
        user = User.query.filter_by(token=data['user_token']).first()
        contact = Contact.query.filter_by(
            init_token=data["contact_init_token"]).first()
        contact.acceptor_id = user.id
        contact.pin = generate_pin()
        contact.token = generate_token()
        contact.store()
        return {"pin": contact.pin, "contact_token": contact.token}

    def post(self):
        data = PostContactPinRequestData().parse_request()
        contact = Contact.query.filter_by(pin=data["pin"]).first()
        return {"contact_token": contact.token}
