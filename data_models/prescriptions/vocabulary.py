class Vocabulary:
    def __init__(self, actions=None, dose_units=None, dosage_units=None, duration_units=None, prepositions=None,
                 indication_use=None):
        if actions is None:
            self.actions = []
        else:
            self.actions = actions
        if dose_units is None:
            self.dose_units = []
        else:
            self.dose_units = dose_units
        if dosage_units is None:
            self.dosage_units = []
        else:
            self.dosage_units = dosage_units
        if duration_units is None:
            self.duration_units = []
        else:
            self.duration_units = duration_units
        if prepositions is None:
            self.duration_units = []
        else:
            self.prepositions = prepositions
        if indication_use is None:
            self.indication_use = []
        else:
            self.indication_use = indication_use
