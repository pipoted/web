from flask import Flask, request, render_template, redirect

app = Flask(__name__)


@app.route('/')
def hello_world():
    return redirect('/login/')


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        if request.args.get('username') and request.args.get('password'):
            return 'success'

    # return redirect('/login/')
    return 'success'


if __name__ == '__main__':
    app.run(debug=True)
