from data_models.patient.model_patient import ModelPatient
from data_models.model_diagnosis import ModelDiagnosis
from data_models.patient.emergency_contacts import EmergencyContacts
from mongodb.connection_handlers.mongo_local_database import MongoLocalDatabase
from datetime import datetime
import re


class GetPatient(ModelPatient):
    def __init__(self, username=''):
        super().__init__(username=username)
        # Set patient info
        self.username = username
        #   Fill data
        self.retrieve_user_data()

    def update_model(self, username=None):
        #   Restore data
        self.restore_model()
        #   Update username
        self.username = username
        #   Fill data
        self.retrieve_user_data()

    def retrieve_user_data(self):
        """     Get patient data        """
        #   Basics
        self.get_patient_basics()
        #   Diagnoses
        self.get_patient_diagnoses()
        #   Immutables
        self.get_patient_immutables()
        #   General info
        self.get_user_general_info()
        #   Contact info
        self.get_user_contact()

    def get_patient_basics(self):
        regex_string = r"^\b({})\b$".format(self.username)
        custom_regex = re.compile(regex_string, re.IGNORECASE)
        # Change collections
        users = MongoLocalDatabase('users').collection
        # Query DB
        user_query = users.find({"username": custom_regex}, {})
        # Digest JSON answer
        self.json_into_self(user_query)

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
        # Change collections
        diagnoses = MongoLocalDatabase('diagnosis').collection
        # Query DB
        diagnoses_query = diagnoses.find({"patient_id": custom_regex}, {})
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

    def get_patient_immutables(self):
        regex_string = r"^\b({})\b$".format(self.user_id)
        custom_regex = re.compile(regex_string, re.IGNORECASE)
        # Change collections
        immutables = MongoLocalDatabase('user_immutable').collection
        # Query DB
        user_query = immutables.find({"user_id": custom_regex}, {})
        # Digest JSON answer
        self.json_into_immutables(user_query)

    def json_into_immutables(self, json):
        for element in json:
            self.immutables.birthday = datetime.strptime(element['birthday'], "%m/%d/%Y, %H:%M:%S")
            self.immutables.date_of_death = element['date_of_death']
            self.immutables.birthplace = element['birthplace']
            self.immutables.blood_type = element['blood_type']
            self.immutables.biological_sex = element['biological_sex']

    def get_user_general_info(self):
        regex_string = r"^\b({})\b$".format(self.user_id)
        custom_regex = re.compile(regex_string, re.IGNORECASE)
        # Change collections
        general_info = MongoLocalDatabase('user_general_info').collection
        # Query DB
        user_query = general_info.find({"user_id": custom_regex}, {})
        # Digest JSON answer
        self.json_into_general_info(user_query)

    def json_into_general_info(self, json):
        for element in json:
            self.general_info['weight'] = element['weight']
            self.general_info['height'] = element['height']
            self.general_info['sex'] = element['sex']
            self.general_info['marital_status'] = element['marital_status']
            self.general_info['occupation'] = element['occupation']
            self.general_info['religion'] = element['religion']
            self.general_info['scholarship'] = element['scholarship']

    def get_user_contact(self):
        regex_string = r"^\b({})\b$".format(self.user_id)
        custom_regex = re.compile(regex_string, re.IGNORECASE)
        # Change collections
        general_info = MongoLocalDatabase('user_contact').collection
        # Query DB
        user_query = general_info.find({"user_id": custom_regex}, {})
        # Digest JSON answer
        self.json_into_user_contact(user_query)

    def json_into_user_contact(self, json):
        for element in json:
            self.user_contact['current_address'] = element['current_address']
            for phone_number in element['phone_numbers']:
                self.user_contact['phone_numbers'].append(phone_number)
            for emergency_contact in element['emergency_contacts']:
                contact_obj = EmergencyContacts(emergency_contact['name'], emergency_contact['phone'],
                                                emergency_contact['relationship'])
                self.user_contact['emergency_contacts'].append(contact_obj)
