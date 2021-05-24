<<<<<<< HEAD
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()
UPLOAD_FOLDER = 'uploads'  

def create_app():
    app = Flask(__name__)

#    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://ron:qwerty@localhost:5432/reddits"
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

    db.init_app(app)
    from .views import main
    app.register_blueprint(main)
    return app
  