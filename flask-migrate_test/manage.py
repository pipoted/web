from flask_migrate import MigrateCommand, Migrate
from exts import db
from xiao import app
from flask_script import Manager
from models import User

manage = Manager(app)
Migrate(app, db)
manage.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manage.run()
