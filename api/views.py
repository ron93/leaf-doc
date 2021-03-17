from flask import Blueprint, jsonify
from . import db

main = Blueprint('main', __name__)

@main.route('/upload', methods=['GET','POST'])
def upload():
    return "upload"

@main.route('/analyze' ,methods=['GET','POST'])
def analyze():
    return "analyze"