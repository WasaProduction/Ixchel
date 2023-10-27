from mongodb.connection_handlers.mongo_local_database import MongoLocalDatabase
from data_models.model_allergy import ModelAllergy
import re


class GetAllergies(list):
    def __init__(self, user_id=''):
        super().__init__()
        self.name = ''
        self.user_id = user_id
        self.users = MongoLocalDatabase('user_allergies').collection
        self.get_affection()

    def get_affection(self):
        regex_string = r"^\b({})\b$".format(self.user_id)
        custom_regex = re.compile(regex_string, re.IGNORECASE)
        # Query DB
        user_query = self.users.find({"user_id": custom_regex}, {})
        # Digest JSON answer
        self.json_into_self(user_query)
        return self.name

    def json_into_self(self, json):
        for element in json:
            for allergy in element['allergies']:
                allergy_obj = ModelAllergy()
                self.append(ModelAllergy(allergy['allergen'], allergy['category'], allergy['severity']))
