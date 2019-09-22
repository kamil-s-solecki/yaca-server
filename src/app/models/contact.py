from db import db
from app.domain.token import generate_token


class Contact(db.Model):
    __tablename__ = 'contacts'
    id = db.Column(db.Integer, primary_key=True)
    init_token = db.Column(db.String(80))
    token = db.Column(db.String(80))
    room = db.Column(db.String(80))
    pin = db.Column(db.String(5))

    initiator_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    acceptor_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    initiator = db.relationship(
        "User", foreign_keys=[initiator_id])
    acceptor = db.relationship(
        "User", foreign_keys=[acceptor_id])

    def __init__(self, _id, init_token, user):
        self.id = _id
        self.init_token = init_token
        self.pin = None
        self.token = None
        self.room = generate_token()
        self.initiator_id = user.id

    def store(self):
        db.session.add(self)
        db.session.commit()
