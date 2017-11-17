# coding:utf-8
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from config import config

db = SQLAlchemy()
migrate = Migrate()


# 使用工厂函数创建实例
def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    db.init_app(app)
    migrate.init_app(app, db)

    # 路由和自定义错误页面
    from src.site.routes import site
    from src.api.routes import api
    from src.admin.routes import admin

    app.register_blueprint(site)
    app.register_blueprint(api, url_prefix='/api/v1.0')
    app.register_blueprint(admin, url_prefix='/admin')

    return app
