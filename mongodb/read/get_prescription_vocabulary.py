from mongodb.connection_handlers.mongo_local_database import MongoLocalDatabase
from data_models.prescriptions.vocabulary import Vocabulary


class GetPrescriptionVocabulary(Vocabulary):
    def __init__(self):
        super().__init__()
        self.collection = MongoLocalDatabase('prescription_vocab').collection
        self.digest_json(self.collection.find())

    def get_vocabulary(self):
        self.digest_json(self.collection.find())
        return self.actions

    def digest_json(self, json):
        for index, element in enumerate(json):
            self.actions = element['actions']
            self.dose_units = element['dose_units']
            self.dosage_units = element['dosage_units']
            self.duration_units = element['duration_units']
            self.prepositions = element['prepositions']
            self.indication_use = element['indication_use']
            #   Execute only once
            break
