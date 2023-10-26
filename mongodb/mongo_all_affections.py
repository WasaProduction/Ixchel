from data_models.model_affections import ModelAffection
from mongodb.connection_handlers.mongo_local_database import MongoLocalDatabase


class MongoAllAffections:
    def __init__(self):
        local_affections = MongoLocalDatabase('afecciones').collection
        self.all_affections = []
        self.json_into_data_model(local_affections.find({}, {'id_cie': 1, 'name': 1}))

    def json_into_data_model(self, json):
        for element in json:
            affection = ModelAffection(id_cie=element['id_cie'])
            # Underscores are used to retain structure
            affection.name = element['name'].replace(' ', '_')
            affection.description = element['description']
            affection.coding_note = element['coding_note']
            affection.inclusions = element['inclusions']
            affection.exclusions = element['exclusions']
            affection.encoded_elsewhere = element['encoded_elsewhere']
            affection.organ = element['organ']
            affection.bone = element['bone']
            affection.chronic = element['chronic']
            self.all_affections.append(affection)
            del affection
