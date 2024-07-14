from flask import Blueprint, render_template
from flask_login import login_required

bp = Blueprint('read', __name__, url_prefix='/aufgabenplaner/read')

@bp.route('/')
@login_required
def read():
    return render_template('pages/aufgabenplaner/read/read.html')