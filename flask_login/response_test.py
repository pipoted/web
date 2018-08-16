from flask import Flask, Response, jsonify
from json import dumps

app = Flask(__name__)


class JSONResponse(Response):

    @classmethod
    def force_type(cls, response, environ=None):
        if isinstance(response, dict):
            response = jsonify(response)
        return super(JSONResponse, cls).force_type(response, environ)


app.response_class = JSONResponse


@app.route('/')
def hello_world():
    return 'hello world'


@app.route('/list/')
def list():
    return {'name': 'xiao'}


if __name__ == '__main__':
    app.run(debug=True)
