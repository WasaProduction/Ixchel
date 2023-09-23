from collections import UserDict


class FullDiagnosis(UserDict):
    def __init__(self, object_id=None, created_by=None, patient_id=None, creation_date=None, interrogatory=None,
                 diagnosis=None, prescription=None, physical_examination=None):
        super().__init__()
        self['object_id'] = object_id
        self['created_by'] = created_by
        self['patient_id'] = patient_id
        self['creation_date'] = creation_date
        self['interrogatory'] = interrogatory
        self['physical_examination'] = physical_examination
        self['diagnosis'] = diagnosis
        self['prescription'] = prescription


class SystemsAparatus(UserDict):
    def __init__(self, cardiovascular_system=None, respiratory_system=None, digestive_system=None,
                 nephro_urological_system=None, endocrine_system_and_metabolism=None, hematopoietic_system=None,
                 nervous_system=None, musculoskeletal_system=None, skin_and_integuments=None, sense_organs=None,
                 psychic_sphere=None):
        super().__init__()
        self['cardiovascular_system'] = cardiovascular_system
        self['respiratory_system'] = respiratory_system
        self['digestive_system'] = digestive_system
        self['nephro_urological_system'] = nephro_urological_system
        self['endocrine_system_and_metabolism'] = endocrine_system_and_metabolism
        self['hematopoietic_system'] = hematopoietic_system
        self['nervous_system'] = nervous_system
        self['musculoskeletal_system'] = musculoskeletal_system
        self['skin_and_integuments'] = skin_and_integuments
        self['sense_organs'] = sense_organs
        self['psychic_sphere'] = psychic_sphere


class PhysicalExamination (UserDict):
    def __init__(self, vitals=None, head=None, eyes=None, ears=None, nose=None, throat=None, neck=None, chest=None,
                 abdomen=None, reproductive_system=None, urinary=None, right_shoulder=None, left_shoulder=None,
                 right_arm=None, left_arm=None, right_hand=None, left_hand=None, hip=None, right_leg=None,
                 left_leg=None, right_foot=None, left_foot=None, vision_acuity=None, hearing_acuity=None,
                 gastrointestinal_examination=None, cardiovascular_evaluation=None, respiratory_assessment=None,
                 musculoskeletal_assessment=None, neuro_exam=None, skin_lymph_node_check=None):
        super().__init__()
        self['vitals'] = vitals
        self['head'] = head
        self['eyes'] = eyes
        self['ears'] = ears
        self['nose'] = nose
        self['throat'] = throat
        self['neck'] = neck
        self['chest'] = chest
        self['abdomen'] = abdomen
        self['reproductive_system'] = reproductive_system
        self['urinary'] = urinary
        self['right_shoulder'] = right_shoulder
        self['left_shoulder'] = left_shoulder
        self['right_arm'] = right_arm
        self['left_arm'] = left_arm
        self['right_hand'] = right_hand
        self['left_hand'] = left_hand
        self['hip'] = hip
        self['right_leg'] = right_leg
        self['left_leg'] = left_leg
        self['right_foot'] = right_foot
        self['left_foot'] = left_foot
        self['vision_acuity'] = vision_acuity
        self['hearing_acuity'] = hearing_acuity
        self['gastrointestinal_exa mination'] = gastrointestinal_examination
        self['cardiovascular_evaluation'] = cardiovascular_evaluation
        self['respiratory_assessment'] = respiratory_assessment
        self['musculoskeletal_assessment'] = musculoskeletal_assessment
        self['neuro_exam'] = neuro_exam
        self['skin_lymph_node_check'] = skin_lymph_node_check


class Diagnosis(UserDict):
    def __init__(self, diagnosis=None, tags_contained=None):
        super().__init__()
        self['diagnosis'] = diagnosis
        self['tags_contained'] = tags_contained


class Prescription(UserDict):
    def __init__(self, prescription_id=None, drug=None, dosage=None, quantity=None, frequency=None, frequency_unit=None,
                 duration=None, duration_unit=None, use_indication=None):
        super().__init__()
        self['prescription_id'] = prescription_id
        self['drug'] = drug
        self['dosage'] = dosage
        self['quantity'] = quantity
        self['frequency'] = frequency
        self['frequency_unit'] = frequency_unit
        self['duration'] = duration
        self['duration_unit'] = duration_unit
        self['use_indication'] = use_indication


class Drug(UserDict):
    def __init__(self, drug_id=None, name=None, form=None, doses=None, doses_unit=None, lab=None, content=None,
                 units_contents=None, category=None, administration_route=None, approved=None, salts=None,
                 side_effects=None, description=None):
        super().__init__()
        self['drug_id'] = drug_id
        self['name'] = name
        self['form'] = form
        self['doses'] = doses
        self['doses_unit'] = doses_unit
        self['lab'] = lab
        self['content'] = content
        self['units_contents'] = units_contents
        self['category'] = category
        self['administration_route'] = administration_route
        self['approved'] = approved
        self['salts'] = salts
        self['side_effects'] = side_effects
        self['description'] = description


class DrugSalt(UserDict):
    def __init__(self, salt_id=None, name=None, content=None, description=None):
        super().__init__()
        self['salt_id'] = salt_id
        self['name'] = name
        self['content'] = content
        self['description'] = description
