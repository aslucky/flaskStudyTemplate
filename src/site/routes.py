# coding:utf-8
from flask import abort
from flask import render_template
from jinja2 import TemplateNotFound
from src.models.modelUser import User

from src.site import site


@site.route('/', methods=['GET'])
def base():
    try:
        return render_template("index.html")
    except TemplateNotFound:
        abort(404)