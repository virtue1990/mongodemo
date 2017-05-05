from pymongo import MongoClient
from unittest import TestCase,main
host = '127.0.0.1'
port = 27017
class TestMongoCase(TestCase):
    '''
    write for python mongo basic operation
    '''

    def setUp(self):
        self.host = host
        self.port = port
        self.client = MongoClient(host=host,port=port)

    def test_print_db(self):
        client = self.client
        dbs = client.database_names()
        self.assertTrue(dbs is not None)

    def test_print_collection(self):
        client = self.client
        db = client.get_database('virtue')
        collnames = db.collection_names()
        self.assertTrue(collnames,'the collections is null')

    def test_insert_document(self):
        client = self.client
        db = client.get_database('virtue')
        collname = db.get_collection('virtue')
        data ={
            'name': 'virtue',
            'db':'mongo'
        }
        res = collname.insert(data)
        self.assertIsNotNone(res)

    def test_update_document(self):
        client = self.client
        db = client.get_database('virtue')
        collname = db.get_collection('virtue')
        data = {
            'append': 'logname'
        }
        res = collname.update({'name':'virtue'},{'$set':data})
        self.assertTrue(res.get('updatedExisting'),'update failed')

    def test_delete_document(self):
        client = self.client
        db = client.get_database('virtue')
        collname = db.get_collection('virtue')
        res = collname.delete_one({'name':'virtue'})
        self.assertTrue(res.raw_result['ok'],'delete is fail')
        res = collname.delete_many({'name':'virtue'})
        self.assertTrue(res.raw_result['ok'],'delete many failed')

    def test_query_document(self):
        client = self.client
        db = client.get_database('virtue')
        collname = db.get_collection('virtue')
        res = collname.find({'name':'virtue'})
        self.assertTrue(res.count(),'query failed')


if __name__ == '__main__':
    main()
