from flask_bootstrap import Bootstrap5
from flask import Flask, render_template

app = Flask(__name__)
bootstrap = Bootstrap5(app)

@app.route("/")
def hello_world():
    return render_template("landing.html", name="sarah")

@app.route("/create")
def create():
    return render_template("create.html")

@app.route("/update")
def update():
    return "<p>aktualisieren</p>"

@app.route("/markdone")
def markdone():
    return "<p>als abgeschlossen markieren</p>"

@app.route("/delete")
def delete():
    return "<p>delete</p>"

@app.route("/search")
def search():
    return "<p>suche</p>"
