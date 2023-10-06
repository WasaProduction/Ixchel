from mongodb.connection_handlers.mongo_local_database import MongoLocalDatabase


class GetTextLabels:
    def __init__(self, language=1):
        self.name = ''
        self.language = language
        self.bone_names = MongoLocalDatabase('text_labels').collection
        self.get_bone_names()

    def get_bone_names(self):
        self.json_into_self(self.bone_names.find())

    def json_into_self(self, json):
        for element in json:
            """
                Text used in labels are inside a mongo object called text, then in an array named by label, text is 
                contained in different languages
                0: English
                1: Spanish
            """
            self.agenda_btn = element['text']['agenda_btn'][self.language]
            self.summary_btn = element['text']['summary_btn'][self.language]
            self.diagnosis_btn = element['text']['diagnosis_btn'][self.language]
            self.general_info_lbl = element['text']['general_information_lbl'][self.language]
            self.age_lbl = element['text']['age_lbl'][self.language]
            self.weight_lbl = element['text']['weight_lbl'][self.language]
            self.height_lbl = element['text']['height_lbl'][self.language]
            self.hereditary_lbl = element['text']['hereditary_lbl'][self.language]
            self.pathologic_lbl = element['text']['pathologic_lbl'][self.language]
            self.immunizations_lbl = element['text']['immunizations_lbl'][self.language]
            self.allergies_lbl = element['text']['allergies_lbl'][self.language]
            self.no_data_lbl = element['text']['no_data_lbl'][self.language]
