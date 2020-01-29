from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class User(Base):
	__tablename__ = 'user'
	id = Column(Integer, primary_key=True)
	name = Column(String)
	Email= Column(String)
	Password= Column(Integer)


class Movie(Base):
	__tablename__ = 'movies'
	id = Column(Integer, primary_key=True)
	name = Column(String)
	Genre = Column(String)
	release_date= Column(Integer)
	img_link=Column(String)
	

