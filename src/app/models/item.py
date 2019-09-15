from db import db


class ItemModel(db.Model):
    __tablename__ = 'items'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

    def __init__(self, _id, name):
        self.id = _id
        self.name = name

    def json(self):
        return {'id': self.id, 'name': self.name}
