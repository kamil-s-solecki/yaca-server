from app.models.user import User
from app.models.contact import Contact


def max_length(n):
    def max_length_validator(value):
        if value and len(value) > n:
            return "This value must have {} characters or less".format(n)
        return None

    return max_length_validator


def not_blank():
    def not_blank_validator(value):
        if not value or value.isspace():
            return "This value cannot be blank"
        return None

    return not_blank_validator


def valid_user_token():
    def valid_user_token_validator(value):
        user = User.query.filter_by(token=value).first()
        if not user:
            return "Incorrect token"
        return None

    return valid_user_token_validator


def valid_contact_init_token():
    def valid_contact_init_token_validator(value):
        contact = Contact.query.filter_by(init_token=value).first()
        if not contact:
            return "No contact exists for given contact token"
        return None

    return valid_contact_init_token_validator


def valid_contact_pin():
    def valid_contact_init_token_validator(value):
        contact = Contact.query.filter_by(pin=value).first()
        if not contact:
            return "No contact exists for given pin"
        return None

    return valid_contact_init_token_validator
