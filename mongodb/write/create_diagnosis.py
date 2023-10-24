from mongodb.mongo_affections_vocabulary import MongoAffectionsVocabulary
from JSON.write.json_diagnosis import JsonDiagnosis
from data_models.model_diagnosis import ModelDiagnosis
from datetime import datetime


class CreateDiagnosis:
    def __init__(self, text):
        contained_tags_array = []
        # Check for tags
        if len(text.strip()) > 3:
            mongodb_affections = MongoAffectionsVocabulary()
            text_array = text.split(' ')
            # Get all tags
            for word in text_array:
                mongodb_affections.reset_affections_dictionary()
                mongodb_affections.set_words(word)
                mongodb_affections.retrieve_affection_code()
                dummy = mongodb_affections.get_affections_dictionary()
                if len(dummy) != 0:
                    contained_tags_array.append(dummy[0].id_cie)
        else:
            # No tags contained
            contained_tags_array = None

        content_obj = ModelDiagnosis(diagnosis_id='test_id', patient_id='patient_id', diagnosis=text, created_by='dr_id'
                                     , tags_contained=contained_tags_array,
                                     creation_date=datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))
        # Pass file contents
        insertion_obj = JsonDiagnosis(content_obj)
        # Insert into db
        insertion_obj.insert_into_db()
