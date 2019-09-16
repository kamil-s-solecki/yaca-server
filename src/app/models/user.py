from db import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    token = db.Column(db.String(80))

    def __init__(self, _id, username, token):
        self.id = _id
        self.username = username
        self.token = token

    def json(self):
        return {'username': self.username, 'token': self.token}

    def store(self):
        db.session.add(self)
        db.session.commit()
