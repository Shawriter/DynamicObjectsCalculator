from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import create_engine
#from db import User
from sqlalchemy.ext.declarative import declarative_base
import os



def shutdown_session(exception=None):
    #session.remove()
    pass