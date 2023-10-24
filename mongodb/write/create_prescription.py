from JSON.write.json_treatment import JsonTreatment


class CreatePrescription:
    def __init__(self, prescription):
        content_obj = prescription
        #   creation_date=datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))
        # Pass file contents
        insertion_obj = JsonTreatment(content_obj)
        # Insert into db
        insertion_obj.insert_into_db()
