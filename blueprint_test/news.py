from flask import Blueprint

news_bp = Blueprint('news', __name__, url_prefix='/news')

@news_bp.route('/newstest/')
def new():
	return 'this is news page'
