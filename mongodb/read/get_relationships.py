from mongodb.connection_handlers.mongo_local_database import MongoLocalDatabase


class GetRelationships:
    def __init__(self):
        self.collection = MongoLocalDatabase('relationships').collection
        self.relationships_dict = {}
        self.get_relationships_dict()

    def get_relationships_dict(self):
        self.digest_json(self.collection.find())

    def digest_json(self, json):
        for element in json:
            self.relationships_dict = element
        del self.relationships_dict['_id']
