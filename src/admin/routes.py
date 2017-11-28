from functools import wraps

from flask import abort
from flask import redirect
from flask import render_template
from flask import session
from flask import url_for
from jinja2 import TemplateNotFound

from src.admin import admin


def login_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if 'userName' in session:
            return f(*args, **kwargs)
        else:
            session["needlogin"] = True
            return redirect(url_for('.index'))

    return decorated


@admin.route('/')
def index():
    try:
        # 已经登录了
        if 'userName' in session:
            return redirect(url_for('.dashboard'))
        else:
            return render_template("adminLogin.html")
    except TemplateNotFound:
        abort(404)


@admin.route('/login')
# @login_required
def test1():
    try:
        return render_template("adminLogin.html")
    except TemplateNotFound:
        abort(404)


@admin.route('/dashboard')
@login_required
def dashboard():
    try:
        return render_template("adminDashboard.html")
    except TemplateNotFound:
        abort(404)


@admin.route('/userManage')
# @login_required
def userManage():
    try:
        return render_template("userManage.html")
    except TemplateNotFound:
        abort(404)


@admin.route('/deviceManage')
# @login_required
def deviceManage():
    try:
        return render_template("deviceManage.html")
    except TemplateNotFound:
        abort(404)


@admin.route('/base')
# @login_required
def adminbase():
    try:
        return render_template("navBar.html")
    except TemplateNotFound:
        abort(404)


@admin.route('/logout', methods=['GET', 'DELETE'])
@login_required
def logout():
    session.pop('userName', None)
    return redirect(url_for('admin.index'))
