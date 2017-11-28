from flask import request, jsonify
from flask import session
from werkzeug.security import check_password_hash

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
