from mongodb.connection_handlers.mongo_local_database import MongoLocalDatabase
from data_models.agenda_entry import Holiday


class GetHolidays(list):
    def __init__(self):
        super().__init__()
        self.collection = MongoLocalDatabase('holidays').collection
        self.get_holidays_dict()

    def get_holidays_dict(self):
        self.digest_json(self.collection.find())

    def digest_json(self, json):
        for element in json:
            holiday = Holiday()
            holiday['name'] = element['name']
            holiday['description'] = element['description']
            holiday['date'] = element['date']
            holiday['annual'] = element['annual']
            self.append(holiday)
