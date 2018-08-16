from flask import Flask, url_for, request, redirect, render_template

app = Flask(__name__)


@app.route('/login/')
def login():
	return 'this is login page'


@app.route('/profile/', methods=['GET', 'POST'])
def profile():
	if not request.args.get('user'):
		return redirect(url_for('login'))

	return "can't be here"


@app.route('/test/')
def test():
	return render_template('href_test.html')


if __name__ == '__main__':
	app.run(debug=True)
