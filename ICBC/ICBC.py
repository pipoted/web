from flask import Flask, render_template, views, request
from forms import RegistForm
from exts import db
from models import User
import config


app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)



@app.route('/')
def index():
    return render_template('index.html')


class RegistViews(views.MethodView):
   
    def get(self):
        return render_template('regist.html')
    
    def post(self):
        form = RegistForm(request.form)
        if form.validate():
            email = form.email.data
            username = form.username.data
            password = form.password.data
            user = User(email=email, username=username,
                        password=password)
            db.session.add(user)
            db.session.commit()
            return '注册成功'
        else:
            print(form.errors)
            return 'error'
    
app.add_url_rule('/regist/', endpoint='regist',
                 view_func=RegistViews.as_view('regist'))



if __name__ == '__main__':
    app.run(debug=True)
