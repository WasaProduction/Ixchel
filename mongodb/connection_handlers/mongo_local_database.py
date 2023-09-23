from pymongo import MongoClient


class MongoLocalDatabase:
    def __init__(self, collection):
        MONGO_URI = 'mongodb://localhost'
        local_client = MongoClient(MONGO_URI)
        self.db = local_client['Ixchel']
        self.collection = self.db[collection]

    def insert_into_collection(self, my_dictionary):
        self.collection.insert_one(my_dictionary)

    @property
    def collection(self):
        return self._collection

    @collection.setter
    def collection(self, value):
        self._collection = value
