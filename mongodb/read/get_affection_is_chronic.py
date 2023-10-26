from mongodb.connection_handlers.mongo_local_database import MongoLocalDatabase
from data_models.model_affections import ModelAffection
import re


class GetAffectionIsChronic(ModelAffection):
    def __init__(self, cie_id=''):
        super().__init__()
        self.cie_id = cie_id
        self.users = MongoLocalDatabase('afecciones').collection
        self.get_affection()

    def get_affection(self):
        regex_string = r"^\b({})\b$".format(self.cie_id)
        custom_regex = re.compile(regex_string, re.IGNORECASE)
        # Query DB
        user_query = self.users.find({"id_cie": custom_regex}, {})
        # Digest JSON answer
        self.json_into_self(user_query)

    def json_into_self(self, json):
        for element in json:
            self.name = element['name']
            self.description = element['description']
            self.coding_note = element['coding_note']
            self.inclusions = element['inclusions']
            self.exclusions = element['exclusions']
            self.encoded_elsewhere = element['encoded_elsewhere']
            self.organ = element['organ']
            self.bone = element['bone']
            self.chronic = element['chronic']
