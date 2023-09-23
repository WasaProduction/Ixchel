from data_models.anatomy.skeleton.bone import Bone
"""
For accessory ribs #
"""


class A1(Bone):
    def __init__(self, bone_ids=None,  path_obj=None, bone_names=None, right=True):
        if right:
            super().__init__(bone_id=bone_ids.rib_r_a01, image_path=path_obj.rib_r_a01, name=bone_names.rib_r_a01)
        else:
            super().__init__(bone_id=bone_ids.rib_l_a01, image_path=path_obj.rib_l_a01, name=bone_names.rib_l_a01)
        self.right = right
