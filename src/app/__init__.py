from flask import Flask
from db import db
from app.routes import blueprint as app_blueprint

app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')
app.config.from_pyfile('config.py')

db.init_app(app)

app.register_blueprint(app_blueprint)
