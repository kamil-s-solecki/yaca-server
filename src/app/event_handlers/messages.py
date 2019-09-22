from sio import sio
from app.models.contact import Contact
from flask import session


def on_message(data):
    token = data['contact']
    contact = Contact.query.filter_by(token=token).first()

    message = {
        'contact': data['contact'],
        'message': data['message'],
        'username': session.get('username'),
    }
    if contact:
        sio.send(message, room=contact.room)
    else:
        sio.emit('incorrect_contact', {'error': 'Incorrect contact token'})
