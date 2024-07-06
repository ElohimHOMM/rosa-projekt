from flask import Blueprint, render_template

bp = Blueprint('markdone', __name__, url_prefix='/markdone')

@bp.route("/")
def markdone():
    return render_template("pages/markdone/markdone.html")