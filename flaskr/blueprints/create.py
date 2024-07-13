from flask import Blueprint, render_template
from flask_login import login_required

bp = Blueprint('create', __name__, url_prefix='/create')

@bp.route('/')
@login_required
def create():
    return render_template('pages/create/create.html')