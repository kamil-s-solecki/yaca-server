import socketio


class Socket():
    def __init__(self):
        self.is_connected = False
        self.sio = socketio.Client()

    def on(self, event, handler):
        self.sio.on(event, handler)

    def on_connect(self, handler):
        self.on('connect', handler)

    def on_incorrect_contact(self, handler):
        self.on('incorrect_contact', handler)

    def on_authorized(self, handler):
        self.on('authorized', handler)

    def on_message(self, handler):
        self.on('message', handler)

    def introduce_yourself(self, token):
        self.sio.emit('self_introduction', {'token': token})

    def connect(self, block=True):
        self.is_connected = True
        self.sio.connect('http://localhost:5000/')
        while self.is_connected and block:
            pass

    def disconnect(self):
        self.is_connected = False
        self.sio.disconnect()
