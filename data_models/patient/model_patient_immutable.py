import datetime


class ModelPatientImmutable:
    def __init__(self, object_id='', user_id='', birthday=None, date_of_death=None, birthplace='Kamino', blood_type='O+'
                 , biological_sex='M'):
        self.object_id = object_id
        self.user_id = user_id
        self.birthday = datetime.datetime.now() if birthday is None else birthday
        self.date_of_death = date_of_death
        self.birthplace = birthplace
        self.blood_type = blood_type
        self.biological_sex = biological_sex
