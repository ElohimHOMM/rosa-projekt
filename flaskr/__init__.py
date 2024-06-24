import os
from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from . import db, create, read, update, markdone, delete

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

    ### Register Blueprints (these are essentially the outsourced routes)
    app.register_blueprint(create.bp)
    app.register_blueprint(update.bp)
    app.register_blueprint(markdone.bp)
    app.register_blueprint(delete.bp)
    app.register_blueprint(read.bp)

    ### initialize db
    db.init_app(app)

    return app