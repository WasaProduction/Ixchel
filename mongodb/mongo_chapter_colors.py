from data_models.model_chapter_colors import ModelChapterColors
from mongodb.connection_handlers.mongo_local_database import MongoLocalDatabase


class MongoChapterColors:
    def __init__(self):
        self.chapter_colors_obj_array = []
        self.json_into_data_model(MongoLocalDatabase('chapter_colors').collection.find())

    def json_into_data_model(self, json):
        for element in json:
            dummy_item = ModelChapterColors(element['_id'], element['id_cie'], element['name'],
                                            element['hex_color'])
            dummy_item.update_object_color()
            self.chapter_colors_obj_array.append(dummy_item)
            del dummy_item

    """             Getters/Setters             """

    @property
    def chapter_colors_obj_array(self):
        return self._chapter_colors_obj_array

    @chapter_colors_obj_array.setter
    def chapter_colors_obj_array(self, value):
        self._chapter_colors_obj_array = value
