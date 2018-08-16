from flask import Flask
from exts import db
from apps.cms import bp as cms_bp
import config



def create_app():
    
    app = Flask(__name__)
    app.config.from_object(config)
    
    app.register_blueprint(cms_bp)
    
    db.init_app(app)
    
    return app




if __name__ == '__main__':
    app = create_app()
    app.run()
