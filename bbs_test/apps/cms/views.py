from flask.blueprints import Blueprint

bp = Blueprint('cms', __name__, url_prefix='/cms')


@bp.route('/')
def index():
	return 'this cms page'
