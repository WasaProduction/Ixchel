class Drug:
    def __init__(self, object_id=None, name=None, dose=None, dose_unit=None, package=None, form=None, salts=None,
                 disbled=False):
        self.object_id = object_id
        self.name = name
        self.dose = dose
        self.dose_unit = dose_unit
        self.package = package
        self.form = form
        self.salts = salts
        self.disbled = disbled
