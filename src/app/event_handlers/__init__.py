from .self_introduction import on_self_introduction
from flask_socketio import SocketIO


def register_handlers(sio: SocketIO):
    sio.on_event('self_introduction', on_self_introduction)
