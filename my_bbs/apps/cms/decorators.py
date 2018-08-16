from flask import session, redirect, url_for
from functools import wraps
import config


def login_require(func):
	"""
	验证用户是否登录,登录继续进行该功能,否则跳转到登录页面
	:param func:被装饰的目标函数
	:return:验证已经登录则执行功能,否则跳转登录页面
	"""
	@wraps(func)
	def inner(*args, **kwargs):
		
		if config.CMS_USER_ID in session:
			return func(*args, **kwargs)
		
		else:
			return redirect(url_for('cms.login'))
	return inner
