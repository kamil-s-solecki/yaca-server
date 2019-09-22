from .self_introduction import on_self_introduction
from .messages import on_message
from flask_socketio import SocketIO


def register_handlers(sio: SocketIO):
    sio.on_event('self_introduction', on_self_introduction)
    sio.on_event('message', on_message)
