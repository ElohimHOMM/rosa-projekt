from flask import Blueprint, render_template

bp = Blueprint('update', __name__, url_prefix='/update')

@bp.route("/")
def update():
    return render_template("pages/update/update.html")