# coding:utf-8
from src import db


class User(db.Model):
    __tablename__ = 't_users'
    id = db.Column('f_id', db.Integer, primary_key=True, autoincrement=True, index=True)
    name = db.Column('f_userName', db.String(80), unique=True, nullable=False, server_default='anonymous', index=True)
    password = db.Column('f_password', db.String(80), nullable=False, server_default='123456')
    email = db.Column('f_email', db.String(80), unique=True, nullable=True, server_default='')
    cellPhone = db.Column('f_cellPhone', db.String(30), unique=True, nullable=True, server_default='')

    def __init__(self, name, password, email):
        self.name = name
        self.password = password
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.name
