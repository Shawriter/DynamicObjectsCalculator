from flask import Flask
from flask_bootstrap import Bootstrap
#from flask_fontawesome import FontAwesome
#from flask_mail import Mail
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_cors import CORS
from flask_wtf.csrf import CSRFProtect
from config import config
import logging
import os
import sys
from sqlalchemy.pool import QueuePool
#from .dbase import conn


login_manager = LoginManager()
login_manager.login_view = 'auth.login'
db = SQLAlchemy()

bootstrap = Bootstrap()
#fa = FontAwesome()

#SECRET_KEY = os.environ.get('SECRET_KEY') or ''
csrf = CSRFProtect()
moment = Moment()


def create_app(config_name):
    app = Flask(__name__)
    
    CORS(app,supports_credentials=True,expose_headers=["Content-Type","X-CSRFToken"])
    app.config.from_object(config[config_name])
    
    config[config_name].init_app(app)
    print(config[config_name].SQLALCHEMY_DATABASE_URI, config[config_name].IMAGES_DIR)
    bootstrap.init_app(app)
    #fa.init_app(app)
    
    moment.init_app(app)
    db.init_app(app)
    print()
    #login_manager.init_app(app)
    
    csrf.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .users import users as users_blueprint
    app.register_blueprint(users_blueprint)

    from .dbase import dbase as dbase_blueprint
    app.register_blueprint(dbase_blueprint)

    return app