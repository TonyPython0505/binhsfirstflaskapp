from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

app = Flask(__name__)

login = LoginManager(app)
login.login_view = 'login'

db = SQLAlchemy()
DB_NAME = "my_database.db"

def create_app():
    app.config['SECRET_KEY'] = 'PercyJackson090'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    create_database(app)

    login.init_app(app)

    import routes, models

    return app

def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)