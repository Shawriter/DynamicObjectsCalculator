import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'testkey'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + 'dev_database.db'
    
    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'testkey'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + 'dev_database.db'
    IMAGES_DIR = os.path.join(basedir, 'app\\static\\uploads')
    

config = {
    'development': DevelopmentConfig
}
