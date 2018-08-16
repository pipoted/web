from sqlalchemy import (
	create_engine, Column, Integer, String, Text, ForeignKey,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship, backref

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

class User(Base):
	__tablename__ = 'user'
	
	id = Column(Integer, primary_key=True, autoincrement=True)
	username = Column(String(50), nullable=False)
	
	# extend = relationship('UserExtend', uselist=False)
	
	# article = relationship('Article')
	
	def __repr__(self):
		return '<User.username:%s>' % self.username
	
class UserExtend(Base):
	__tablename__ = 'userextend'
	
	id = Column(Integer, primary_key=True, autoincrement=True)
	school = Column(String(50), nullable=False)
	
	uid = Column(Integer, ForeignKey('user.id'))
	
	# user = relationship('User', backref='extend')
	user = relationship('User', backref=backref('extend', uselist=False))
	

class Article(Base):
	__tablename__ = 'article'
	
	id = Column(Integer, primary_key=True, autoincrement=True)
	title = Column(String(100), nullable=False)
	content = Column(Text, nullable=False)
	
	uid = Column(Integer, ForeignKey('user.id', ondelete='RESTRICT'))
	
	author = relationship('User', backref='articles')
	
	def __repr__(self):
		return '<Article(title:%s, content:%s)>' % (
			self.title, self.content
		)
	
# Base.metadata.drop_all()
# Base.metadata.create_all()
#
#
# user = User(username='xiao')
# session.add(user)
# session.commit()
#
# article = Article(title='jian', content='test', uid=1)
# session.add(article)
# session.commit()
# article = session.query(Article).first()
# uid = article.uid
# print(article)
# user = session.query(User).get(uid)
# print(user)

# article = session.query(Article).first()
# print(article.author.username)

# user = session.query(User).first()
# print(user.article)
user = User(username='xiao')
extend1 = UserExtend(school='nt')

print(type(user.extend))


article1 = Article(title='text1', content='test')
article2 = Article(title='text2', content='fjsdkfj')

# user.articles.append('article1')
# user.articles.append('article2')
user.extend = extend1

session.add(user)
session.commit()


