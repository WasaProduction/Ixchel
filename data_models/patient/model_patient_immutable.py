class ModelPatientImmutable:
    def __init__(self, object_id='', user_id='', birthday=None, birthplace=None, blood_type='', biological_sex=''):
        self.object_id = object_id
        self.user_id = user_id
        self.birthday = birthday
        self.birthplace = birthplace
        self.blood_type = blood_type
        self.biological_sex = biological_sex

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
    def birthday(self):
        return self._birthday

    @birthday.setter
    def birthday(self, value):
        self._birthday = value

    @property
    def birthplace(self):
        return self._birthplace

    @birthplace.setter
    def birthplace(self, value):
        self._birthplace = value

    @property
    def blood_type(self):
        return self._blood_type

    @blood_type.setter
    def blood_type(self, value):
        self._blood_type = value

    @property
    def biological_sex(self):
        return self._biological_sex

    @biological_sex.setter
    def biological_sex(self, value):
        self._biological_sex = value
