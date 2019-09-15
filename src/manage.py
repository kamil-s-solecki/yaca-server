from flask_script import Manager

from app import app
from sio import sio
import fixtures

manager = Manager(app)


@manager.command
def start():
    sio.run(app, host='0.0.0.0')


@manager.command
def create_tables():
    from app import db
    with app.app_context():
        db.create_all()
        db.session.commit()


@manager.command
def drop_tables():
    from app import db
    with app.app_context():
        db.drop_all()
        db.session.commit()


@manager.command
def load_fixtures():
    with app.app_context():
        fixtures.load_fixtures()


@manager.command
def recreate_db():
    drop_tables()
    create_tables()
    load_fixtures()


if __name__ == "__main__":
    manager.run()
