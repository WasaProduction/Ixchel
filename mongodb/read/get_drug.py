from data_models.model_drug import Drug
from mongodb.connection_handlers.mongo_local_database import MongoLocalDatabase
import re


class GetDrug:
    def __init__(self):
        self.local_affections = MongoLocalDatabase('drugs').collection
        self.drugs_dictionary = []
        self.words = []
