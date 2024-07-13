from flask import Blueprint, render_template
from flask_login import login_required, current_user

bp = Blueprint('main', __name__)

@bp.route('/')
@login_required
def index():
    return render_template('pages/index.html')

@bp.route('/profile')
@login_required
def profile():
    return render_template('pages/profile/profile.html', user=current_user)