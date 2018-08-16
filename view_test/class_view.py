from flask import Flask, views

app = Flask(__name__)


class List_view(views.View):

	def dispatch_request(self):
		return 'list view'


app.add_url_rule('/list/', endpoint='list', view_func=List_view.as_view('list'))

if __name__ == '__main__':
	app.run()
