from pymongo import MongoClient
import re
from data_models.model_affections import ModelAffection

MONGO_URI = 'mongodb://localhost'
local_client = MongoClient(MONGO_URI)
db = local_client['Ixchel']
local_affections = db['afecciones']

custom_regex = re.compile(r"^(?=.*\bEscherichia\b).*^(?=.*\bcoli\b).*$", re.IGNORECASE)
affection_query = local_affections.find({"nombre": custom_regex}, {})

affections_dictionary = []
for element in affection_query:
    print(element)
    dummy_item = ModelAffection()
    dummy_item.object_id = element['_id']
    dummy_item.id_cie = element['id_cie']
    dummy_item.name = element['nombre']
    dummy_item.description = element['description']
    dummy_item.nota_sobre_codificacion = element['nota_sobre_la_codificacion']
    dummy_item.inclusiones = element['inclusiones']
    dummy_item.exclusiones = element['exclusiones']
    dummy_item.codificado_otra_parte = element['codificado_en_otra_parte']
    affections_dictionary.append(dummy_item)
    del dummy_item

for cosa in affections_dictionary:
    print(cosa.name)
    print("---------")