from flask import Flask
from App.views import signin
from App.models import init_model
from flask_sqlalchemy import SQLAlchemy


def creatApp():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///sqlite.db"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.register_blueprint(signin)
    init_model(app)
    return app
