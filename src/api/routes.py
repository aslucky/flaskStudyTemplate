from src.api import api


@api.route('/users')
def getUsers():
    return '{"result":"users info"}';