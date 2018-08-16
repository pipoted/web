from flask_script import Manager
from flask_migrate import MigrateCommand, Migrate
from apps.cms import models as cms_models
from bbs import create_app
from exts import db

app = create_app()
CMSUser = cms_models.CMSUser

manage = Manager(app)
Migrate(app, db)
manage.add_command('db', MigrateCommand)


@manage.option('-u' , '--username' , dest='username')
@manage.option('-p' , '--password' , dest='password')
@manage.option('-e' , '--email'    , dest='email')
def create_cms_user(username, password, email):
    user = CMSUser(username=username, password=password, email=email)
    db.session.add(user)
    db.session.commit()
    print('cms用户添加成功.')


if __name__ == '__main__':
    manage.run()
