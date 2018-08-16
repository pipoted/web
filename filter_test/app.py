from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def hello_world():
	context = {
		'js'         : "<script>alert('hello')</script>",
		'test_str'   : 'hello hello world',
		'create_time': datetime(2018, 7, 30, 4, 23, 43, 54)
	}
	return render_template('test.html', **context)


@app.template_filter('my_cut')
def cut(value):
	"""

	:type value: str
	"""
	return value.replace('hello', ' ')


@app.template_filter('deal_time')
def deal_time(time):
	"""

	:type time: datetime
	"""
	if isinstance(time, datetime):
		now = datetime.now()
		timestamp = (now - time).total_seconds()

		if timestamp < 60:
			return 'just a while'
		elif 60 <= timestamp < 60 * 60:
			minutes = timestamp / 60
			return '%s minutes later' % int(minutes)
		elif 60 * 60 <= timestamp < 60 * 60 * 24:
			hours = timestamp / (60 * 60)
			return '%s hour later' % int(hours)
		elif 60 * 60 * 24 <= timestamp < 60 * 60 * 24 * 30:
			days = timestamp / (60 * 60 * 24)
			return '%s days later' % int(days)
		else:
			return 'elllll'
	else:
		return time


if __name__ == '__main__':
	app.run(debug=True)
