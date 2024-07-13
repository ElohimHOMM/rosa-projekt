from . import db
from sqlalchemy.orm import Mapped, mapped_column
from flask_login import UserMixin

class User(UserMixin, db.Model):
    # primary key is required by SQLAlchemy, this is the key by which flask_login will recognize the user
    id: Mapped[int] = mapped_column(db.Integer, primary_key=True, nullable=False)
    username: Mapped[str]  = mapped_column(db.String(100), unique=True, nullable=False)
    password: Mapped[str]  = mapped_column(db.String(100), nullable=False)