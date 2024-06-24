from flask import Blueprint, render_template
from flaskr.db import get_db

bp = Blueprint('delete', __name__, url_prefix='/delete')

@bp.route("/")
def delete():
    return render_template("delete/delete.html")