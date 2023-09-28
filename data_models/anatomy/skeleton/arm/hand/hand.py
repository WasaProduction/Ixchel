from data_models.anatomy.skeleton.arm.hand.carpals import Carpals
from data_models.anatomy.skeleton.arm.hand.fingers import *
from data_models.anatomy.skeleton.arm.hand.metacarpals import *


class Hand:
    def __init__(self, bone_ids=None,  path_obj=None, bone_names=None, right=True, colors=None):
        self.carpals = Carpals(bone_ids=bone_ids,  path_obj=path_obj, bone_names=bone_names, right=right, colors=colors)
        self.metacarpals = Metacarpals(bone_ids=bone_ids,  path_obj=path_obj, bone_names=bone_names, right=right, colors=colors)
        self.fingers = Fingers(bone_ids=bone_ids,  path_obj=path_obj, bone_names=bone_names, right=right, colors=colors)
        self.right = right
