from flask_script import Manager
from app import app
from exts import db
import models
from flask_migrate import MigrateCommand, Migrate

manage = Manager(app)
Migrate(app, db)
manage.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manage.run()
