from data_models.anatomy.skeleton.bone import Bone
"""
For metacarpals
"""


class Metacarpals:
    def __init__(self, bone_ids=None,  path_obj=None, bone_names=None, right=True):
        self.first = FirstMetacarpal(bone_ids=bone_ids,  path_obj=path_obj, bone_names=bone_names, right=right)
        self.second = SecondMetacarpal(bone_ids=bone_ids,  path_obj=path_obj, bone_names=bone_names, right=right)
        self.third = ThirdMetacarpal(bone_ids=bone_ids,  path_obj=path_obj, bone_names=bone_names, right=right)
        self.fourth = FourthMetacarpal(bone_ids=bone_ids,  path_obj=path_obj, bone_names=bone_names, right=right)
        self.fifth = FifthMetacarpal(bone_ids=bone_ids,  path_obj=path_obj, bone_names=bone_names, right=right)
        self.right = right


class FirstMetacarpal(Bone):
    def __init__(self, bone_ids=None,  path_obj=None, bone_names=None, right=True):
        if right:
            super().__init__(bone_id=bone_ids.r_first_metacarpal, image_path=path_obj.r_first_metacarpal, name=bone_names.r_first_metacarpal)
        else:
            super().__init__(bone_id=bone_ids.l_first_metacarpal, image_path=path_obj.l_first_metacarpal, name=bone_names.l_first_metacarpal)
        self.right = right


class SecondMetacarpal(Bone):
    def __init__(self, bone_ids=None,  path_obj=None, bone_names=None, right=True):
        if right:
            super().__init__(bone_id=bone_ids.r_second_metacarpal, image_path=path_obj.r_second_metacarpal, name=bone_names.r_second_metacarpal)
        else:
            super().__init__(bone_id=bone_ids.l_second_metacarpal, image_path=path_obj.l_second_metacarpal, name=bone_names.l_second_metacarpal)
        self.right = right


class ThirdMetacarpal(Bone):
    def __init__(self, bone_ids=None,  path_obj=None, bone_names=None, right=True):
        if right:
            super().__init__(bone_id=bone_ids.r_third_metacarpal, image_path=path_obj.r_third_metacarpal, name=bone_names.r_third_metacarpal)
        else:
            super().__init__(bone_id=bone_ids.l_third_metacarpal, image_path=path_obj.l_third_metacarpal, name=bone_names.l_third_metacarpal)
        self.right = right


class FourthMetacarpal(Bone):
    def __init__(self, bone_ids=None,  path_obj=None, bone_names=None, right=True):
        if right:
            super().__init__(bone_id=bone_ids.r_fourth_metacarpal, image_path=path_obj.r_fourth_metacarpal, name=bone_names.r_fourth_metacarpal)
        else:
            super().__init__(bone_id=bone_ids.l_fourth_metacarpal, image_path=path_obj.l_fourth_metacarpal, name=bone_names.l_fourth_metacarpal)
        self.right = right


class FifthMetacarpal(Bone):
    def __init__(self, bone_ids=None,  path_obj=None, bone_names=None, right=True):
        if right:
            super().__init__(bone_id=bone_ids.r_fifth_metacarpal, image_path=path_obj.r_fifth_metacarpal, name=bone_names.r_fifth_metacarpal)
        else:
            super().__init__(bone_id=bone_ids.r_fifth_metacarpal, image_path=path_obj.r_fifth_metacarpal, name=bone_names.r_fifth_metacarpal)
        self.right = right
