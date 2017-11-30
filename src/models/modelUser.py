# coding:utf-8
from sqlalchemy import func

from src import db


class User(db.Model):
    __tablename__ = 't_users'
    id = db.Column('f_id', db.Integer, primary_key=True, autoincrement=True, index=True)
    name = db.Column('f_userName', db.String(80), unique=True, nullable=False, server_default='anonymous', index=True)
    password = db.Column('f_password', db.String(80), nullable=False, server_default='123456')
    email = db.Column('f_email', db.String(80), unique=True, nullable=True, server_default='')
    cellPhone = db.Column('f_cellPhone', db.String(30), unique=True, nullable=True, server_default='')
    registerDate = db.Column('f_registerDate', db.DateTime, unique=False, nullable=False, server_default=func.now())
    lastLoginDate = db.Column('f_lastLoginDate', db.DateTime, unique=False, nullable=False,server_default=func.now())
    deleteFlag = db.Column('f_delete', db.Integer, unique=False, nullable=False, default=0)

    def __init__(self, name, password, email, cellPhone):
        self.name = name
        self.password = password
        self.email = email
        self.cellPhone = cellPhone

    def __repr__(self):
        return '<User %r>' % self.name

    def dump_datetime(self, value):
        """Deserialize datetime object into string form for JSON processing."""
        if value is None:
            return None
        return [value.strftime("%Y-%m-%d"), value.strftime("%H:%M:%S")]

    @property
    def serialize_many2many(self):
        """
        Return object's relations in easily serializeable format.
        NB! Calls many2many's serialize property.
        """
        return [item.serialize for item in self.many2many]

    # use e.g. return jsonify(json_list=[i.serialize for i in qryresult.all()])
    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.id,
            'name': self.name,
            'password': self.password,
            'email': self.email,
            'cellPhone': self.cellPhone,
            'registerDate': self.dump_datetime(self.registerDate),
            'lastLoginDate': self.dump_datetime(self.lastLoginDate),
            'deleteFlag': self.deleteFlag
            # This is an example how to deal with Many2Many relations
            # 'many2many': self.serialize_many2many
        }
