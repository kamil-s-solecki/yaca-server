from sio import sio
from app.models.user import User


@sio.on('self_introduction')
def on_self_introduction(data):
    user = User.query.filter_by(token=data['token']).first()
    if not user:
        sio.emit('incorrect_token', {'message': 'Incorrect token'})
    else:
        sio.emit('authorized', {'message': 'Great job!'})
