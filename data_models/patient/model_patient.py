class ModelPatient:
    def __init__(self, object_id='', user_id='', username='', name='', lastname_1='', lastname_2='',
                 diagnosis_entries=None):
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

    """             Getters/Setters             """
    @property
    def object_id(self):
        return self._object_id

    @object_id.setter
    def object_id(self, value):
        self._object_id = value

    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        self._username = value

    @property
    def lastname_1(self):
        return self._lastname_1

    @lastname_1.setter
    def lastname_1(self, value):
        self._lastname_1 = value

    @property
    def lastname_2(self):
        return self._lastname_2

    @lastname_2.setter
    def lastname_2(self, value):
        self._lastname_2 = value

    @property
    def diagnosis_entries(self):
        return self._diagnosis_entries

    @diagnosis_entries.setter
    def diagnosis_entries(self, value):
        self._diagnosis_entries = value
