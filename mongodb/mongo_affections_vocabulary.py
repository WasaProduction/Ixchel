from data_models.model_affections import ModelAffection
from mongodb.connection_handlers.mongo_local_database import MongoLocalDatabase
import re


class MongoAffectionsVocabulary:
    def __init__(self):
        self.local_affections = MongoLocalDatabase('afecciones').collection
        self.affections_dictionary = []
        self.words = []

    def set_words(self, first_value, second_value=None, third_value=None):
        self.words = []
        self.words.append(first_value)
        if second_value is not None:
            self.words.append(second_value)
            if third_value is not None:
                self.words.append(third_value)

    def get_affections_dictionary(self):
        self.retrieve_affections_dictionary()
        return self.affections_dictionary

    def get_affections_possibility(self):
        self.retrieve_affection_possibility()
        return self.affections_dictionary

    def reset_affections_dictionary(self):
        self.affections_dictionary = []

    # Look for known word
    def retrieve_affections_dictionary(self):
        regex_string = "^"
        if len(self.words) != 1:
            for index, word in enumerate(self.words):
                regex_string += r"(?=.*\b{}\b)".format(word)
                if index != len(self.words) - 1:
                    regex_string += r".*^"
                else:
                    regex_string += r".*$"
        else:
            regex_string = r"^(?=.*\b{}\b).*$".format(self.words[0])

        custom_regex = re.compile(regex_string, re.IGNORECASE)
        del regex_string
        # Querying mongo
        affection_query = self.local_affections.find({"name": custom_regex}, {})
        del custom_regex
        # get the JSON into model_affections
        self.json_into_data_model(affection_query)
        del affection_query

    def retrieve_affection_possibility(self):
        # Looks for substring inside a string
        regex_string = r"^.*{}.*$".format(self.words[0])
        custom_regex = re.compile(regex_string, re.IGNORECASE)
        del regex_string
        # Querying mongo
        affection_query = self.local_affections.find({"name": custom_regex}, {})
        del custom_regex
        # Get the JSON into model_affections
        self.json_into_data_model(affection_query)
        del affection_query

    def retrieve_affection_code(self):
        # r"^(?=.*\b({})\b).*$"
        regex_string = r"^\b({})\b$".format(self.words[0])
        custom_regex = re.compile(regex_string, re.IGNORECASE)
        del regex_string
        # Querying mongo
        affection_query = self.local_affections.find({"name": custom_regex}, {})
        del custom_regex
        # get the JSON into model_affections
        self.json_into_data_model(affection_query)
        del affection_query

    # Transform retrieved JSON into an object of AffectionDataModel type
    def json_into_data_model(self, json):
        for i, element in enumerate(json):
            dummy_item = ModelAffection(element['_id'], element['id_cie'], element['name'],
                                        element['description'], element['coding_note'],
                                        element['inclusions'], element['exclusions'],
                                        element['encoded_elsewhere'], element['organ'], element['bone'],
                                        element['chronic'])
            self.affections_dictionary.append(dummy_item)
            del dummy_item
