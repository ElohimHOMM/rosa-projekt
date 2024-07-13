from flask import Blueprint, render_template
from flask_login import login_required

bp = Blueprint('update', __name__, url_prefix='/update')

@bp.route('/')
@login_required
def update():
    return render_template('pages/update/update.html')