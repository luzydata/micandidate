import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

################################################################################
# APP INITIALIZATION ###########################################################
################################################################################
app = Flask(__name__)

##############################
###### CONFIG ################
##############################
# TODO: set your environment variables at the command line TO deploy.
app.config['SECRET_KEY'] = 'mysecret'


################################################################################
# DB SETUP #####################################################################
################################################################################
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
##############################
# DB INITIALIZATION ##########
##############################
db = SQLAlchemy(app)
Migrate(app,db)

################################################################################
# LOGIN MANAGER CONFIG #########################################################
################################################################################
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'users.login'
# TODO: create html template


################################################################################
# BLUEPRINTS REGISTRY & CONFIG #################################################
################################################################################
from mi_candidate.core.views import core
from mi_candidate.users.views import users
from mi_candidate.error_pages.handlers import error_pages

app.register_blueprint(core)
app.register_blueprint(users)
app.register_blueprint(error_pages)
