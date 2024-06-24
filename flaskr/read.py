from flask import Blueprint, render_template
from flaskr.db import get_db

bp = Blueprint('read', __name__, url_prefix='/read')

@bp.route("/")
def read():
    return render_template("read/read.html")