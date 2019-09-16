from flask import Flask
from db import db
from sio import sio
from app.routes import blueprint as app_blueprint
from app import event_handlers

app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')
app.config.from_pyfile('config.py')

db.init_app(app)
sio.init_app(app)
event_handlers.register_handlers(sio)

app.register_blueprint(app_blueprint)
