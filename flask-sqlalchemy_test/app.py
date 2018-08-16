from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


HOSTNAME = '127.0.0.1'
PORT     = '3306'
DATABASE = 'flask_sql'
USERNAME = 'root'
PASSWORD = 'xzx199110'

DB_URI = "mysql+pymysql://{username}:{password}@{host}:{port}/{database}".format(
    username = USERNAME,
    password = PASSWORD,
    host     =  HOSTNAME,
    port     =  PORT,
    database =  DATABASE
)

app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), nullable=False)
    
    def __repr__(self):
        return '<user:(username:%s)>' % self.username
  
  
class Article(db.Model):
    __tablename__ = 'article'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(50), nullable=False)
    
    uid = db.Column(db.Integer, db.ForeignKey('user.id'))
    
    author = db.relationship('User', backref='articles')

# db.drop_all()
# db.create_all()


# user = User(username='xiao')
# article = Article(title='title one')
# article.author = user
#
# db.session.add(article)
# db.session.commit()

#
# engier = create_engine(DB_URI)
# session = sessionmaker(engier)()
#
# Base = declarative_base(engier)

users = User.query.all()
print(users)
