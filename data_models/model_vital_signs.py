from collections import UserDict
"""
For vital signs
"""


class ModelVitalSigns(UserDict):
    def __init__(self, pulse=None, temperature=None, blood_pressure=None, heart_rate=None, respiratory_rate=None,
                 peripheral_oxygen_saturation=None):
        super().__init__()
        self['pulse'] = pulse
        self['temperature'] = temperature
        self['blood_pressure'] = blood_pressure
        self['heart_rate'] = heart_rate
        self['respiratory_rate'] = respiratory_rate
        self['peripheral_oxygen_saturation'] = peripheral_oxygen_saturation
