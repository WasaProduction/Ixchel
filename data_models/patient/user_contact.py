from collections import defaultdict


class UserContact(defaultdict):
    def __init__(self, current_address=None, phone_numbers=None, mail=None, emergency_contacts=None):
        super().__init__()
        self['current_address'] = current_address
        if phone_numbers is not None:
            self['phone_numbers'] = phone_numbers
        else:
            self['phone_numbers'] = []
        self[mail] = mail
        if emergency_contacts is None:
            self['emergency_contacts'] = []
        else:
            self['emergency_contacts'] = emergency_contacts
