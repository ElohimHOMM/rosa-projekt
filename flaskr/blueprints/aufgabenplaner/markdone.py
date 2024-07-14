from flask import Blueprint, render_template
from flask_login import login_required

bp = Blueprint('markdone', __name__, url_prefix='/aufgabenplaner/markdone')

@bp.route('/')
@login_required
def markdone():
    return render_template('pages/aufgabenplaner/markdone/markdone.html')