from mongodb.connection_handlers.mongo_local_database import MongoLocalDatabase
from PyQt6.QtGui import QColor


class GetBoneColors:
    def __init__(self):
        self.colors_arr = []
        self.collection = MongoLocalDatabase('bone_colors').collection
        self.get_colors_arr()

    def get_color(self, case=None):
        if case is None:
            return None
        else:
            return self.colors_arr[case]

    def get_colors_arr(self):
        self.digest_json(self.collection.find())

    def digest_json(self, json):
        retrieved_arr = []
        for element in json:
            retrieved_arr = element['colors']
        self.colors_arr = ['#' + color for color in retrieved_arr]
        self.colors_arr = [QColor(color) for color in self.colors_arr]
