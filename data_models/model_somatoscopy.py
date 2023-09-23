"""
Classes:
    ModelSomatoscopy
"""


class ModelSomatoscopy:
    def __init__(self, object_id='', patient_id='', patient_condition=None, apparent_age=None, attitude=None,
                 fascies=None, movement=None, abnormal_movement=None, consciousness=None, voice=None,
                 personal_grooming=None, clothing=None, smell=None, model_habitus=None):
        self.object_id = object_id
        self.patient_id = patient_id
        self.patient_condition = patient_condition
        self.apparent_age = apparent_age
        self.attitude = attitude
        self.fascies = fascies
        self.movement = movement
        self.abnormal_movement = abnormal_movement
        self.consciousness = consciousness
        self.voice = voice
        self.personal_grooming = personal_grooming
        self.clothing = clothing
        self.smell = smell
        self.model_habitus = model_habitus

    """             Getters/Setters             """
    @property
    def object_id(self):
        return self._object_id

    @object_id.setter
    def object_id(self, value):
        self._object_id = value

    @property
    def patient_id(self):
        return self._patient_id

    @patient_id.setter
    def patient_id(self, value):
        self._patient_id = value

    @property
    def patient_condition(self):
        return self._patient_condition

    @patient_condition.setter
    def patient_condition(self, value):
        self._patient_condition = value

    @property
    def apparent_age(self):
        return self._apparent_age

    @apparent_age.setter
    def apparent_age(self, value):
        self._apparent_age = value

    @property
    def attitude(self):
        return self._attitude

    @attitude.setter
    def attitude(self, value):
        self._attitude = value

    @property
    def movement(self):
        return self._movement

    @movement.setter
    def movement(self, value):
        self._movement = value

    @property
    def abnormal_movement(self):
        return self._abnormal_movement

    @abnormal_movement.setter
    def abnormal_movement(self, value):
        self._abnormal_movement = value

    @property
    def consciousness(self):
        return self._consciousness

    @consciousness.setter
    def consciousness(self, value):
        self._consciousness = value

    @property
    def voice(self):
        return self._voice

    @voice.setter
    def voice(self, value):
        self._voice = value

    @property
    def personal_grooming(self):
        return self._personal_grooming

    @personal_grooming.setter
    def personal_grooming(self, value):
        self._personal_grooming = value

    @property
    def clothing(self):
        return self._clothing

    @clothing.setter
    def clothing(self, value):
        self._clothing = value

    @property
    def smell(self):
        return self._smell

    @smell.setter
    def smell(self, value):
        self._smell = value
