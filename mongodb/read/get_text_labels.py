from mongodb.connection_handlers.mongo_local_database import MongoLocalDatabase
from data_models.multilingual_obj import MultilingualOBJ


class GetTextLabels(MultilingualOBJ):
    def __init__(self, language=1):
        super().__init__()
        #   Integer used for language selection.
        self.language = language
        self.text_contents = MongoLocalDatabase('text_labels').collection
        #   Query db
        self.get_text()

    def get_text(self):
        self.digest_json(self.text_contents.find())

    def digest_json(self, json):
        for element in json:
            """
                Text used in labels are inside a mongo object called text, then in an array named by label, text is 
                contained in different languages
                0: English
                1: Spanish
            """
            self.agenda_btn = element['agenda_btn'][self.language]
            self.summary_btn = element['summary_btn'][self.language]
            self.diagnosis_btn = element['diagnosis_btn'][self.language]
            self.general_info_lbl = element['general_information_lbl'][self.language]
            self.age_lbl = element['age_lbl'][self.language]
            self.weight_lbl = element['weight_lbl'][self.language]
            self.height_lbl = element['height_lbl'][self.language]
            self.hereditary_lbl = element['hereditary_lbl'][self.language]
            self.pathologic_lbl = element['pathologic_lbl'][self.language]
            self.immunizations_lbl = element['immunizations_lbl'][self.language]
            self.allergies_lbl = element['allergies_lbl'][self.language]
            self.no_data_lbl = element['no_data_lbl'][self.language]
            self.pulse = element['pulse'][self.language]
            self.temperature = element['temperature'][self.language]
            self.pressure = element['pressure'][self.language]
            self.heart_rate = element['heart_rate'][self.language]
            self.respiratory_rate = element['respiratory_rate'][self.language]
            self.o2_saturation = element['o2_saturation'][self.language]
            self.interrogatory = element['interrogatory'][self.language]
            self.examination = element['examination'][self.language]
            self.diagnosis = element['diagnosis'][self.language]
            self.diagnosis_prescription = element['diagnosis_prescription'][self.language]
            self.prescription = element['prescription'][self.language]
            self.habitus = element['habitus'][self.language]
            self.history_log = element['history_log'][self.language]
            self.id_card = element['id_card'][self.language]
            self.hereditary_background = element['hereditary_background'][self.language]
            self.pathologic_background = element['pathologic_background'][self.language]
            self.non_path_background = element['non_path_background'][self.language]
            self.physical_examination = element['physical_examination'][self.language]
            self.interrogatory = element['interrogatory'][self.language]
            self.notifications = element['notifications'][self.language]
            self.user = element['user'][self.language]
            self.config = element['config'][self.language]
            self.search = element['search'][self.language]
            self.add = element['add'][self.language]
            self.date = element['date'][self.language]
            self.start = element['start'][self.language]
            self.end = element['end'][self.language]
            self.new_appointment = element['new_appointment'][self.language]
            self.no_appointment_past = element['no_appointment_past'][self.language]
            self.appointment_overlap = element['appointment_overlap'][self.language]
            self.save_changes = element['save_changes'][self.language]
            # self. = element[''][self.language]
