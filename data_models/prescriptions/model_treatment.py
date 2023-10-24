from datetime import datetime


class ModelTreatment:
    def __init__(self, creation_date=None, treatment_id=None, patient_id=None, medic_id=None, instructions=None,
                 active=None, raw_text=None):
        self.creation_date = datetime.now() if creation_date is None else creation_date
        self.treatment_id = treatment_id
        self.patient_id = patient_id
        self.medic_id = medic_id
        self.instructions = [] if instructions is None else instructions
        #   Depends on the sum of its instructions.
        self.active = active if active is not None else True
        self.raw_text = raw_text


class Instruction(dict):
    def __init__(self, instruction_type=None, raw_text=None, instruction=None, drug=None, action=None, quantity=None,
                 periodicity=None, duration=None, indication_of_use=None, complement=None, start_date=None,
                 to_deactivate=None, active=False):
        super().__init__()
        #   Instruction type
        self['instruction_type'] = instruction_type
        #   Instruction
        self['instruction'] = instruction
        #   Raw text
        self['raw_text'] = raw_text
        #   Drug
        self['drug'] = drug
        #   Action
        self['action'] = action
        #   Quantity
        self['quantity'] = quantity if quantity is not None else Quantity()
        #   Periodicity()
        self['periodicity'] = periodicity if periodicity is not None else Periodicity()
        #   Duration()
        self['duration'] = duration if duration is not None else Duration()
        #   Indications of use.
        self['indication_of_use'] = indication_of_use if indication_of_use is not None else IndicationsOfUse()
        #   Complement.
        self['complement'] = complement
        #   Start date.
        self['start_date'] = start_date
        #   Foreseen end date.
        self['to_deactivate'] = to_deactivate
        #   Active.
        self['active'] = active


class Quantity(dict):
    def __init__(self, quantity=None, unit=None):
        super().__init__()
        self['quantity'] = quantity
        self['unit'] = unit


class Periodicity(dict):
    def __init__(self, quantity=None, unit=None):
        super().__init__()
        self['quantity'] = quantity
        self['unit'] = unit


class Duration(dict):
    def __init__(self, quantity=None, unit=None):
        super().__init__()
        self['quantity'] = quantity
        self['unit'] = unit


class IndicationsOfUse(dict):
    def __init__(self, condition=None, act=None):
        super().__init__()
        self['condition'] = condition
        self['act'] = act
