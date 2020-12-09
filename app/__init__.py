import os

from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


basedir = os.path.abspath(os.path.dirname(__file__))
db = SQLAlchemy()
login_manager = LoginManager()


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(basedir, '../app.db')}"
    app.config['SECRET_KEY'] = "b'\xed\x0e\xb9\x15`/2=\xbe\x18\r\x83e\xb1\xde\x9d'"

    from app.views.main_views import bp_main
    from app.views.auth_views import bp_auth

    app.register_blueprint(bp_main)
    app.register_blueprint(bp_auth)

    login_manager.session_protection = "strong"
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    db.init_app(app)

    Migrate(app, db)

    return app
