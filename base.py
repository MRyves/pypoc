# coding=utf-8

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine(
    'mysql+mysqlconnector://admin:admin@localhost:3306/test')
Session = sessionmaker(bind=engine)

Base = declarative_base()
