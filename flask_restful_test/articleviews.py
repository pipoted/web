from flask import Blueprint, render_template, make_response
from flask_restful import marshal_with, fields, Resource, Api

from models import Article

article_db = Blueprint('article', __name__, url_prefix='/articles')

api = Api(article_db)

@api.representation('text/html')
def output_html(data, code, headers):
	
	resp = make_response(data)
	return resp


class ArticleView(Resource):
	resource_fields = {
		'title'  : fields.String,
		'content': fields.String,
		'author' : fields.Nested({
			'username': fields.String,
			'email'   : fields.String
		}),
		'tag'    : fields.List(
			fields.Nested({
				'id'  : fields.Integer,
				'name': fields.String
			})
		)
	}
	
	@marshal_with(resource_fields)
	def get(self, article_id):
		article = Article.query.get(article_id)
		return article

api.add_resource(ArticleView, '/article/<article_id>/', endpoint='article')

class ListView(Resource):
	def get(self):
		return render_template('index.html')

api.add_resource(ListView, '/list/', endpoint='list')
