from mongodb.connection_handlers.mongo_local_database import MongoLocalDatabase


class JsonDiagnosis:
    def __init__(self, json_diagnosis_model):
        self.JsonDiagnosisModel = json_diagnosis_model
        try:
            self.db = MongoLocalDatabase('diagnosis')
        except:
            print("Upgrade exception at write_json_diagnosis")

# Data to be written
    def model_into_json(self):
        # Obj into dictionary
        dictionary = {
            "diagnosis_id": self.JsonDiagnosisModel.diagnosis_id,
            "creation_date": self.JsonDiagnosisModel.creation_date,
            "created_by": self.JsonDiagnosisModel.created_by,
            "patient_id": self.JsonDiagnosisModel.patient_id,
            "diagnosis": self.JsonDiagnosisModel.diagnosis,
            "tags_contained": self.JsonDiagnosisModel.tags_contained
        }
        return dictionary

    def insert_into_db(self):
        self.db.insert_into_collection(self.model_into_json())
