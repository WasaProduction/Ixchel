from data_models.anatomy.skeleton.bone import Bone
"""
For ribs joined to the sternum 8-10
"""


class T8(Bone):
    def __init__(self, bone_ids=None,  path_obj=None, bone_names=None, right=True, colors=None):
        if right:
            super().__init__(bone_id=bone_ids.rib_r_t08, image_path=path_obj.rib_r_t08, name=bone_names.rib_r_t08, colors=colors)
        else:
            super().__init__(bone_id=bone_ids.rib_l_t08, image_path=path_obj.rib_l_t08, name=bone_names.rib_r_t08, colors=colors)
        self.right = right


class T9(Bone):
    def __init__(self, bone_ids=None,  path_obj=None, bone_names=None, right=True, colors=None):
        if right:
            super().__init__(bone_id=bone_ids.rib_r_t09, image_path=path_obj.rib_r_t09, name=bone_names.rib_r_t09, colors=colors)
        else:
            super().__init__(bone_id=bone_ids.rib_l_t09, image_path=path_obj.rib_l_t09, name=bone_names.rib_l_t09, colors=colors)
        self.right = right


class T10(Bone):
    def __init__(self, bone_ids=None,  path_obj=None, bone_names=None, right=True, colors=None):
        if right:
            super().__init__(bone_id=bone_ids.rib_r_t10, image_path=path_obj.rib_r_t10, name=bone_names.rib_r_t10, colors=colors)
        else:
            super().__init__(bone_id=bone_ids.rib_l_t10, image_path=path_obj.rib_l_t10, name=bone_names.rib_l_t10, colors=colors)
        self.right = right
