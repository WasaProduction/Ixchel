from data_models.anatomy.skeleton.bone import Bone
"""
For floating ribs 11-12
"""


class T11(Bone):
    def __init__(self, bone_ids=None,  path_obj=None, bone_names=None, right=True, colors=None):
        if right:
            super().__init__(bone_id=bone_ids.rib_r_t11, image_path=path_obj.rib_r_t11, name=bone_names.rib_r_t11, colors=colors)
        else:
            super().__init__(bone_id=bone_ids.rib_l_t11, image_path=path_obj.rib_l_t11, name=bone_names.rib_l_t11, colors=colors)
        self.right = right


class T12(Bone):
    def __init__(self, bone_ids=None,  path_obj=None, bone_names=None, right=True, colors=None):
        if right:
            super().__init__(bone_id=bone_ids.rib_r_t12, image_path=path_obj.rib_r_t12, name=bone_names.rib_r_t12, colors=colors)
        else:
            super().__init__(bone_id=bone_ids.rib_l_t12, image_path=path_obj.rib_l_t12, name=bone_names.rib_l_t12, colors=colors)
        self.right = right
