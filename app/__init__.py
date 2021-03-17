import os
from flask import Flask, request, redirect, url_for, send_from_directory, render_template
from keras.preprocessing.image import ImageDataGenerator, load_img, img_to_array
from keras.models import Sequential, load_model
from werkzeug.utils import secure_filename
import numpy as np

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

#    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://ron:qwerty@localhost:5432/reddits"

    db.init_app(app)
    from .views import main
    app.register_blueprint(main)
    return app
    