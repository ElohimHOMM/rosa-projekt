from flask import Blueprint, render_template

bp = Blueprint('read', __name__, url_prefix='/read')

@bp.route("/")
def read():
    return render_template("pages/read/read.html")