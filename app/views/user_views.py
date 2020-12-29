from flask import Blueprint, render_template, flash, url_for, request
from flask_login import current_user, login_required
from werkzeug.utils import redirect

from app import db
from app.forms.user_forms import ChangePasswordForm, DeleteUserForm
from app.models.user_models import User

bp_user = Blueprint('user', __name__, url_prefix='/user')


@bp_user.route('/<username>')
def user(username):
    user = User.query.filter_by(username=current_user.username).first_or_404()
    form = DeleteUserForm()
    return render_template('user.html', user=user, form=form)


@bp_user.route('/change_password', methods=['GET', 'POST'])
@login_required
def change_password():
    # if current_user != User.get_by_username(username):

    form = ChangePasswordForm()
    if form.validate_on_submit():
        user = User.get_by_username(current_user.username)
        if user.check_password(form.old_password.data):
            user.password = form.new_password.data
            db.session.commit()
            flash(f"Password successfully changed.", 'success')
            return redirect(url_for('user.user', username=current_user.username))
        else:
            flash(f"Current password is incorrect.", 'danger')
    return render_template('change_password.html', form=form)


@bp_user.route('/delete_user/', methods=['POST'])
@login_required
def delete_user():
    form = DeleteUserForm()
    user = User.get_by_username(current_user.username)
    if form.validate_on_submit():
        if request.method == 'POST':
            db.session.delete(user)
            db.session.commit()
            flash(f'Deleted {user.username}', 'warning')
            return redirect(url_for('main.home'))
    flash('Wrong password', 'danger')
    return redirect(url_for('user.user', username=current_user.username))

