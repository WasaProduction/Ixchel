from mongodb.connection_handlers.mongo_local_database import MongoLocalDatabase
from data_models.agenda_entry import AgendaEntry
import re


class GetAgendaEntries:
    def __init__(self, medic=None):
        self.medic = medic
        self.collection = MongoLocalDatabase('agenda').collection
        #   Array of agenda entries.
        self.agenda = []

    def get_agenda(self):
        #   Empty agenda
        self.agenda = []
        regex_string = r"{}*".format(self.medic)
        custom_regex = re.compile(regex_string, re.IGNORECASE)
        # Query DB.
        user_query = self.collection.find({"id_medic": custom_regex}, {})
        # Digest JSON answer.
        self.digest_json(user_query)
        return self.agenda

    def digest_json(self, json):
        #   JSON into data model.
        for element in json:
            entry = AgendaEntry()
            #   datetime()
            entry['end'] = element['end']
            #   datetime()
            entry['start'] = element['start']
            #   str()
            entry['location'] = element['location']
            #   int()
            entry['status'] = element['status']
            #   str()
            entry['id_attendee'] = element['id_attendee']
            #   str()
            entry['id_medic'] = element['id_medic']
            #   str()
            entry['id_organizer'] = element['id_organizer']
            self.agenda.append(entry)

