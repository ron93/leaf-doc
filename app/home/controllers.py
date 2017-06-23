from flask import Blueprint,render_template,abort 
from jinja2 import TemplateNotFound


home_mod = Blueprint('home', __name__, url_prefix='/home', static_folder='static', template_folder='templates')


@home_mod.route('/')
def home():
    # with home_mod.open_resource('static/home/css/home.css') as f:
        # code = f.read()
    return render_template('home/home.html')
   
