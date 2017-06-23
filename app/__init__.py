from flask import Flask, render_template,app
import config 

import admin,home,auth

from app.home.controllers import home_mod
from app.admin.controllers import admin_mod
from app.auth.controllers import auth_mod

app = Flask(__name__)
# configurations
app.config.from_object('config.DevelopmentConfig')





# register blueprints

# home page blueprint
app.register_blueprint(home.controllers.home_mod)

# admin blueprint
app.register_blueprint(admin.controllers.admin_mod)

#auth blueprint
app.register_blueprint(auth.controllers.auth_mod)

