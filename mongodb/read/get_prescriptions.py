from mongodb.connection_handlers.mongo_local_database import MongoLocalDatabase
from data_models.prescriptions.model_treatment import ModelTreatment, Instruction, Quantity, Periodicity, Duration


class GetPrescriptions(list):
    def __init__(self):
        super().__init__()
        self.collection = MongoLocalDatabase('prescriptions').collection
        self.get_prescriptions()

    def get_prescriptions(self):
        self.digest_json(self.collection.find())

    def digest_json(self, json):
        for index, element in enumerate(json):
            prescription = ModelTreatment()
            prescription.creation_date = element['creation_date']
            prescription.treatment_id = element['treatment_id']
            prescription.patient_id = element['patient_id']
            prescription.medic_id = element['medic_id']
            if element['instructions']:
                prescription_instructions = []
                for instruction in element['instructions']:
                    #   Instruction object.
                    instruction_obj = Instruction()
                    instruction_obj['instruction_type'] = instruction['instruction_type']
                    instruction_obj['instruction'] = instruction['instruction']
                    instruction_obj['raw_text'] = instruction['raw_text']
                    instruction_obj['drug'] = instruction['drug']
                    instruction_obj['action'] = instruction['action']
                    # ---------------------------------------------------------------------
                    #   Quantity
                    instruction_qty = Quantity()
                    instruction_qty['quantity'] = instruction['quantity']['quantity']
                    instruction_qty['unit'] = instruction['quantity']['unit']
                    #   Duration
                    instruction_dur = Duration()
                    instruction_dur['quantity'] = instruction['duration']['quantity']
                    instruction_dur['unit'] = instruction['duration']['unit']
                    #   Periodicity
                    instruction_rate = Periodicity()
                    instruction_rate['quantity'] = instruction['periodicity']['quantity']
                    instruction_rate['unit'] = instruction['periodicity']['unit']
                    # ---------------------------------------------------------------------
                    instruction_obj['indication_of_use'] = instruction['indication_of_use']
                    instruction_obj['complement'] = instruction['complement']
                    instruction_obj['start_date'] = instruction['start_date']
                    instruction_obj['to_deactivate'] = instruction['to_deactivate']
                    instruction_obj['active'] = instruction['active']
                    prescription_instructions.append(instruction_obj)
                prescription.instructions = prescription_instructions
            prescription.active = element['active']
            prescription.raw_text = element['raw_text']
            self.append(prescription)
