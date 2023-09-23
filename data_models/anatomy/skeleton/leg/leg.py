from data_models.anatomy.skeleton.bone import Bone
from data_models.anatomy.skeleton.leg.foot.foot import Foot
"""
For leg
Classes:
    Leg
"""


class Leg:
    def __init__(self, bone_ids=None,  path_obj=None, bone_names=None, right=None):
        self.right = right
        self.femur = Femur(bone_ids=bone_ids, path_obj=path_obj, bone_names=bone_names, right=right)
        self.patella = Patella(bone_ids=bone_ids, path_obj=path_obj, bone_names=bone_names, right=right)
        self.tibia = Tibia(bone_ids=bone_ids, path_obj=path_obj, bone_names=bone_names, right=right)
        self.fibula = Fibula(bone_ids=bone_ids, path_obj=path_obj, bone_names=bone_names, right=right)
        self.foot = Foot(bone_ids=bone_ids, path_obj=path_obj, bone_names=bone_names, right=right)


class Femur(Bone):
    def __init__(self, bone_ids=None,  path_obj=None, bone_names=None, right=True):
        if right:
            super().__init__(bone_id=bone_ids.r_femur, image_path=path_obj.r_femur, name=bone_names.r_femur)
        else:
            super().__init__(bone_id=bone_ids.l_femur, image_path=path_obj.l_femur, name=bone_names.r_femur)


class Patella(Bone):
    def __init__(self, bone_ids=None,  path_obj=None, bone_names=None, right=True):
        if right:
            super().__init__(bone_id=bone_ids.r_patella, image_path=path_obj.r_patella, name=bone_names.r_femur)
        else:
            super().__init__(bone_id=bone_ids.l_patella, image_path=path_obj.l_patella, name=bone_names.r_femur)


class Tibia(Bone):
    def __init__(self, bone_ids=None,  path_obj=None, bone_names=None, right=True):
        if right:
            super().__init__(bone_id=bone_ids.r_tibia, image_path=path_obj.r_tibia, name=bone_names.r_tibia)
        else:
            super().__init__(bone_id=bone_ids.l_tibia, image_path=path_obj.l_tibia, name=bone_names.l_tibia)


class Fibula(Bone):
    def __init__(self, bone_ids=None,  path_obj=None, bone_names=None, right=True):
        if right:
            super().__init__(bone_id=bone_ids.r_fibula, image_path=path_obj.r_fibula, name=bone_names.r_fibula)
        else:
            super().__init__(bone_id=bone_ids.l_fibula, image_path=path_obj.l_fibula, name=bone_names.l_fibula)
