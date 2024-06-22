import functools
from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
from flaskr.db import get_db

bp = Blueprint('create', __name__, url_prefix='/create')

@bp.route("/")
def create():
    return render_template("create/create.html")