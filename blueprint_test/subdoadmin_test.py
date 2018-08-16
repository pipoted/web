from flask import Blueprint

cms_bp = Blueprint('cms', __name__, subdomain='cms')

@cms_bp.route('/')
def index():
	return 'this is cms page'
