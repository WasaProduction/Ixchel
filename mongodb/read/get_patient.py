from data_models.patient.model_patient import ModelPatient
from data_models.model_diagnosis import ModelDiagnosis
from mongodb.connection_handlers.mongo_local_database import MongoLocalDatabase
from datetime import datetime
import re


class GetPatient(ModelPatient):
    def __init__(self, username=''):
        super().__init__(username=username)
        # Get DB collections
        self.users = MongoLocalDatabase('users').collection
        self.diagnoses = MongoLocalDatabase('diagnosis').collection
        # Set patient info
        self.username = username
        self.get_patient_basics()

    def get_patient_basics(self):
        regex_string = r"^\b({})\b$".format(self.username)
        custom_regex = re.compile(regex_string, re.IGNORECASE)
        # Query DB
        user_query = self.users.find({"username": custom_regex}, {})
        # Digest JSON answer
        self.json_into_self(user_query)
        # Fetch further data
        self.get_patient_diagnoses()

    def json_into_self(self, json):
        for index, element in enumerate(json):
            if index == 0:
                self.object_id = element['_id']
                self.user_id = element['user_id']
                self.username = element['username']
                self.name = element['name']
                self.lastname_1 = element['lastname_1']
                self.lastname_2 = element['lastname_2']

    def get_patient_diagnoses(self):
        regex_string = r"^\b({})\b$".format(self.object_id)
        custom_regex = re.compile(regex_string, re.IGNORECASE)
        # Query DB
        diagnoses_query = self.diagnoses.find({"patient_id": custom_regex}, {})
        # Digest JSON
        self.json_into_diagnoses(diagnoses_query)

    def json_into_diagnoses(self, json):
        for element in json:
            self.diagnosis_entries.append(ModelDiagnosis(diagnosis_id=element['_id'], created_by=element['created_by'],
                                                         patient_id=element['patient_id'],
                                                         diagnosis=element['diagnosis'],
                                                         tags_contained=element['tags_contained'],
                                                         creation_date=datetime.strptime(element['creation_date'],
                                                                                         "%m/%d/%Y, %H:%M:%S")))
