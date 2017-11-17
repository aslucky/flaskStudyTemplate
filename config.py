# coding:utf-8
import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    DEBUG = False
    TESTING = False
    # 登录设置 session cookie使用
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'catsknowsSECRETkEY'

    # database config
    # mysql+pymysql://name:password@localhost/db_name
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DEV_DATABASE_URL') or 'mysql+pymysql://gisServer:adminGisServer@localhost:3306/flaskStudy'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DEV_DATABASE_URL') or 'mysql+pymysql://gisServer:adminGisServer@localhost:3306/flaskStudy'


class TestingConfig(Config):
    TESTING = True


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DEV_DATABASE_URL') or 'mysql+pymysql://gisServer:adminGisServer@localhost:3306/flaskStudy'


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}