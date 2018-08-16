from flask import (
	Blueprint, views, render_template, request, session, redirect, url_for
)
from apps.cms.forms import LoginForm
from .models import CMSUser
from .decorators import login_require
import config

bp = Blueprint('cms', __name__, url_prefix='/cms')


@bp.route('/', endpoint='index')
@login_require
def index():
	return render_template('cms/cms_index.html')


# 实现登录功能
class LoginView(views.MethodView):

	def get(self, message=None):
		return render_template('cms/cms_login.html', message=message)
	
	def post(self):
		
		form = LoginForm(request.form)
		if form.validate():
			
			email = form.email.data
			password = form.password.data
			remember = form.remember.data
			print(email, password, remember)
			
			user = CMSUser.query.filter_by(email=email).first()
			print('-----user------', user)
			print(user.check_password(password))
			if user and user.check_password(password):
			
				session[config.CMS_USER_ID] = user.id
				if remember:
					# 如果如下设置为True,则session的过期时间为31天
					session.permanent = True
				
				return redirect(url_for('cms.index'))
			
			else:
				return self.get(message='用户验证失败')
			
		else:
			# print(form.errors)
			message = form.errors.popitem()[1][0]
			return self.get(message=message)


bp.add_url_rule('/login/', endpoint='login', view_func=LoginView.as_view('login'))
