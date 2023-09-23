from data_models.anatomy.skeleton.bone import Bone
"""
For cervical vertebrae C1-C7
Classes:
    C1, C2, C3, C4, C5, C6, C7
"""


class C1(Bone):
    def __init__(self, bone_ids=None,  path_obj=None, bone_names=None):
        super().__init__(bone_id=bone_ids.c1, image_path=path_obj.c1, name=bone_names.c1)


class C2(Bone):
    def __init__(self, bone_ids=None,  path_obj=None, bone_names=None):
        super().__init__(bone_id=bone_ids.c2, image_path=path_obj.c2, name=bone_names.c2)


class C3(Bone):
    def __init__(self, bone_ids=None,  path_obj=None, bone_names=None):
        super().__init__(bone_id=bone_ids.c3, image_path=path_obj.c3, name=bone_names.c3)


class C4(Bone):
    def __init__(self, bone_ids=None,  path_obj=None, bone_names=None):
        super().__init__(bone_id=bone_ids.c4, image_path=path_obj.c4, name=bone_names.c4)


class C5(Bone):
    def __init__(self, bone_ids=None,  path_obj=None, bone_names=None):
        super().__init__(bone_id=bone_ids.c5, image_path=path_obj.c5, name=bone_names.c5)


class C6(Bone):
    def __init__(self, bone_ids=None,  path_obj=None, bone_names=None):
        super().__init__(bone_id=bone_ids.c6, image_path=path_obj.c6, name=bone_names.c6)


class C7(Bone):
    def __init__(self, bone_ids=None,  path_obj=None, bone_names=None):
        super().__init__(bone_id=bone_ids.c7, image_path=path_obj.c7, name=bone_names.c7)
