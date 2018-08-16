from wtforms import Form, StringField, IntegerField
from wtforms.validators import Length
from models import User


class RegistForm(Form):
	username = StringField(validators=[Length(3, 10)])
	userpass = StringField(validators=[Length(6, 10)])


class LoginForm(Form):
	username = StringField(validators=[Length(3, 10)])
	userpass = StringField(validators=[Length(6, 20)])
	
	def validate(self):
		result = super(LoginForm, self).validate()
		
		if not result:
			return False
		else:
			username = self.username.data
			userpass = self.userpass.data
			
			user = User.query.filter(User.user_name == username,
			                         User.user_pass == userpass)
			
			if not user:
				self.username.errors.append('邮箱或密码错误')
				return False
			else:
				return True
