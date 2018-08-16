from wtforms import Form, StringField, IntegerField
from wtforms.validators import Email, InputRequired, Length


class LoginForm(Form):
	email = StringField(validators=[
		Email(message='错误的邮箱格式'),
		InputRequired(message='请输入邮箱内容')
	])
	
	password = StringField(validators=[
		Length(min=6, max=20,
		       message='密码长度必须在6到20之间')
	])
	
	remember = IntegerField()
