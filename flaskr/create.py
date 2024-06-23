from flask import Blueprint, render_template
from flaskr.db import get_db

bp = Blueprint('create', __name__, url_prefix='/create')

@bp.route("/")
def create():
    return render_template("create/create.html")