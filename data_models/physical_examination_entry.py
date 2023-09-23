from collections import defaultdict


class PhysicalExaminationEntry(defaultdict):
    def __init__(self, created_by=None, patient_id=None, creation_date=None, related_note=None, content=None):
        super().__init__()
        self['created_by'] = created_by
        self['patient_id'] = patient_id
        self['creation_date'] = creation_date
        self['related_note'] = related_note
        self['content'] = content
