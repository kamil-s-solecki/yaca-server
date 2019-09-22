from sio import sio
from app.models.contact import Contact


def on_message(data):
    token = data['contact']
    contact = Contact.query.filter_by(token=token).first()
    if contact:
        sio.send(data, room=contact.room)
    else:
        sio.emit('incorrect_contact', {'error': 'Incorrect contact token'})
