from app.models.item import ItemModel
from app import db

items = [
    ItemModel(None, 'something'),
    ItemModel(None, 'something else'),
]


def load_fixtures():
    for item in items:
        db.session.add(item)
    db.session.commit()
