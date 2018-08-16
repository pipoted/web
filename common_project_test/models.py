from exts import db

class User(db.Model):
	__tablename__ = 'user'
	
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	user_name = db.Column(db.String(20), nullable=False)
	user_pass = db.Column(db.String(20), nullable=True)
