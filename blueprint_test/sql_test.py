# from sqlalchemy import create_engine, Column, Integer, String, Float, Date
# from sqlalchemy import Boolean
from sqlalchemy import (
	create_engine, Column, Integer, String, Float, Date, Boolean, Enum
)
from sqlalchemy.ext.declarative import declarative_base, DeclarativeMeta
from sqlalchemy.orm import sessionmaker
import enum

HOSTNAME = '127.0.0.1'
PORT     = '3306'
DATABASE = 'flask_sql'
USERNAME = 'root'
PASSWORD = 'xzx199110'

DB_URL = "mysql+pymysql://{username}:{password}@{host}:{port}/{database}".format(
	username = USERNAME,
	password = PASSWORD,
	host     = HOSTNAME,
	port     = PORT,
	database = DATABASE
)

class TypeEnum(enum.Enum):
	python = 'python'
	flask  = 'flask'
	django = 'django'

engine = create_engine(DB_URL)
session = sessionmaker(engine)()


Base: DeclarativeMeta = declarative_base(engine)
Sql_test              = declarative_base(engine)

class Self(Sql_test):
	__tablename__ = 'jian'
	
	id    = Column(Integer, primary_key = True, autoincrement = True)
	name  = Column(String(50))
	age   = Column(Integer)
	float = Column(Float)
	date  = Column(Date)
	bool  = Column(Boolean)
	enum  = Column(Enum(TypeEnum))


class Person(Base):
	__tablename__ = 'person'
	
	id   = Column(Integer, primary_key = True, autoincrement = True)
	name = Column(String(50))
	age  = Column(Integer)
	
Base.metadata.create_all()
Sql_test.metadata.create_all()
