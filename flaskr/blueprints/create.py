from flask import Blueprint, render_template

bp = Blueprint('create', __name__, url_prefix='/create')

@bp.route("/")
def create():
    return render_template("pages/create/create.html")