from collections import defaultdict


class GeneralInfo(defaultdict):
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
