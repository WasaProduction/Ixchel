from data_models.anatomy.skeleton.bone import Bone
"""
For metatarsal
"""


class Metatarsal:
    def __init__(self, bone_ids=None,  path_obj=None, bone_names=None, right=True, colors=None):
        self.first = FirstMetatarsal(bone_ids=bone_ids, path_obj=path_obj, bone_names=bone_names, right=right, colors=colors)
        self.second = SecondMetatarsal(bone_ids=bone_ids, path_obj=path_obj, bone_names=bone_names, right=right, colors=colors)
        self.third = ThirdMetatarsal(bone_ids=bone_ids, path_obj=path_obj, bone_names=bone_names, right=right, colors=colors)
        self.fourth = FourthMetatarsal(bone_ids=bone_ids, path_obj=path_obj, bone_names=bone_names, right=right, colors=colors)
        self.fifth = FifthMetatarsal(bone_ids=bone_ids, path_obj=path_obj, bone_names=bone_names, right=right, colors=colors)


class FirstMetatarsal(Bone):
    def __init__(self, bone_ids=None,  path_obj=None, bone_names=None, right=True, colors=None):
        if right:
            super().__init__(bone_id=bone_ids.r_first_metatarsal, image_path=path_obj.r_first_metatarsal, name=bone_names.r_first_metatarsal, colors=colors)
        else:
            super().__init__(bone_id=bone_ids.l_first_metatarsal, image_path=path_obj.l_first_metatarsal, name=bone_names.l_first_metatarsal, colors=colors)
        self.right = right


class SecondMetatarsal(Bone):
    def __init__(self, bone_ids=None,  path_obj=None, bone_names=None, right=True, colors=None):
        if right:
            super().__init__(bone_id=bone_ids.r_second_metatarsal, image_path=path_obj.r_second_metatarsal, name=bone_names.r_second_metatarsal, colors=colors)
        else:
            super().__init__(bone_id=bone_ids.l_second_metatarsal, image_path=path_obj.l_second_metatarsal, name=bone_names.l_second_metatarsal, colors=colors)
        self.right = right


class ThirdMetatarsal(Bone):
    def __init__(self, bone_ids=None,  path_obj=None, bone_names=None, right=True, colors=None):
        if right:
            super().__init__(bone_id=bone_ids.r_third_metatarsal, image_path=path_obj.r_third_metatarsal, name=bone_names.r_third_metatarsal, colors=colors)
        else:
            super().__init__(bone_id=bone_ids.l_third_metatarsal, image_path=path_obj.l_third_metatarsal, name=bone_names.l_third_metatarsal, colors=colors)
        self.right = right


class FourthMetatarsal(Bone):
    def __init__(self, bone_ids=None,  path_obj=None, bone_names=None, right=True, colors=None):
        if right:
            super().__init__(bone_id=bone_ids.r_fourth_metatarsal, image_path=path_obj.r_fourth_metatarsal, name=bone_names.r_fourth_metatarsal, colors=colors)
        else:
            super().__init__(bone_id=bone_ids.l_fourth_metatarsal, image_path=path_obj.l_fourth_metatarsal, name=bone_names.l_fourth_metatarsal, colors=colors)
        self.right = right


class FifthMetatarsal(Bone):
    def __init__(self, bone_ids=None,  path_obj=None, bone_names=None, right=True, colors=None):
        if right:
            super().__init__(bone_id=bone_ids.r_fifth_metatarsal, image_path=path_obj.r_fifth_metatarsal, name=bone_names.r_fifth_metatarsal, colors=colors)
        else:
            super().__init__(bone_id=bone_ids.l_fifth_metatarsal, image_path=path_obj.l_fifth_metatarsal, name=bone_names.l_fifth_metatarsal, colors=colors)
        self.right = right
