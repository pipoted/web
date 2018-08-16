from flask import Flask, views, render_template, request
from blinker import Namespace
from signals import login_signal

app = Flask(__name__)


# namespace = Namespace()
# fire_signal = namespace.signal('fire')
#
#
# def fire_start(sender):
#     print(sender)
#     print('fire start')
# fire_signal.connect(fire_start)
#
#
# fire_signal.send()

@app.route('/')
def hello_world():
	return 'Hello World!'


class LoginViews(views.MethodView):
	
	def get(self):
		return render_template('login.html')
	
	def post(self):
		username = request.args.get('username')
		# password = request.args.get('password')
		
		if username == 'xzx':
			login_signal.send()
			return 'success login'
		else:
			return 'error'


app.add_url_rule('/login/', endpoint='login',
                 view_func=LoginViews.as_view('login'))

if __name__ == '__main__':
	app.run(debug=True)
