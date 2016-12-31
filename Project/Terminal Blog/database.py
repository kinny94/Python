import pymongo
__author__ = 'Arjun'

class Database(object):

    #the following variable will remain same through out, that's y not declared under __init__. To access these variable you need to use Database.URI
    URI = "mongodb://127.0.0.1:27017"
    DATABASE = None

    #if we are not using self, we need to use the following
    @staticmethod
    def initialize():
        client = pymongo.MongoClient(Database.URI)
        Database.DATABASE = client['fullstack']

    @staticmethod
    def insert(collection, data):
        Database.DATABASE[collection].insert(data)

    @staticmethod
    def find(collection, query):
        return Database.DATABASE[collection].find(query)

    @staticmethod
    def find_one(collection, query):
        return Database.DATABASE[collection].find_one(query)