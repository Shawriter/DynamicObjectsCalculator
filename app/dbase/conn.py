from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import create_engine
from . import dbase



def setup_session():
    engine = create_engine('sqlite:///database.db')
    db_session = scoped_session(sessionmaker(bind=engine))




def shutdown_session(exception=None):
    #db_session.remove()
    pass