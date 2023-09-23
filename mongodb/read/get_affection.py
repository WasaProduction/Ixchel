from mongodb.connection_handlers.mongo_local_database import MongoLocalDatabase
import re


class GetAffection:
    def __init__(self, cie_id=''):
        self.name = ''
        self.cie_id = cie_id
        self.users = MongoLocalDatabase('afecciones').collection

    def get_affection(self):
        regex_string = r"^\b({})\b$".format(self.cie_id)
        custom_regex = re.compile(regex_string, re.IGNORECASE)
        # Query DB
        user_query = self.users.find({"id_cie": custom_regex}, {})
        # Digest JSON answer
        self.json_into_self(user_query)
        return self.name

    def json_into_self(self, json):
        for element in json:
            self.name = element['nombre']
