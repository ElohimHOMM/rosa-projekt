from flask import Blueprint, render_template

bp = Blueprint('delete', __name__, url_prefix='/delete')

@bp.route("/")
def delete():
    return render_template("pages/delete/delete.html")