from data_models.anatomy.skeleton.bone import Bone
from data_models.anatomy.skeleton.leg.foot.foot import Foot
"""
For leg
Classes:
    Leg
"""


class Leg:
    def __init__(self, bone_ids=None,  path_obj=None, bone_names=None, right=None, colors=None):
        self.right = right
        self.femur = Femur(bone_ids=bone_ids, path_obj=path_obj, bone_names=bone_names, right=right, colors=colors)
        self.patella = Patella(bone_ids=bone_ids, path_obj=path_obj, bone_names=bone_names, right=right, colors=colors)
        self.tibia = Tibia(bone_ids=bone_ids, path_obj=path_obj, bone_names=bone_names, right=right, colors=colors)
        self.fibula = Fibula(bone_ids=bone_ids, path_obj=path_obj, bone_names=bone_names, right=right, colors=colors)
        self.foot = Foot(bone_ids=bone_ids, path_obj=path_obj, bone_names=bone_names, right=right, colors=colors)


class Femur(Bone):
    def __init__(self, bone_ids=None,  path_obj=None, bone_names=None, right=True, colors=None):
        if right:
            super().__init__(bone_id=bone_ids.r_femur, image_path=path_obj.r_femur, name=bone_names.r_femur, colors=colors)
        else:
            super().__init__(bone_id=bone_ids.l_femur, image_path=path_obj.l_femur, name=bone_names.r_femur, colors=colors)


class Patella(Bone):
    def __init__(self, bone_ids=None,  path_obj=None, bone_names=None, right=True, colors=None):
        if right:
            super().__init__(bone_id=bone_ids.r_patella, image_path=path_obj.r_patella, name=bone_names.r_femur, colors=colors)
        else:
            super().__init__(bone_id=bone_ids.l_patella, image_path=path_obj.l_patella, name=bone_names.r_femur, colors=colors)


class Tibia(Bone):
    def __init__(self, bone_ids=None,  path_obj=None, bone_names=None, right=True, colors=None):
        if right:
            super().__init__(bone_id=bone_ids.r_tibia, image_path=path_obj.r_tibia, name=bone_names.r_tibia, colors=colors)
        else:
            super().__init__(bone_id=bone_ids.l_tibia, image_path=path_obj.l_tibia, name=bone_names.l_tibia, colors=colors)


class Fibula(Bone):
    def __init__(self, bone_ids=None,  path_obj=None, bone_names=None, right=True, colors=None):
        if right:
            super().__init__(bone_id=bone_ids.r_fibula, image_path=path_obj.r_fibula, name=bone_names.r_fibula, colors=colors)
        else:
            super().__init__(bone_id=bone_ids.l_fibula, image_path=path_obj.l_fibula, name=bone_names.l_fibula, colors=colors)
