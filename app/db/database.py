from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
import sys


DB_USER = os.environ['DB_USER']
DB_PASSWORD = os.environ['DB_PASSWORD']

DISPLAY_DB_LOG = False

# SQLALCHEMY_DATABASE_URL = "sqlite:///./app/db/db.sqlite3" # Local SQLite

SQLALCHEMY_DATABASE_URL = f'postgresql://{DB_USER}:{DB_PASSWORD}@localhost/ifood' # Local PostgreSQL

# SQLALCHEMY_DATABASE_URL = os.environ['DATABASE_URL'].replace("://", "ql://", 1) # Heroku

# engine = create_engine(SQLALCHEMY_DATABASE_URL, 
# 	echo=display_db_log, 
# 	connect_args={'check_same_thread': False}) # SQLite

engine = create_engine(SQLALCHEMY_DATABASE_URL,
	echo=DISPLAY_DB_LOG) # PostgreSQL

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()