import os
from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from . import db, create, update

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY = 'dev',
        DATABASE = os.path.join(app.instance_path, 'flaskr.sqlite'),
        TEMPLATES_AUTO_RELOAD = True
    )
    bootstrap = Bootstrap5(app)

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    ### Register Paths (these will be outsourced later)
    @app.route("/")
    def hello_world():
        return render_template("landing.html")

    @app.route("/markdone")
    def markdone():
        return "<p>als abgeschlossen markieren</p>"

    @app.route("/delete")
    def delete():
        return "<p>delete</p>"

    @app.route("/search")
    def search():
        return "<p>suche</p>"

    ### Register Blueprints (these are essentially the outsourced routes)
    app.register_blueprint(create.bp)
    app.register_blueprint(update.bp)

    ### initialize db
    db.init_app(app)

    return app