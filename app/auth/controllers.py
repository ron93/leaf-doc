from flask import Flask,Blueprint,render_template

auth_mod =Blueprint('auth',__name__,url_prefix='/auth',static_folder='static',template_folder='templates')

@auth_mod.route('/')
def auth():
    return render_template('auth/auth.html')

@auth_mod.route('/signup')
def signup():
    return render_template('auth/signup.html')