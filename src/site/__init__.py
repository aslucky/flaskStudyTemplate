# coding:utf-8
from flask import Blueprint

site = Blueprint('site', __name__, template_folder='templates',static_folder='static')

# 末尾导入是为了避免循环导入依赖
from . import routes, errors