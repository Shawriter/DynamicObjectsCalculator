from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import create_engine



engine = create_engine('sqlite:///database.db')
db_session = scoped_session(sessionmaker(bind=engine))