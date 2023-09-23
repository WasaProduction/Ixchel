from data_models.model_affections import ModelAffection
from mongodb.connection_handlers.mongo_local_database import MongoLocalDatabase


class MongoAllAffections:
    def __init__(self):
        local_affections = MongoLocalDatabase('afecciones').collection
        self.all_affections = []
        self.json_into_data_model(local_affections.find({}, {'id_cie': 1, 'nombre': 1}))

    def json_into_data_model(self, json):
        for element in json:
            dummy_item = ModelAffection(id_cie=element['id_cie'])
            # Underscores are used to retain structure
            dummy_item.name = element['nombre'].replace(' ', '_')
            self.all_affections.append(dummy_item)
            del dummy_item
