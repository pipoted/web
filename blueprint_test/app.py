from flask import Flask
from subdoadmin_test import cms_bp
from user import user_bp

app = Flask(__name__)
app.register_blueprint(user_bp)
app.register_blueprint(cms_bp)
# app.register_blueprint(user_test)
# app.register_blueprint(news_bp)

@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True)
