from mongodb.connection_handlers.mongo_local_database import MongoLocalDatabase


class JsonTreatment:
    def __init__(self, json_treatment_model):
        self.JsonTreatmentModel = json_treatment_model
        try:
            self.db = MongoLocalDatabase('prescriptions')
        except:
            print("Upgrade exception at write_json_prescription")

# Data to be written
    def model_into_json(self):
        # Obj into dictionary
        dictionary = {
            "treatment_id": self.JsonTreatmentModel.treatment_id,
            "creation_date": self.JsonTreatmentModel.creation_date,
            "patient_id": self.JsonTreatmentModel.patient_id,
            "medic_id": self.JsonTreatmentModel.medic_id,
            "instructions": self.JsonTreatmentModel.instructions,
            "active": self.JsonTreatmentModel.active,
            "raw_text": self.JsonTreatmentModel.raw_text
        }
        return dictionary

    def insert_into_db(self):
        print('insertiiiing', self.model_into_json())
        self.db.insert_into_collection(self.model_into_json())
