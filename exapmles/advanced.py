# -*- coding:utf-8 -*-
from mongoengine import *
from config import mongo_url
from mongoengine.context_managers import switch_collection,switch_db
import datetime

class InitConnectDb(object):
    def __init__(self):
        self.init_db()

    def init_db(self):
        connect(mongo_url)
        register_connection('user-db','virtue')
        register_connection('user-db1','virtue1')


class User(Document):
    name = StringField()
    password = StringField(default='123456')
    date_modified = DateTimeField(default=datetime.datetime.now)
    meta = {
        'db_alias':'user-db',
        'collection': 'user-collection'
    }


class UserDynamic(DynamicDocument):
    name = StringField()




def switch_db_operation(class_name=None,db_alias='default'):
    if not class_name:
        raise Exception('class error None,operation failed')

    with switch_db(class_name,db_alias) as f:
        f(name='test').save()


def operation_user_dynamic():
    user = UserDynamic(name='test')
    user.password = 'password'
    user.secret = 'books'
    user.test = 'test'
    user.save()


if __name__ == '__main__':
    operation_user_dynamic()


