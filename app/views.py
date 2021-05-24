from flask import render_template, flash, redirect, url_for, request, g, \
    jsonify, current_app,Blueprint
from . import db
import os
from flask import Flask, request, redirect, url_for, send_from_directory, render_template
from keras.preprocessing.image import ImageDataGenerator, load_img, img_to_array
from keras.models import Sequential, load_model
from werkzeug.utils import secure_filename
import numpy as np
import pickle
import app

classes = ['Apple___Apple_scab','Apple___Black_rot','Apple___Cedar_apple_rust','Apple___healthy','Blueberry___healthy','Cherry_(including_sour)___Powdery_mildew','Cherry_(including_sour)___healthy','Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot','Corn_(maize)___Common_rust_','Corn_(maize)___Northern_Leaf_Blight','Corn_(maize)___healthy','Grape___Black_rot','Grape___Esca_(Black_Measles)','Grape___Leaf_blight_(Isariopsis_Leaf_Spot)','Grape___healthy','Orange___Haunglongbing_(Citrus_greening)','Peach___Bacterial_spot','Peach___healthy','Pepper,_bell___Bacterial_spot','Pepper,_bell___healthy','Potato___Early_blight','Potato___Late_blight','Potato___healthy','Raspberry___healthy','Soybean___healthy','Squash___Powdery_mildew','Strawberry___Leaf_scorch','Strawberry___healthy','Tomato___Bacterial_spot','Tomato___Early_blight','Tomato___Late_blight','Tomato___Leaf_Mold','Tomato___Septoria_leaf_spot','Tomato___Spider_mites Two-spotted_spider_mite','Tomato___Target_Spot','Tomato___Tomato_Yellow_Leaf_Curl_Virus','Tomato___Tomato_mosaic_virus','Tomato___healthy','background']

main = Blueprint('main', __name__)


ALLOWED_EXTENSIONS = set(['jpg', 'jpeg', 'png'])
IMAGE_SIZE = (224, 224)

with open('ml_models/model.pkl', 'rb') as file:
    pickle.load(file)
file.close()

# allowed pic extensions
def allowed_file(filename):
    return '-' in filename and filename.split('.',1)[1] in ALLOWED_EXTENSIONS



@main.route('/', methods=['GET','POST'])
def home():
    return render_template('home.html')

@main.route('/upload', methods=['GET','POST'])
def upload():
  
    return "upload"

@main.route('/analyze' ,methods=['GET','POST'])
def analyze():
    return "analyze"