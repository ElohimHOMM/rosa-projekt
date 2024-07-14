from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import login_required
from flaskr.models import Aufgabe
from flaskr import db
from datetime import datetime
from sqlalchemy.exc import SQLAlchemyError

bp = Blueprint('create', __name__, url_prefix='/aufgabenplaner/create')

@bp.route('/')
@login_required
def create():
    return render_template('pages/aufgabenplaner/create/create.html')

@bp.route('/', methods=['POST'])
@login_required
def create_post():
    form = request.form
    titel = form.get('titel')
    beginndatum = parse_to_datetime(form.get('beginndatum'))
    enddatum = parse_to_datetime(form.get('enddatum'))
    prioritaet = form.get('prioritaet')

    aufgabe = Aufgabe.query.filter_by(titel=titel).first()

    if aufgabe:
        flash('Eine Aufgabe mit diesem Titel existiert bereits.')
        return redirect(url_for('create.create'))
    
    try:
        aufgabe = Aufgabe(titel=titel, beginndatum=beginndatum, enddatum=enddatum, prioritaet=prioritaet)
        db.session.add(aufgabe)
        db.session.commit()
    except SQLAlchemyError as e:
        flash('Etwas ist schief gelaufen beim Speichern der Aufgabe.\n{e}')
        return redirect(url_for('create.create'))

    flash(f"Aufgabe mit der ID {aufgabe.id} wurde erfolgreich angelegt.")
    return redirect(url_for('create.create'))

def parse_to_datetime(input: str):
    input = input.split('-')
    year = int(input[0])
    month = int(input[1])
    day = int(input[2])
    return datetime(year=year, month=month, day=day)