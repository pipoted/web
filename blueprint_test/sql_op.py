from sqlalchemy import (
	create_engine, Column, Integer, Enum,
	String, Date
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import enum
from datetime import date


HOSTNAME = '127.0.0.1'
PORT     = '3306'
DATABASE = 'flask_sql'
USERNAME = 'root'
PASSWORD = 'xzx199110'

DB_URL = "mysql+pymysql://{username}:{password}@{host}:{port}/{database}".format(
	username = USERNAME,
	password = PASSWORD,
	host     =  HOSTNAME,
	port     =  PORT,
	database =  DATABASE
)

engier = create_engine(DB_URL)
session = sessionmaker(engier)()

Base = declarative_base(engier)

class Type_Enum(enum.Enum):
	python = 'python'
	flask  = 'flask'
	django = 'django'

class My_Flask(Base):
	__tablename__ = 'myflask'
	
	id = Column(Integer, primary_key=True, autoincrement=True)
	name = Column(String(50))
	class_name = Column(Enum(Type_Enum))
	create_time = Column(Date)

test = My_Flask(create_time=date(year=2018,month=2,day=12))
Base.metadata.create_all()
session.add(My_Flask)
session.commit()
