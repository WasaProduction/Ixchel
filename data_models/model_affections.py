class ModelAffection:
    def __init__(self, object_id='', id_cie='', name='', description=None, coding_note=None, inclusions=None,
                 exclusions=None, encoded_elsewhere=None, organ=None, bone=None, chronic=False):
        self.object_id = object_id
        self.id_cie = id_cie
        self.name = name
        self.description = description
        self.coding_note = coding_note
        self.inclusions = inclusions
        self.exclusions = exclusions
        self.encoded_elsewhere = encoded_elsewhere
        self.organ = [] if organ is None else organ
        self.bone = [] if bone is None else bone
        self.chronic = chronic

    """             Getters/Setters             """
    @property
    def object_id(self):
        return self._object_id

    @object_id.setter
    def object_id(self, value):
        self._object_id = value

    @property
    def id_cie(self):
        return self._id_cie

    @id_cie.setter
    def id_cie(self, value):
        self._id_cie = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value

    @property
    def coding_note(self):
        return self._coding_note

    @coding_note.setter
    def coding_note(self, value):
        self._coding_note = value

    @property
    def inclusions(self):
        return self._inclusions

    @inclusions.setter
    def inclusions(self, value):
        self._inclusions = value

    @property
    def exclusions(self):
        return self._exclusions

    @exclusions.setter
    def exclusions(self, value):
        self._exclusions = value

    @property
    def coded_elsewhere(self):
        return self._coded_elsewhere

    @coded_elsewhere.setter
    def coded_elsewhere(self, value):
        self._coded_elsewhere = value
