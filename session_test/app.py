from flask import Flask, session
import os
from datetime import timedelta

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)
app.config['SESSION_PERMANENT_LIFETIME'] = timedelta(hours=2)


@app.route('/')
def hello_world():
    session['username'] = 'xiao'
    session.permanent = True
    return 'Hello World!'


@app.route('/get_session/')
def get_session():
    username = session.get('username')
    return username or 'none'

@app.route('/del_session/')
def del_session():
    session.pop('username')
    session.clear()
    return 'delete success'

if __name__ == '__main__':
    app.run()
