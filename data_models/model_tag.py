class ModelTag:
    def __init__(self, cie_id='', diagnosis_id='', creation_date=None, name='', color='', severity=''):
        self.cie_id = cie_id
        self.diagnosis_id = diagnosis_id
        self.creation_date = creation_date
        self.name = name
        self.color = color
        self.severity = severity

    """             Getters/Setters             """
    @property
    def cie_id(self):
        return self._cie_id

    @cie_id.setter
    def cie_id(self, value):
        self._cie_id = value

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
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        self._color = value

    @property
    def severity(self):
        return self._severity

    @severity.setter
    def severity(self, value):
        self._severity = value
