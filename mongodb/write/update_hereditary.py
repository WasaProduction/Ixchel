from mongodb.connection_handlers.mongo_local_database import MongoLocalDatabase
from JSON.JsonifyModel.HereditaryModel import HereditaryModel


class HereditaryMongo:
    def __init__(self):
        try:
            self.db = MongoLocalDatabase('hereditary')
        except:
            print("Upgrade exception at write_json_diagnosis")


class UpdateHereditary(HereditaryMongo):
    def __init__(self, content):
        super().__init__()
