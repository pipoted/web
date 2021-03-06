from wtforms import Form, FileField, StringField
from wtforms.validators import InputRequired
from flask_wtf.file import FileRequired, FileAllowed

class UploadForm(Form):
	avatar = FileField(validators=[FileRequired(), FileAllowed(
		['jpg','png','gig']
	)])
	desc = StringField(validators=[InputRequired()])
	
