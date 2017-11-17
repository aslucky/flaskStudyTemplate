from src.admin import admin


@admin.route('/')
def index():
    return '{"result":"admin page"}';