from flask import Blueprint, render_template
from flaskr.db import get_db

bp = Blueprint('update', __name__, url_prefix='/update')

@bp.route("/")
def update():
    return render_template("update/update.html")