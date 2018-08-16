HOSTNAME = '127.0.0.1'
PORT     = '3306'
DATABASE = 'icbc_sql'
USERNAME = 'root'
PASSWORD = 'xzx199110'

DB_URI = "mysql+pymysql://{username}:{password}@{host}:{port}/{database}".format(
    username = USERNAME,
    password = PASSWORD,
    host     =  HOSTNAME,
    port     =  PORT,
    database =  DATABASE
)

SQLALCHEMY_DATABASE_URI = DB_URI

SQLALCHEMY_TRACK_MODIFICATIONS = False
