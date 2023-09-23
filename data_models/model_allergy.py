class ModelAllergy:
    def __init__(self, allergen='', category=0, severity=0):
        self.allergen = allergen
        self.category = category
        self.severity = severity

    """             Getters/Setters             """

    @property
    def allergen(self):
        return self._allergen

    @allergen.setter
    def allergen(self, value):
        self._allergen = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        self._category = value

    @property
    def severity(self):
        return self._severity

    @severity.setter
    def severity(self, value):
        self._severity = value
