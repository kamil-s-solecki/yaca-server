import socketio


class Socket():
    def __init__(self):
        self.is_connected = False
        self.sio = socketio.Client()

    def on(self, event, handler):
        self.sio.on(event, handler)

    def on_connect(self, handler):
        self.on('connect', handler)

    def introduce_yourself(self, token):
        self.sio.emit('self_introduction', {'token': token})

    def connect(self):
        self.is_connected = True
        self.sio.connect('http://localhost:5000/')
        while self.is_connected:
            pass

    def disconnect(self):
        self.is_connected = False
        self.sio.disconnect()

