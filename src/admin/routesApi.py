import datetime

import decimal
from flask import request, jsonify, json
from flask import session
from werkzeug.security import check_password_hash, generate_password_hash

from src import db
from src.admin import admin
from src.models.modelUser import User


@admin.route('/api/v1.0/login', methods=['POST'])
def login():
    if not request.is_json:
        return jsonify({'code': 1, 'msg': '请使用JSON格式的请求'})

    try:
        data = request.get_json()
        if not data.get('username'):
            return jsonify({'code': -1, 'msg': '缺少必要参数-username'})
        if not data.get('password'):
            return jsonify({'code': -2, 'msg': '缺少必要参数-password'})
        user = User.query.filter_by(name=data['username']).first()
        if not user:
            return jsonify({'code': 10, 'msg': '未找到该用户'})

        if not check_password_hash(user.password, request.get_json()['password']):
            return jsonify({'code': 11, 'msg': '密码验证失败'})
        else:
            session['userName'] = user.name
            return jsonify({'code': 0, 'msg': '验证成功'})
    except:
        import traceback
        traceback.print_exc()
        errMsg = traceback.format_exc()
        print(errMsg)
        return jsonify({'code': 100, 'msg': '后台处理出现异常情况，请稍后在试'})


def alchemyencoder(obj):
    """JSON encoder function for SQLAlchemy special classes."""
    if isinstance(obj, datetime.date):
        return obj.isoformat()
    elif isinstance(obj, decimal.Decimal):
        return float(obj)


@admin.route('/api/v1.0/users', methods=['GET'])
def users():
    # jquery 表格接口
    page = request.values.get('page')
    rows = request.values.get('rows')

    if not page or not rows:
        return jsonify({'total': 1, 'rows': ''})
    try:
        users = User.query.all()
        return jsonify({'total': len(users), 'rows': [i.serialize for i in users]})
    except:
        import traceback
        traceback.print_exc()
        errMsg = traceback.format_exc()
        print(errMsg)
        return jsonify({'code': 100, 'msg': '后台处理出现异常情况，请稍后在试'})


@admin.route('/api/v1.0/users', methods=['POST'])
def addUsers():
    # jquery 表格接口
    try:
        name = request.values.get('name')
        if not name:
            return jsonify({'msg': '必要参数不存在', 'code': 102})
        isExist = User.query.filter_by(name=name).first()
        if isExist:
            return jsonify({'msg': '用户已存在', 'code': 101})

        password = generate_password_hash(request.values.get('password'), method='sha256')
        email = request.values.get('email')
        cellPhone = request.values.get('cellPhone')



        user = User(name, password, email, cellPhone)
        db.session.add(user)
        db.session.commit()

        return jsonify({'msg': '', 'code': 0})
    except:
        import traceback
        traceback.print_exc()
        errMsg = traceback.format_exc()
        print(errMsg)
        return jsonify({'code': 100, 'msg': '后台处理出现异常情况，请稍后在试'})


@admin.route('/api/v1.0/users', methods=['DELETE'])
def deleteUsers():
    # jquery 表格接口
    try:
        id = request.values.get('id')
        mod = User.query.filter_by(id=id).first()
        db.session.delete(mod)
        db.session.commit()

        return jsonify({'msg': '', 'code': 0})
    except:
        import traceback
        traceback.print_exc()
        errMsg = traceback.format_exc()
        print(errMsg)
        return jsonify({'code': 100, 'msg': '后台处理出现异常情况，请稍后在试'})


@admin.route('/api/v1.0/users', methods=['PUT'])
def modifyUsers():
    # jquery 表格接口
    try:
        id = request.values.get('id')
        name = request.values.get('name')
        password = generate_password_hash(request.values.get('password'), method='sha256')
        email = request.values.get('email')
        cellPhone = request.values.get('cellPhone')

        numId = int(id)

        isExist = User.query.filter_by(name=name).first()
        if isExist and isExist.id != numId:
            return jsonify({'msg': '用户已存在', 'code': 101})

        isExist = User.query.filter_by(cellPhone=cellPhone).first()
        if isExist and isExist.id != numId:
            return jsonify({'msg': '电话已存在', 'code': 101})

        isExist = User.query.filter_by(email=email).first()
        if isExist and isExist.id != numId:
            return jsonify({'msg': '邮箱已存在', 'code': 101})

        user = User.query.filter_by(id=id).first()
        user.name = name
        user.email = email
        user.password = password
        user.cellPhone = cellPhone
        db.session.commit()

        return jsonify({'msg': '', 'code': 0})
    except:
        import traceback
        traceback.print_exc()
        errMsg = traceback.format_exc()
        print(errMsg)
        return jsonify({'code': 100, 'msg': '后台处理出现异常情况，请稍后在试'})
