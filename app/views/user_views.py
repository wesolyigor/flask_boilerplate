from flask import Blueprint, render_template
from flask_login import current_user

from app.models.user_models import User

bp_user = Blueprint('user', __name__, url_prefix='/user')


@bp_user.route('/<username>')
def user(username):
    user = User.query.filter_by(username=current_user.username).first_or_404()
    return render_template('user.html', user=user)
