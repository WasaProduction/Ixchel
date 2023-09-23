from collections import UserDict
# https://realpython.com/inherit-python-dict/


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
        self['gastrointestinal_examination'] = gastrointestinal_examination
        self['cardiovascular_evaluation'] = cardiovascular_evaluation
        self['respiratory_assessment'] = respiratory_assessment
        self['musculoskeletal_assessment'] = musculoskeletal_assessment
        self['neuro_exam'] = neuro_exam
        self['skin_lymph_node_check'] = skin_lymph_node_check
