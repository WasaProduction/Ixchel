class ModelPatientImmutable:
    def __init__(self, object_id='', user_id='', birthday=None, date_of_death=None, birthplace=None, blood_type='',
                 biological_sex=''):
        self.object_id = object_id
        self.user_id = user_id
        self.birthday = birthday
        self.date_of_death = date_of_death
        self.birthplace = birthplace
        self.blood_type = blood_type
        self.biological_sex = biological_sex
