from flask import Flask
from apps.cms import bp as cms_bp
from apps.common import bp as common_bp
from apps.front import bp as front_bp
from exts import db
import config


# config.py 存放配置文件
# exts.py 存放
# models.py 存放模型
# manage.py 执行模型,将表存放到数据库中
# 将前台,后台,公共部分放到不同的蓝图中
# apps存放所有的app(蓝图)

def create_app():
    app = Flask(__name__)
    app.config.from_object(config)
    app.register_blueprint(cms_bp)
    app.register_blueprint(common_bp)
    app.register_blueprint(front_bp)
    
    db.init_app(app)
    
    return app



if __name__ == '__main__':
    app = create_app()
    app.run()
