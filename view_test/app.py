from flask import Flask, url_for

app = Flask(__name__)


@app.route('/', endpoint='hello')
def hello_world():
    print(url_for('test'))
    return 'Hello World!'


def list():
    return 'this is a list'


app.add_url_rule('/list/', endpoint='test', view_func=list)

if __name__ == '__main__':
    app.run()
