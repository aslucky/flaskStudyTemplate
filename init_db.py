# coding:utf-8
import os
from werkzeug.security import generate_password_hash
from src import db, create_app
from src.models.modelUser import User
if __name__ == "__main__":
    app = create_app(os.getenv('FLASK_CONFIG') or 'default')
    with app.app_context():
        # 创建数据库表，通过migrate创建，这里注释掉
        # db.create_all()
        admin = User('admin', generate_password_hash('123456', method='sha256'),'admin@126.com')
        db.session.add(admin)
        db.session.commit()
        print(User.query.all())
        print(User.query.filter_by(name='admin').first())