from sio import sio
from app.models.user import User
from app.models.contact import Contact
from flask_socketio import join_room
from sqlalchemy import or_
from flask import session


def find_contacts_for(user):
    return Contact.query.filter(
        or_(Contact.initiator_id == user.id, Contact.acceptor_id == user.id)
    ).all()


def join_rooms(user):
    for contact in find_contacts_for(user):
        join_room(contact.room)


def on_self_introduction(data):
    user = User.query.filter_by(token=data['token']).first()
    if user:
        join_rooms(user)
        session['username'] = user.username
        sio.emit('authorized', {'message': 'Great job!'})
    else:
        sio.emit('incorrect_token', {'message': 'Incorrect token'})
