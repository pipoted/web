import os

HOSTNAME = '127.0.0.1'
PORT     = '3306'
DATABASE = 'bbs'
USERNAME = 'root'
PASSWORD = 'xzx199110'

DB_URI = "mysql+pymysql://{username}:{password}@{host}:{port}/{database}?charset=utf8".\
	format(
    username = USERNAME,
    password = PASSWORD,
    host     =  HOSTNAME,
    port     =  PORT,
    database =  DATABASE
)

SQLALCHEMY_DATABASE_URI = DB_URI

SQLALCHEMY_TRACK_MODIFICATIONS = False

SECRET_KEY = os.urandom(25)

DEBUG = True

CMS_USER_ID = 'HAPPYHACKINGCODING'
