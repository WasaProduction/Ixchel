from data_models.anatomy.skeleton.bone import Bone
"""
For Pelvis
"""


class Sacrum(Bone):
    def __init__(self, bone_ids=None,  path_obj=None, bone_names=None, colors=None):
        super().__init__(bone_id=bone_ids.sacrum, image_path=path_obj.sacrum, name=bone_names.sacrum, colors=colors)


class Coccyx(Bone):
    def __init__(self, bone_ids=None,  path_obj=None, bone_names=None, colors=None):
        super().__init__(bone_id=bone_ids.coccyx, image_path=path_obj.coccyx, name=bone_names.coccyx, colors=colors)


class Hip(Bone):
    def __init__(self, bone_ids=None,  path_obj=None, bone_names=None, right=True, colors=None):
        if right:
            super().__init__(bone_id=bone_ids.r_hip, image_path=path_obj.r_hip, name=bone_names.r_hip, colors=colors)
        else:
            super().__init__(bone_id=bone_ids.l_hip, image_path=path_obj.l_hip, name=bone_names.l_hip, colors=colors)
        self.right = right
