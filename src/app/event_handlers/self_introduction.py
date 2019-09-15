from sio import sio


@sio.on('self_introduction')
def on_self_introduction(data):
    sio.emit('incorrect_token', {'message': 'Incorrect token'})
