from flask import Flask,Blueprint,render_template

admin_mod =Blueprint('admin',__name__,url_prefix='/admin',static_folder='static',template_folder='templates')

@admin_mod.route('/')
def admin():
    return render_template('admin/admin.html')