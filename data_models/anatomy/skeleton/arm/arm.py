from data_models.anatomy.skeleton.bone import Bone
from data_models.anatomy.skeleton.arm.hand.hand import Hand
"""
For arm
Classes:
    Arm
"""


class Arm:
    def __init__(self, bone_ids=None, path_obj=None, bone_names=None, right=True):
        self.humerus = Humerus(bone_ids, path_obj, bone_names, right)
        self.radius = Radius(bone_ids, path_obj, bone_names, right)
        self.ulna = Ulna(bone_ids, path_obj, bone_names, right)
        self.hand = Hand(bone_ids, path_obj, bone_names, right)
        self.right = right


class Humerus(Bone):
    def __init__(self, bone_ids=None,  path_obj=None, bone_names=None, right=True):
        if right:
            super().__init__(bone_id=bone_ids.r_humerus, image_path=path_obj.r_humerus, name=bone_names.r_humerus)
        else:
            super().__init__(bone_id=bone_ids.l_humerus, image_path=path_obj.l_humerus, name=bone_names.l_humerus)

        self.right = right


class Radius(Bone):
    def __init__(self, bone_ids=None,  path_obj=None, bone_names=None, right=True):
        if right:
            super().__init__(bone_id=bone_ids.r_radius, image_path=path_obj.r_radius, name=bone_names.r_radius)
        else:
            super().__init__(bone_id=bone_ids.l_radius, image_path=path_obj.l_radius, name=bone_names.l_radius)
        self.right = right


class Ulna(Bone):
    def __init__(self, bone_ids=None,  path_obj=None, bone_names=None, right=True):
        if right:
            super().__init__(bone_id=bone_ids.r_ulna, image_path=path_obj.r_ulna, name=bone_names.r_ulna)
        else:
            super().__init__(bone_id=bone_ids.l_ulna, image_path=path_obj.l_ulna, name=bone_names.l_ulna)
        self.right = right
