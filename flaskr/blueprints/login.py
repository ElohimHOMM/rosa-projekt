from flask import Blueprint, render_template, request, redirect, url_for
from flaskr.db.db import get_db

bp = Blueprint('login', __name__, url_prefix='/login')

@bp.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('index'))
    return render_template('pages/login/login.html', error=error)