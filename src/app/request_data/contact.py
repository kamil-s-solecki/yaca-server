from app.request_data.validators import (
    valid_user_token, valid_contact_init_token, valid_contact_pin)
from app.request_data.request_data import RequestData


class ContactTokenRequestData(RequestData):
    def add_fields(self):
        self.add_field('User-Token', location='headers',
                       validators=[valid_user_token()])


class GetContactPinRequestData(RequestData):
    def add_fields(self):
        self.add_field('contact_init_token', location='args',
                       validators=[valid_contact_init_token()])
        self.add_field('User-Token', location='headers',
                       validators=[valid_user_token()])


class PostContactPinRequestData(RequestData):
    def add_fields(self):
        self.add_field('pin',
                       validators=[valid_contact_pin()])
