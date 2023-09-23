from data_models.anatomy.skeleton.bone import Bone
"""
For thoracic vertebrae T1-T12
Classes:
    T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12
"""


class T1(Bone):
    def __init__(self, bone_ids=None,  path_obj=None, bone_names=None):
        super().__init__(bone_id=bone_ids.t1, image_path=path_obj.t1, name=bone_names.t1)


class T2(Bone):
    def __init__(self, bone_ids=None,  path_obj=None, bone_names=None):
        super().__init__(bone_id=bone_ids.t2, image_path=path_obj.t2, name=bone_names.t2)


class T3(Bone):
    def __init__(self, bone_ids=None,  path_obj=None, bone_names=None):
        super().__init__(bone_id=bone_ids.t3, image_path=path_obj.t3, name=bone_names.t3)


class T4(Bone):
    def __init__(self, bone_ids=None,  path_obj=None, bone_names=None):
        super().__init__(bone_id=bone_ids.t4, image_path=path_obj.t4, name=bone_names.t4)


class T5(Bone):
    def __init__(self, bone_ids=None,  path_obj=None, bone_names=None):
        super().__init__(bone_id=bone_ids.t5, image_path=path_obj.t5, name=bone_names.t5)


class T6(Bone):
    def __init__(self, bone_ids=None,  path_obj=None, bone_names=None):
        super().__init__(bone_id=bone_ids.t6, image_path=path_obj.t6, name=bone_names.t6)


class T7(Bone):
    def __init__(self, bone_ids=None,  path_obj=None, bone_names=None):
        super().__init__(bone_id=bone_ids.t7, image_path=path_obj.t7, name=bone_names.t7)


class T8(Bone):
    def __init__(self, bone_ids=None,  path_obj=None, bone_names=None):
        super().__init__(bone_id=bone_ids.t8, image_path=path_obj.t8, name=bone_names.t8)


class T9(Bone):
    def __init__(self, bone_ids=None,  path_obj=None, bone_names=None):
        super().__init__(bone_id=bone_ids.t9, image_path=path_obj.t9, name=bone_names.t9)


class T10(Bone):
    def __init__(self, bone_ids=None,  path_obj=None, bone_names=None):
        super().__init__(bone_id=bone_ids.t10, image_path=path_obj.t10, name=bone_names.t10)


class T11(Bone):
    def __init__(self, bone_ids=None,  path_obj=None, bone_names=None):
        super().__init__(bone_id=bone_ids.t11, image_path=path_obj.t11, name=bone_names.t11)


class T12(Bone):
    def __init__(self, bone_ids=None,  path_obj=None, bone_names=None):
        super().__init__(bone_id=bone_ids.t12, image_path=path_obj.t12, name=bone_names.t12)
