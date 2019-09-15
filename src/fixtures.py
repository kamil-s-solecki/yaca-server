from app import db

items = [
]


def load_fixtures():
    for item in items:
        db.session.add(item)
    db.session.commit()
