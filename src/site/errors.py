# coding:utf-8
from flask import render_template, app

from src.site import site


@site.app_errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@site.app_errorhandler(500)
def internal_server_error(e):
    import traceback
    traceback.print_exc()
    errMsg = traceback.format_exc()
    app.logger.exception('error 500: %s', errMsg)
    return render_template('500.html'), 500
