from flask import (
	Flask, render_template, request, views, session, url_for
)
from exts import db
from forms import RegistForm, LoginForm
from models import User
from flask_wtf import CSRFProtect
import config

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)

CSRFProtect(app)


@app.route('/')
def index():
	return render_template('index.html')

#
# @app.route('/regist/', methods=['GET', 'POST'])
# def regist():
#
# 	errors = ''
#
# 	if request.method == 'GET':
# 		return render_template('regist.html')
# 	else:
#
# 		form = RegistForm(request.form)
# 		if form.Validate():
# 			username = form.username.data
# 			userpass = form.userpass.data
#
# 			user = User(user_name=username, user_pass=userpass)
# 			db.session.add(user)
# 			db.session.commit()
#
# 			return '注册成功'
#
# 		else:
# 			return render_template('regist.html', errors='regist error')


class RegistViews(views.MethodView):
	
	def __init__(self):
		self.error = ''
	
	
	def get(self):
		return render_template('regist.html')
	
	def post(self):
		
		form = RegistForm(request.form)
		
		if form.validate():
			username = form.username.data
			userpass = form.userpass.data
			
			user = User(user_name=username, user_pass=userpass)
			
			db.session.add(user)
			db.session.commit()
			
			return render_template(url_for('login'))
		
		else:
			self.error = 'regist error'
			return render_template('regist.html', error=self.error)



class LoginViews(views.MethodView):
	
	def get(self):
		return render_template('login.html')
	
	def post(self):
		form = LoginForm(request.form)
		
		if form.validate():
			
			username = form.username.data
			userpass = form.userpass.data
			
			user = User.query.filter(
				User.user_name == username,
				User.user_pass == userpass
			).first()
			
			if user:
				session['user_id'] = user.id
				return '登录成功'
			else:
				return '用户名或密码错误'
			
		
app.add_url_rule('/regist/', endpoint='regist',
                 view_func=RegistViews.as_view('regist'))
app.add_url_rule(
	'/login/',
	endpoint='login',
	view_func=LoginViews.as_view('login')
)
		
		

if __name__ == '__main__':
	app.run(debug=True)
