import pymongo
__author__ = 'dhairya'


class Database(object):
    URI = "mongodb://127.0.0.1:27017"
    DATABASE = None

    def __init__(self):
        pass

    @staticmethod
    def initialize():
        client = pymongo.MongoClient(Database.URI)
        Database.DATABASE = client['fullstack']

    @staticmethod
    # collection.insert() inbuilt method
    def insert(collection, data):
        Database.DATABASE[collection].insert(data)


    @staticmethod
    # collection.find() inbuilt method
    def find(collection, query):
        return Database.DATABASE[collection].find(query)


    @staticmethod
    # collection.find_one() inbuilt method
    def find_one(collection, query):
        return Database.DATABASE[collection].find_one(query)
