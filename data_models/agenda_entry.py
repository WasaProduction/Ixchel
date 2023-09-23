from collections import UserDict
from datetime import datetime


class AgendaEntry(UserDict):
    def __init__(self, start=None, end=None, location=None, id_attendee=None, id_medic=None, id_organizer=None,
                 status=None):
        super().__init__()
        self['start'] = start if start is not None else datetime.today()
        self['end'] = end if end is not None else datetime.today()
        self['location'] = location if location is not None else '0'
        self['id_attendee'] = id_attendee if id_attendee is not None else '0'
        self['id_medic'] = id_medic if id_medic is not None else '0'
        self['id_organizer'] = id_organizer if id_organizer is not None else '0'
        self['status'] = status


class Holiday(UserDict):
    def __init__(self, name=None, date=None, annual=False, description=None):
        super().__init__()
        self['name'] = name if name is not None else 'Holiday'
        self['date'] = date if date is not None else datetime.today()
        #   If true ignore year
        self['annual'] = annual
        self['description'] = description if description is not None else 'Holiday description'
