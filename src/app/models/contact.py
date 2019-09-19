from db import db


class Contact(db.Model):
    __tablename__ = 'contacts'
    id = db.Column(db.Integer, primary_key=True)
    init_token = db.Column(db.String(80))
    token = db.Column(db.String(80))
    pin = db.Column(db.String(5))

    def __init__(self, _id, init_token):
        self.id = _id
        self.init_token = init_token
        self.pin = None
        self.token = None

    def store(self):
        db.session.add(self)
        db.session.commit()
