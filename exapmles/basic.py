# -*- coding:utf-8 -*-
import pymongo
from pymongo import MongoClient
from config import mongo_url

# mongo clint how to close


class MongoConnection(object):
    def __init__(self):
        self.url = mongo_url

    @property
    def client(self):
        return MongoClient(self.url)

    @property
    def close(self):
        if self.client:
            self.client.close()


class MongoBasicOperation(MongoConnection):
    def __init__(self,database='virtue',collection='virtue'):
        self.database = database
        self.collection = collection
        super(MongoBasicOperation,self).__init__()

    def use_database(self):
        db = self.client.get_database(self.database)
        return db

    def use_collection(self):
        db = self.client.get_database(self.database)
        collection = db.get_collection(self.collection)
        return collection

    def show_databases(self):
        dbs = self.client.database_names()
        return dbs

    def show_collections(self):
        db = self.client.get_database(self.database)
        collections = db.collection_names()
        return collections

    def drop_collection(self):
        db = self.use_database()
        res = db.drop_collection(self.collection)
        return res

    def drop_db(self):
        res = self.client.drop_database(self.database)
        return res

    def document_insert(self,**kwargs):
        if not kwargs:
            raise Exception('the data is None')

        collection = self.use_collection()
        res = collection.insert(kwargs)
        return res

    def document_update(self,condition=None,**kwargs):
        if not isinstance(condition,dict):
            raise Exception('update conditon format is not correct')
        if not kwargs:
            raise Exception('the update data is None')

        collection = self.use_collection()
        res = collection.update(condition,{'$set':kwargs})
        return res

    def document_query(self,condition=None):
        if not isinstance(condition,dict):
            raise Exception('query condition format is not correct')
        collection = self.use_collection()
        res = collection.find(condition)
        return res

    def document_delete(self,condition=None):
        if not isinstance(condition,dict):
            raise Exception('delete condition format is not correct')
        collection = self.use_collection()
        res = collection.delete_one(condition)

    def collection_create_index(self):
        collection = self.use_collection()
        res1 = collection.create_index('title')
        res2 = collection.create_index([('title',pymongo.ASCENDING),
                                        ('name',pymongo.ASCENDING)
                                        ])

        return res1,res2

if __name__ == '__main__':
    mbo = MongoBasicOperation()
    mbo.use_database()
    mbo.use_collection()
    data = {
        'name': 'yongboli',
        'password': 'return',
        'time':'2017-05-07'
    }
    condition={
        'name':'yongboli'
    }
    mbo.document_insert(**data)
    mbo.document_update(condition,**{'time':'2017-05-08'})
    mbo.document_query(condition)
    mbo.document_delete(condition)
    mbo.drop_collection()
    mbo.drop_db()



