from flask import Flask, url_for
from flask_restful import Api, Resource, reqparse, fields, marshal_with
from exts import db
from models import User, Article, Tag
from articleviews import article_db
import config

app = Flask(__name__)
app.config.from_object(config)

db.init_app(app)
app.register_blueprint(article_db)


# class LoginView(Resource):
# 	resource_fields = {
# 		'username': fields.String,
# 		'password': fields.String,
# 		'age'     : fields.Integer
# 	}
#
# 	@marshal_with(resource_fields)
# 	def post(self):
# 		parser = reqparse.RequestParser()
# 		parser.add_argument('username', type=str, help='username confirm '
# 		                                               'error')
# 		parser.add_argument('password', type=str, help='password error')
#
# 		args = parser.parse_args()
# 		print(args)
# 		return 'username'
#
#
# api.add_resource(LoginView, '/login/', endpoint='login')
#
# with app.test_request_context():
# 	print(url_for('login'))


@app.route('/', methods=['GET', 'POST'])
def index():
	user = User(username='xiao', email='xxxx@qq.com')
	article = Article(title='title one', content='fasdf')
	article.author = user
	tag = Tag(name='python')
	tag2 = Tag(name='java')
	
	article.tags.append(tag)
	article.tags.append(tag2)
	
	db.session.add(article)
	db.session.commit()
	return 'index page'


if __name__ == '__main__':
	app.run(debug=True)
