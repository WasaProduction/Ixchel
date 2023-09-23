from data_models.anatomy.skeleton.bone import Bone
"""
For Pelvis
"""


class Sacrum(Bone):
    def __init__(self, bone_ids=None,  path_obj=None, bone_names=None):
        super().__init__(bone_id=bone_ids.sacrum, image_path=path_obj.sacrum, name=bone_names.sacrum)


class Coccyx(Bone):
    def __init__(self, bone_ids=None,  path_obj=None, bone_names=None):
        super().__init__(bone_id=bone_ids.coccyx, image_path=path_obj.coccyx, name=bone_names.coccyx)


class Hip(Bone):
    def __init__(self, bone_ids=None,  path_obj=None, bone_names=None, right=True):
        if right:
            super().__init__(bone_id=bone_ids.r_hip, image_path=path_obj.r_hip, name=bone_names.r_hip)
        else:
            super().__init__(bone_id=bone_ids.l_hip, image_path=path_obj.l_hip, name=bone_names.l_hip)
        self.right = right
