from flask_script import Manager
from app import app
from flask_migrate import Migrate, MigrateCommand
from exts import db

manage = Manager(app)
Migrate(app, db)
manage.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manage.run()
