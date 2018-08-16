from flask import Flask, request, render_template, redirect

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')

    else:
        name = request.form.get('username')
        pwd = request.form.get('password')

        if name and pwd:
            return redirect('/index/')
    return render_template('login.html')


@app.route('/index/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
