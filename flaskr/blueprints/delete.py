from flask import Blueprint, render_template
from flask_login import login_required

bp = Blueprint('delete', __name__, url_prefix='/delete')

@bp.route('/')
@login_required
def delete():
    return render_template('pages/delete/delete.html')