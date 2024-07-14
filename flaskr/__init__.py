import os
from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_login import LoginManager
import logging
import logging.config
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from werkzeug.security import generate_password_hash

class Base(DeclarativeBase):
  pass

login_manager = LoginManager()
# Instantiate app with config values
app = Flask(__name__, instance_relative_config=True)
app.config.from_mapping(
    SECRET_KEY = 'dev',
    DATABASE = os.path.join(app.instance_path, 'flaskr.sqlite'),
    TEMPLATES_AUTO_RELOAD = True,
    SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite'
)
db = SQLAlchemy(app, model_class=Base)
# define helper objects: login_manager, bootstrap (for templates), logger and db
login_manager.init_app(app)
login_manager.login_view = 'auth.login'

bootstrap = Bootstrap5(app)
logger = logging.getLogger(__name__)
# Import and create Database
from .models import User
with app.app_context():
    db.create_all()
    # Either do this on first run or just create it via the register page
    # db.session.add(User(username='admin', password=generate_password_hash('admin')))
    # db.session.commit()

# define login_manager user_loader method to correctly save user in session
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Actual Controlling goes here

### Register Blueprints (these are essentially the outsourced routes)
from .blueprints import auth, main
app.register_blueprint(auth.bp)
app.register_blueprint(main.bp)
from .blueprints.aufgabenplaner import create, delete, markdone, read, update
app.register_blueprint(create.bp)
app.register_blueprint(update.bp)
app.register_blueprint(markdone.bp)
app.register_blueprint(delete.bp)
app.register_blueprint(read.bp)