from flask import Flask, request, render_template
from wtforms import Form, StringField
from wtforms.validators import Length, EqualTo

class Register_Form(Form):
    username = StringField(validators=[Length(min=3, max=10)])
    password = StringField(validators=[Length(min=6, max=15)])
    repassword = StringField(validators=[Length(min=6, max=15),
                             EqualTo('password')])
    
    

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/register/', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        # username = request.form.get('username')
        # password = request.form.get('password')
        # re_password = request.form.get('repassword')
        # return '%s %s %s' % (username, password, re_password)
        form = Register_Form(request.form)
        if form.validate():
            return 'success'
        else:
            return 'error'


if __name__ == '__main__':
    app.run(debug=True)
