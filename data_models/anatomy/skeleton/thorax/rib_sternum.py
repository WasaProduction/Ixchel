from data_models.anatomy.skeleton.bone import Bone
"""
For ribs joined to the sternum 1-7
"""


class T1(Bone):
    def __init__(self, bone_ids=None,  path_obj=None, bone_names=None, right=True, colors=None):
        if right:
            super().__init__(bone_id=bone_ids.rib_r_t01, image_path=path_obj.rib_r_t01, name=bone_names.rib_r_t01, colors=colors)
        else:
            super().__init__(bone_id=bone_ids.rib_l_t01, image_path=path_obj.rib_l_t01, name=bone_names.rib_l_t01, colors=colors)
        self.right = right


class T2(Bone):
    def __init__(self, bone_ids=None,  path_obj=None, bone_names=None, right=True, colors=None):
        if right:
            super().__init__(bone_id=bone_ids.rib_r_t02, image_path=path_obj.rib_r_t02, name=bone_names.rib_r_t02, colors=colors)
        else:
            super().__init__(bone_id=bone_ids.rib_l_t02, image_path=path_obj.rib_l_t02, name=bone_names.rib_l_t02, colors=colors)
        self.right = right


class T3(Bone):
    def __init__(self, bone_ids=None,  path_obj=None, bone_names=None, right=True, colors=None):
        if right:
            super().__init__(bone_id=bone_ids.rib_r_t03, image_path=path_obj.rib_r_t03, name=bone_names.rib_r_t03, colors=colors)
        else:
            super().__init__(bone_id=bone_ids.rib_l_t03, image_path=path_obj.rib_l_t03, name=bone_names.rib_l_t03, colors=colors)
        self.right = right


class T4(Bone):
    def __init__(self, bone_ids=None,  path_obj=None, bone_names=None, right=True, colors=None):
        if right:
            super().__init__(bone_id=bone_ids.rib_r_t04, image_path=path_obj.rib_r_t04, name=bone_names.rib_r_t04, colors=colors)
        else:
            super().__init__(bone_id=bone_ids.rib_l_t04, image_path=path_obj.rib_l_t04, name=bone_names.rib_l_t04, colors=colors)
        self.right = right


class T5(Bone):
    def __init__(self, bone_ids=None,  path_obj=None, bone_names=None, right=True, colors=None):
        if right:
            super().__init__(bone_id=bone_ids.rib_r_t05, image_path=path_obj.rib_r_t05, name=bone_names.rib_r_t05, colors=colors)
        else:
            super().__init__(bone_id=bone_ids.rib_l_t05, image_path=path_obj.rib_l_t05, name=bone_names.rib_l_t05, colors=colors)
        self.right = right


class T6(Bone):
    def __init__(self, bone_ids=None,  path_obj=None, bone_names=None, right=True, colors=None):
        if right:
            super().__init__(bone_id=bone_ids.rib_r_t06, image_path=path_obj.rib_r_t06, name=bone_names.rib_r_t06, colors=colors)
        else:
            super().__init__(bone_id=bone_ids.rib_l_t06, image_path=path_obj.rib_l_t06, name=bone_names.rib_l_t06, colors=colors)
        self.right = right


class T7(Bone):
    def __init__(self, bone_ids=None,  path_obj=None, bone_names=None, right=True, colors=None):
        if right:
            super().__init__(bone_id=bone_ids.rib_r_t07, image_path=path_obj.rib_r_t07, name=bone_names.rib_r_t07, colors=colors)
        else:
            super().__init__(bone_id=bone_ids.rib_l_t07, image_path=path_obj.rib_l_t07, name=bone_names.rib_l_t07, colors=colors)
        self.right = right
