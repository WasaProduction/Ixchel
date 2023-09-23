from collections import defaultdict


class ModelTreatment:
    def __init__(self, object_id=None, patient_id=None, medic_id=None, drug=None, instruction=None):
        self.object_id = object_id
        self.patient_id = patient_id
        self.medic_id = medic_id
        self.drug = drug
        self.instruction = instruction if instruction is not None else Instruction()


class Instruction(defaultdict):
    def __init__(self, instruction_type=None, raw_text=None, instruction=None, drug=None, action=None, quantity=None,
                 periodicity=None, duration=None, indication_of_use=None, complement=None):
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
        # Periodicity()
        self['periodicity'] = periodicity if periodicity is not None else Periodicity()
        # Duration()
        self['duration'] = duration if duration is not None else Duration()
        # Indications of use
        self['indication_of_use'] = indication_of_use if indication_of_use is not None else IndicationsOfUse()
        # Complement
        self['complement'] = complement


class Quantity(defaultdict):
    def __init__(self, quantity=None, unit=None):
        super().__init__()
        self['quantity'] = quantity
        self['unit'] = unit


class Periodicity(defaultdict):
    def __init__(self, quantity=None, unit=None):
        super().__init__()
        self['quantity'] = quantity
        self['unit'] = unit


class Duration(defaultdict):
    def __init__(self, quantity=None, unit=None):
        super().__init__()
        self['quantity'] = quantity
        self['unit'] = unit


class IndicationsOfUse(defaultdict):
    def __init__(self, condition=None, act=None):
        super().__init__()
        self.condition = condition
        self.act = act
