from data_models.anatomy.skeleton.vertebrae.cervical import *
from data_models.anatomy.skeleton.vertebrae.thoracic import *
from data_models.anatomy.skeleton.vertebrae.lumbar import *


class Vertebrae:
    def __init__(self, bone_ids=None,  path_obj=None, bone_names=None):
        #   Cervical
        self.C1 = C1(bone_ids=bone_ids, path_obj=path_obj, bone_names=bone_names)
        self.C2 = C2(bone_ids=bone_ids, path_obj=path_obj, bone_names=bone_names)
        self.C3 = C3(bone_ids=bone_ids, path_obj=path_obj, bone_names=bone_names)
        self.C4 = C4(bone_ids=bone_ids, path_obj=path_obj, bone_names=bone_names)
        self.C5 = C5(bone_ids=bone_ids, path_obj=path_obj, bone_names=bone_names)
        self.C6 = C6(bone_ids=bone_ids, path_obj=path_obj, bone_names=bone_names)
        self.C7 = C7(bone_ids=bone_ids, path_obj=path_obj, bone_names=bone_names)
        #   Thoracic
        self.T1 = T1(bone_ids=bone_ids, path_obj=path_obj, bone_names=bone_names)
        self.T2 = T2(bone_ids=bone_ids, path_obj=path_obj, bone_names=bone_names)
        self.T3 = T3(bone_ids=bone_ids, path_obj=path_obj, bone_names=bone_names)
        self.T4 = T4(bone_ids=bone_ids, path_obj=path_obj, bone_names=bone_names)
        self.T5 = T5(bone_ids=bone_ids, path_obj=path_obj, bone_names=bone_names)
        self.T6 = T6(bone_ids=bone_ids, path_obj=path_obj, bone_names=bone_names)
        self.T7 = T7(bone_ids=bone_ids, path_obj=path_obj, bone_names=bone_names)
        self.T8 = T8(bone_ids=bone_ids, path_obj=path_obj, bone_names=bone_names)
        self.T9 = T9(bone_ids=bone_ids, path_obj=path_obj, bone_names=bone_names)
        self.T10 = T10(bone_ids=bone_ids, path_obj=path_obj, bone_names=bone_names)
        self.T11 = T11(bone_ids=bone_ids, path_obj=path_obj, bone_names=bone_names)
        self.T12 = T12(bone_ids=bone_ids, path_obj=path_obj, bone_names=bone_names)
        #   Lumbar
        self.L1 = L1(bone_ids=bone_ids, path_obj=path_obj, bone_names=bone_names)
        self.L2 = L2(bone_ids=bone_ids, path_obj=path_obj, bone_names=bone_names)
        self.L3 = L3(bone_ids=bone_ids, path_obj=path_obj, bone_names=bone_names)
        self.L4 = L4(bone_ids=bone_ids, path_obj=path_obj, bone_names=bone_names)
        self.L5 = L5(bone_ids=bone_ids, path_obj=path_obj, bone_names=bone_names)
