from wtforms import Form, StringField
from wtforms.validators import Email, Length

class RegistForm(Form):
	email = StringField(validators=[Email()])
	username = StringField(validators=[Length(min=3, max=10)])
	password = StringField(validators=[Length(6, 20)])
