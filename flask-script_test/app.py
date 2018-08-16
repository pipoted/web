from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import config
from models import User
from exts import db

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)



# class User(db.Model):
#     __tablename__ = 'user'
#
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     username = db.Column(db.String(50), nullable=False)

@app.route('/hello/')
def hello():
    pass


if __name__ == '__main__':
    app.run()
