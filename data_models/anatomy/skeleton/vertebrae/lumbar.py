from data_models.anatomy.skeleton.bone import Bone
"""
For lumbar vertebrae L1-L5
Classes:
    L1, L2, L3, L4, L5

"""


class L1(Bone):
    def __init__(self, bone_ids=None,  path_obj=None, bone_names=None, colors=None):
        super().__init__(bone_id=bone_ids.l1, image_path=path_obj.l1, name=bone_names.l1, colors=colors)


class L2(Bone):
    def __init__(self, bone_ids=None,  path_obj=None, bone_names=None, colors=None):
        super().__init__(bone_id=bone_ids.l2, image_path=path_obj.l2, name=bone_names.l2, colors=colors)


class L3(Bone):
    def __init__(self, bone_ids=None,  path_obj=None, bone_names=None, colors=None):
        super().__init__(bone_id=bone_ids.l2, image_path=path_obj.l3, name=bone_names.l3, colors=colors)


class L4(Bone):
    def __init__(self, bone_ids=None,  path_obj=None, bone_names=None, colors=None):
        super().__init__(bone_id=bone_ids.l4, image_path=path_obj.l4, name=bone_names.l4, colors=colors)


class L5(Bone):
    def __init__(self, bone_ids=None,  path_obj=None, bone_names=None, colors=None):
        super().__init__(bone_id=bone_ids.l5, image_path=path_obj.l5, name=bone_names.l5, colors=colors)
