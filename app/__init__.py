import os

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))
db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(basedir, '../chat.db')}"
    app.config['SECRET_KEY'] = "b'\xed\x0e\xb9\x15`/2=\xbe\x18\r\x83e\xb1\xde\x9d'"

    from app.views import bp_main

    app.register_blueprint(bp_main)

    db.init_app(app)

    Migrate(app, db)

    return app
