from flask import Blueprint

user_bp = Blueprint('user', __name__, url_prefix='/user')


@user_bp.route('/userlist/')
def user():
	return 'this is user list page'

