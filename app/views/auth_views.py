from flask import Blueprint, render_template, flash, request, url_for
from flask_login import login_user, logout_user
from werkzeug.utils import redirect

from app import db
from app.forms.user_forms import LoginForm, SignUpForm
from app.models.user_models import User

bp_auth = Blueprint('auth', __name__, url_prefix='/auth')


@bp_auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.get_by_username(form.username.data)
        if user is None or not user.check_password(form.password.data):
            flash("Invalid username or password", 'danger')
            return redirect(url_for("auth.login"))

        login_user(user, remember=form.remember_me.data)
        flash(f'You are logged in!', 'success')
        return redirect(request.args.get('next') or url_for('main.home'))

    return render_template('login.html', form=form)


@bp_auth.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data, password=form.password.data)

        db.session.add(user)
        db.session.commit()

        flash(f'Hello {user.username}! Please login', 'info')
        return redirect(url_for('auth.login'))
    return render_template('signup.html', form=form)


@bp_auth.route('/logout')
def logout():
    logout_user()
    flash(f'Logged out!', 'warning')
    return redirect(url_for('main.home'))
