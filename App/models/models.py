from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def init_model(app):
    db.init_app(app=app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20))
    password = db.Column(db.String(20))
