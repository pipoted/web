from flask import Flask, views, request, render_template
from functools import wraps

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'hello world'

def login_check(func):
    @wraps(func)
    def inner(*args, **kwargs):
        username: str = request.form.get('username')
        password: str = request.form.get('password')
        
        if username == 'xiao' and password == '123':
            return func(*args, **kwargs)
        else:
            return 'error'
    return inner
    
        
class List_View(views.MethodView):
    
    @property
    def get(self):
        return render_template('login.html')
    
    @property
    def post(self):
        name = request.form.get
        pwd  = request.form.get
        print(name, pwd)
        
        return 'post'
    
class Profile(views.View):
    decorators = [login_check]
    def dispatch_request(self):
        return 'profile page'


@app.route('/testpage/')
@login_check
def test_page():
    return 'settings page'

app.add_url_rule(
    '/profile/',
    endpoint  = 'profile',
    view_func = Profile.as_view('profile')
)
app.add_url_rule('/list/',
                 endpoint  = 'list',
                 view_func = List_View.as_view('list'))

if __name__ == '__main__':
    app.run(debug=True)
