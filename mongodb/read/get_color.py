from mongodb.connection_handlers.mongo_local_database import MongoLocalDatabase
import re


class GetColor:
    def __init__(self, cie_id=None):
        self.cie_id = cie_id
        self.color = ''
        self.colors_dict = {}
        self.collection = MongoLocalDatabase('chapter_colors').collection

    def get_color(self):
        regex_string = r"{}*".format(self.cie_id[:2])
        custom_regex = re.compile(regex_string, re.IGNORECASE)
        # Query DB
        user_query = self.collection.find({"id_cie": custom_regex}, {})
        # Digest JSON answer
        self.digest_json(user_query)
        return self.color

    def get_colors_dict(self):
        self.digest_json(self.collection.find())
        return self.colors_dict

    def digest_json(self, json):
        for element in json:
            self.color = element['hex_color']
            self.colors_dict[element['id_cie'][:1]] = element['hex_color']

