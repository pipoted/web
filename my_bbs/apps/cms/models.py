from exts import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash


class CMSUser(db.Model):
	__tablename__ = 'cms_user'
	
	id        = db.Column(db.Integer     , primary_key  = True, autoincrement = True)
	username  = db.Column(db.String(50)  , nullable     = False)
	_password = db.Column(db.String(100) , nullable     = False)
	email     = db.Column(db.String(50)  , nullable     = False, unique = True)
	join_time = db.Column(db.DateTime    , default      = datetime.now)
	
	
	def __init__(self, username, password, email):
		self.username = username
		self.password = password
		self.email    = email
	
	# 密码明文存在数据库中并不安全,所以要进行加密处理
	# 密码对外显示明文password, 对内显示_password,在模型中对密码进行加密,将
	# 加密好的密码存入到数据库中,取出时进行解密
	
	@property
	def password(self):
		return self._password
	
	@password.setter
	def password(self, raw_password):
		self._password = generate_password_hash(raw_password)
	
	def check_password(self, raw_password):
		result = check_password_hash(self.password, raw_password)
		return result
	
