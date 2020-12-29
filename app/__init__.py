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
    from app.views.user_views import bp_user
    from app.views.article_views import bp_article
    from app.views.admin_views import bp_admin

    app.register_blueprint(bp_main)
    app.register_blueprint(bp_auth)
    app.register_blueprint(bp_user)
    app.register_blueprint(bp_article)
    app.register_blueprint(bp_admin)

    login_manager.session_protection = "strong"
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    db.init_app(app)

    Migrate(app, db)

    return app
