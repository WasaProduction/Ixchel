from mongodb.connection_handlers.mongo_local_database import MongoLocalDatabase
from data_models.agenda_entry import AgendaEntry
from datetime import datetime


class WriteAgendaEntries:
    def __init__(self, entry=None, sent_by=None):
        now = datetime.now()
        custom = now.strftime("%m/%d/%Y")
        self.EntryModel = AgendaEntry()
        #   Check if date is available
        #   Check
        """     Db      """
        #   Try to establish connection
        try:
            self.db = MongoLocalDatabase('agenda')
        except:
            print("Upgrade exception at write_json_diagnosis")
        #
        self.db.insert_into_collection(self.EntryModel)

    #   Transform model into JSON
    def model_into_json(self):
        # Obj into dictionary
        dictionary = {
            "start": self.EntryModel['start'],
            "end": self.EntryModel['end'],
            "location": self.EntryModel['location'],
            "id_attendee": self.EntryModel['id_attendee'],
            "id_medic": self.EntryModel['id_medic'],
            "id_organizer": self.EntryModel['id_organizer'],
            "status": self.EntryModel['status']
        }
        return dictionary

    def insert_into_db(self):
        self.db.insert_into_collection(self.model_into_json())

