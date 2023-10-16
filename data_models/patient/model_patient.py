from data_models.patient.model_patient_immutable import ModelPatientImmutable
from data_models.patient.general_info import GeneralInfo
from data_models.patient.user_contact import UserContact


class ModelPatient:
    def __init__(self, object_id='', user_id='', username='', name='', lastname_1='', lastname_2='',
                 diagnosis_entries=None, immutables=None, general_info=None, user_contact=None):
        self.object_id = object_id
        self.user_id = user_id
        self.username = username
        self.name = name
        self.lastname_1 = lastname_1
        self.lastname_2 = lastname_2
        if diagnosis_entries is None:
            self.diagnosis_entries = []
        else:
            self.diagnosis_entries = diagnosis_entries
        if immutables is None:
            self.immutables = ModelPatientImmutable()
        else:
            self.immutables = diagnosis_entries
        if general_info is None:
            self.general_info = GeneralInfo()
        else:
            self.general_info = general_info
        if user_contact is None:
            self.user_contact = UserContact()
        else:
            self.user_contact = user_contact



