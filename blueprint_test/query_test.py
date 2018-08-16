from sqlalchemy import (
	create_engine, Column, Integer, Enum, Float, func,
	String, Date
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import enum
from datetime import date
import random

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

class Article(Base):
	__tablename__ = 'article'
	
	id    = Column(Integer, primary_key = True, autoincrement = True)
	title = Column(String(50), nullable=False)
	price = Column(Float, nullable=False)
	
	def __repr__(self):
		return 'Article<title:%s>' % self.title

Base.metadata.drop_all()
Base.metadata.create_all()

for num in range(10):
	article = Article(title=f'title{num}',
	                  price=float(random.randint(0, 100)))
	
	session.add(article)
	
session.commit()

# articles = session.query(Article).all()
# for num, article in enumerate(start=1, iterable=articles):
# 	print(num)
# 	print(article)
# 	print(article.price)
# 	print(article.title)

# articles = session.query(Article.title, Article.price).all()
# for article in articles:
# 	print(article)
	

# articles = session.query(Article).filter(Article.title == 'title0').first()
# articles = session.query(Article).filter(Article.title != 'title0').first()
# articles = session.query(Article).filter(Article.title.like('title%')).all()
# articles = session.query(Article).filter(Article.title.in_(
# 		['title1', 'title2'])
# 	).all()
articles = session.query(Article).filter(~Article.title.in_(
	['title1', 'title2']
)).all()
print(articles)
