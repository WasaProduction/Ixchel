from mongodb.connection_handlers.mongo_local_database import MongoLocalDatabase


class JsonDiagnosis:
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
            "diagnosis_id": self.JsonTreatmentModel.patient_id,
            "creation_date": self.JsonTreatmentModel.medic_id,
            "created_by": self.JsonTreatmentModel.drug,
            "patient_id": self.JsonTreatmentModel.instruction
        }
        return dictionary

    def insert_into_db(self):
        self.db.insert_into_collection(self.model_into_json())
