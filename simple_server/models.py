import json

from utils import log


def save(data, path):
	"""
	
	:param data:
	:param path:
	:return:
	"""
	s = json.dumps(data, indent=2, ensure_ascii=False)
	with open(path, 'w+', encoding='utf-8') as f:
		s = f.read()
		log('save', path, s, data)
		return json.loads(s)


def load(path):
	"""
	
	:param path:
	:return:
	"""
	with open(path, 'r', encoding='utf-8') as f:
		s = f.read()
		log('load', s)
		return json.loads(s)


class Modle(object):
	
	
	@classmethod
	def db_path(cls):
		classname = cls.__name__
		path = '{}.txt'.format(classname)
		return path
	
	
	@classmethod
	def all(cls):
		path = cls.db_path()
		models = load(path)
		ms = [cls.__new__(m) for m in models]
		return ms
	
	
	def save(self):
		models = self.all()
		log('models', models)
		models.append(self)
		l = [m.__dict__ for m in models]
		path = self.db_path()
		save(l, path)
	
	
	def __repr__(self):
		classname = self.__class__.__name__
		properties = ['{}: ({})'.format(k, v) for k, v in
			self.__dict__.items()]
		s = '\n'.join(properties)
		return '<{}\n{}>\n'.format(classname, s)


class User(Modle):
	
	
	def new(self, form):
		self.username = form.get('username', '')
		self.password = form.get('password', '')
	
	
	def validate_login(self):
		return self.username == 'gua' and self.password == '123'
	
	
	def validate_register(self):
		return len(self.username) > 2 and len(self.password) > 2


class Message(Modle):
	
	
	def new(self, form):
		self.author = form.get('author', '')
		self.message = form.get('message', '')
