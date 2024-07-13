from flask import Blueprint, render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from ..models import User
from flask_login import login_user, login_required, logout_user
from .. import db

bp = Blueprint('auth', __name__,)

@bp.route('/login')
def login():
    return render_template('pages/auth/login.html')

@bp.route('/login', methods=['POST'])
def login_post():
    username = request.form.get('username')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = User.query.filter_by(username=username).first()

    if not user or not check_password_hash(user.password, password):
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.login'))

    login_user(user, remember=remember)
    return redirect(url_for('main.index'))

@bp.route('/register')
def register():
    return render_template('pages/auth/register.html')

@bp.route('/register', methods=['POST'])
def register_post():
    form = request.form
    # get relevant information from register page
    username = form.get('username')
    password = form.get('password')

    # Check db if username is already registered
    user = User.query.filter_by(username = username).first()

    if user: # This check returns None (or Falsey) if user is not present
        flash('Username already exists')
        return redirect(url_for('auth.register'))
    
    # If user was not present we continue here and create one in the DB. Password is hashed
    user = User(username=username, password=generate_password_hash(password))
    db.session.add(user)
    db.session.commit()

    flash(f'User {username} has been registered successfully.')
    return redirect(url_for('auth.login'))

@bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))