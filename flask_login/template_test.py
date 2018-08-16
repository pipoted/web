from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
	return 'hello world'


@app.route('/index/')
def index():
	username = 'xiaojian'
	content = {
		'username': username,
		'age'     : 16,
	}
	return render_template('template.html', **content)


if __name__ == '__main__':
	app.run()
