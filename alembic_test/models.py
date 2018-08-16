from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base


DB_USERNAME = 'root'
DB_PASSWORD = 'xzx199110'
DB_HOST = '127.0.0.1'
DB_PORT = 3306
DB_NAME = 'flask_sql'

DB_URI = 'mysql+pymysql://%s:%s@%s:%s/%s' % (
	DB_USERNAME, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME
)

engier = create_engine(DB_URI)

Base = declarative_base(engier)

class User(Base):
	__tablename__ = 'user'
	
	id = Column(Integer, primary_key=True, autoincrement=True)
	username = Column(String(50), nullable=False)

Base.metadata.drop_all()
Base.metadata.create_all()
 
