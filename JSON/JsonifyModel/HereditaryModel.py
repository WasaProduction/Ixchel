from mongodb.connection_handlers.mongo_local_database import MongoLocalDatabase


class HereditaryModel:
    def __init__(self, hereditary_model):
        self.hereditary_model = hereditary_model

    def model_into_json(self):
        # Obj into dictionary
        dictionary = {
            "patient_id": self.hereditary_model.diagnosis_id,
            "last_modify_by": self.hereditary_model.creation_date,
            "last_update": self.hereditary_model.created_by,
            "background": self.hereditary_model.patient_id,
            "creation_date": self.hereditary_model.diagnosis,
        }
        return dictionary
