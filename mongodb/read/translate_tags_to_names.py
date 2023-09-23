from data_models.model_tag import ModelTag
from mongodb.connection_handlers.mongo_local_database import MongoLocalDatabase
from mongodb.mongo_chapter_colors import MongoChapterColors
import re


class TranslateTagsNames:
    def __init__(self, cie_id='', diagnosis_id='', creation_date=None):
        self.name = ''
        self.color = ''
        self.cie_id = cie_id
        self.diagnosis_id = diagnosis_id
        self.creation_date = creation_date
        self.users = MongoLocalDatabase('afecciones').collection
        self.colors = MongoChapterColors().chapter_colors_obj_array
        self.get_affection()
        #print('name:', self.name, 'color:', self.color, self.cie_id, self.diagnosis_id)

    def get_tag(self):
        return ModelTag(cie_id=self.cie_id, diagnosis_id=self.diagnosis_id, creation_date=self.creation_date,
                        name=self.name, color=self.color, severity='')

    def get_affection(self):
        regex_string = r"^\b({})\b$".format(self.cie_id)
        custom_regex = re.compile(regex_string, re.IGNORECASE)
        # Query DB
        user_query = self.users.find({"id_cie": custom_regex}, {})
        # Digest JSON answer
        self.json_into_self(user_query)

    def json_into_self(self, json):
        for element in json:
            self.name = element['nombre']
            for color in self.colors:
                if color.id_cie[:2] == self.cie_id[:2]:
                    self.color = color.object_color_code
