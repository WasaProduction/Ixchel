from data_models.anatomy.skeleton.bone import Bone
"""
For ribs joined to the sternum 1-7
"""


class T1(Bone):
    def __init__(self, bone_ids=None,  path_obj=None, bone_names=None, right=True):
        if right:
            super().__init__(bone_id=bone_ids.rib_r_t01, image_path=path_obj.rib_r_t01, name=bone_names.rib_r_t01)
        else:
            super().__init__(bone_id=bone_ids.rib_l_t01, image_path=path_obj.rib_l_t01, name=bone_names.rib_l_t01)
        self.right = right


class T2(Bone):
    def __init__(self, bone_ids=None,  path_obj=None, bone_names=None, right=True):
        if right:
            super().__init__(bone_id=bone_ids.rib_r_t02, image_path=path_obj.rib_r_t02, name=bone_names.rib_r_t02)
        else:
            super().__init__(bone_id=bone_ids.rib_l_t02, image_path=path_obj.rib_l_t02, name=bone_names.rib_l_t02)
        self.right = right


class T3(Bone):
    def __init__(self, bone_ids=None,  path_obj=None, bone_names=None, right=True):
        if right:
            super().__init__(bone_id=bone_ids.rib_r_t03, image_path=path_obj.rib_r_t03, name=bone_names.rib_r_t03)
        else:
            super().__init__(bone_id=bone_ids.rib_l_t03, image_path=path_obj.rib_l_t03, name=bone_names.rib_l_t03)
        self.right = right


class T4(Bone):
    def __init__(self, bone_ids=None,  path_obj=None, bone_names=None, right=True):
        if right:
            super().__init__(bone_id=bone_ids.rib_r_t04, image_path=path_obj.rib_r_t04, name=bone_names.rib_r_t04)
        else:
            super().__init__(bone_id=bone_ids.rib_l_t04, image_path=path_obj.rib_l_t04, name=bone_names.rib_l_t04)
        self.right = right


class T5(Bone):
    def __init__(self, bone_ids=None,  path_obj=None, bone_names=None, right=True):
        if right:
            super().__init__(bone_id=bone_ids.rib_r_t05, image_path=path_obj.rib_r_t05, name=bone_names.rib_r_t05)
        else:
            super().__init__(bone_id=bone_ids.rib_l_t05, image_path=path_obj.rib_l_t05, name=bone_names.rib_l_t05)
        self.right = right


class T6(Bone):
    def __init__(self, bone_ids=None,  path_obj=None, bone_names=None, right=True):
        if right:
            super().__init__(bone_id=bone_ids.rib_r_t06, image_path=path_obj.rib_r_t06, name=bone_names.rib_r_t06)
        else:
            super().__init__(bone_id=bone_ids.rib_l_t06, image_path=path_obj.rib_l_t06, name=bone_names.rib_l_t06)
        self.right = right


class T7(Bone):
    def __init__(self, bone_ids=None,  path_obj=None, bone_names=None, right=True):
        if right:
            super().__init__(bone_id=bone_ids.rib_r_t07, image_path=path_obj.rib_r_t07, name=bone_names.rib_r_t07)
        else:
            super().__init__(bone_id=bone_ids.rib_l_t07, image_path=path_obj.rib_l_t07, name=bone_names.rib_l_t07)
        self.right = right
