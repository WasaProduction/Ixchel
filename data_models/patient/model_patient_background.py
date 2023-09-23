class PatientBackground:
    def __init__(self, used_id=None, weight=None, height=None, sex=None, marital_status=None, occupation=None,
                 religion=None, scholarship=None, current_address=None, phone=None):
        self.used_id = used_id
        self.my_dict = {'weight': weight, 'height': height, 'sex': sex, 'marital_status': marital_status,
                        'occupation': occupation, 'religion': religion, 'scholarship': scholarship,
                        'current_address': current_address, 'phone': phone}
