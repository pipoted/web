from flask import Flask, request, Response

app = Flask(__name__)


@app.route('/')
def hello_world():
    resp = Response('hello world')
    resp.set_cookie('useranme', 'xiao', max_age=60)
    return resp

@app.route('/del/')
def delete_cookies():
    resp = Response('hello world')
    resp.delete_cookie('username')
    return resp

if __name__ == '__main__':
    app.run()
