class ModelDiagnosis:
    def __init__(self, diagnosis_id='', created_by='', patient_id=None, diagnosis=None,
                 tags_contained=None, creation_date=None):
        self.diagnosis_id = diagnosis_id
        self.creation_date = creation_date
        self.created_by = created_by
        self.patient_id = patient_id
        self.diagnosis = diagnosis
        self.tags_contained = tags_contained

    """             Getters/Setters             """
    @property
    def diagnosis_id(self):
        return self._diagnosis_id

    @diagnosis_id.setter
    def diagnosis_id(self, value):
        self._diagnosis_id = value

    @property
    def creation_date(self):
        return self._creation_date

    @creation_date.setter
    def creation_date(self, value):
        self._creation_date = value

    @property
    def created_by(self):
        return self._created_by

    @created_by.setter
    def created_by(self, value):
        self._created_by = value

    @property
    def patient_id(self):
        return self._patient_id

    @patient_id.setter
    def patient_id(self, value):
        self._patient_id = value

    @property
    def diagnosis(self):
        return self._diagnosis

    @diagnosis.setter
    def diagnosis(self, value):
        self._diagnosis = value

    @property
    def tags_contained(self):
        return self._tags_contained

    @tags_contained.setter
    def tags_contained(self, value):
        self._tags_contained = value
