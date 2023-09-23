from collections import UserDict


class SystemsAparatus(UserDict):
    def __init__(self, cardiovascular_system=None, respiratory_system=None, digestive_system=None,
                 nephro_urological_system=None, endocrine_system_and_metabolism=None, hematopoietic_system=None,
                 nervous_system=None, musculoskeletal_system=None, skin_and_integuments=None, sense_organs=None,
                 psychic_sphere=None):
        super().__init__()
        self['cardiovascular_system'] = cardiovascular_system
        self['respiratory_system'] = respiratory_system
        self['digestive_system'] = digestive_system
        self['nephro_urological_system'] = nephro_urological_system
        self['endocrine_system_and_metabolism'] = endocrine_system_and_metabolism
        self['hematopoietic_system'] = hematopoietic_system
        self['nervous_system'] = nervous_system
        self['musculoskeletal_system'] = musculoskeletal_system
        self['skin_and_integuments'] = skin_and_integuments
        self['sense_organs'] = sense_organs
        self['psychic_sphere'] = psychic_sphere
