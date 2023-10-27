class GeneralInfo(dict):
    def __init__(self, used_id=None, weight=None, height=None, sex=None, marital_status=None, occupation=None,
                 religion=None, scholarship=None):
        super().__init__()
        self.used_id = used_id
        self['weight'] = weight
        self['height'] = height
        self['sex'] = sex
        self['marital_status'] = marital_status
        self['occupation'] = occupation
        self['religion'] = religion
        self['scholarship'] = scholarship

    def restore_model(self):
        self.used_id = None
        self['weight'] = None
        self['height'] = None
        self['sex'] = None
        self['marital_status'] = None
        self['occupation'] = None
        self['religion'] = None
        self['scholarship'] = None
