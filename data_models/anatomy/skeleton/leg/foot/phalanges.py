from data_models.anatomy.skeleton.bone import Bone
"""
For foot phalanges
"""


#   First toe
class FirstProximal(Bone):
    def __init__(self, bone_ids=None,  path_obj=None, bone_names=None, right=True, colors=None):
        if right:
            super().__init__(bone_id=bone_ids.r_1_phalanx_proximal, image_path=path_obj.r_1_phalanx_proximal, name=bone_names.r_1_phalanx_proximal, colors=colors)
        else:
            super().__init__(bone_id=bone_ids.l_1_phalanx_proximal, image_path=path_obj.l_1_phalanx_proximal, name=bone_names.l_1_phalanx_proximal, colors=colors)
        self.right = right


class FirstDistal(Bone):
    def __init__(self, bone_ids=None,  path_obj=None, bone_names=None, right=True, colors=None):
        if right:
            super().__init__(bone_id=bone_ids.r_1_phalanx_distal, image_path=path_obj.r_1_phalanx_distal, name=bone_names.r_1_phalanx_distal, colors=colors)
        else:
            super().__init__(bone_id=bone_ids.l_1_phalanx_distal, image_path=path_obj.l_1_phalanx_distal, name=bone_names.l_1_phalanx_distal, colors=colors)
        self.right = right


#   Second toe
class SecondProximal(Bone):
    def __init__(self, bone_ids=None,  path_obj=None, bone_names=None, right=True, colors=None):
        if right:
            super().__init__(bone_id=bone_ids.r_2_phalanx_proximal, image_path=path_obj.r_2_phalanx_proximal, name=bone_names.r_2_phalanx_proximal, colors=colors)
        else:
            super().__init__(bone_id=bone_ids.l_2_phalanx_proximal, image_path=path_obj.l_2_phalanx_proximal, name=bone_names.l_2_phalanx_proximal, colors=colors)
        self.right = right


class SecondIntermediate(Bone):
    def __init__(self, bone_ids=None,  path_obj=None, bone_names=None, right=True, colors=None):
        if right:
            super().__init__(bone_id=bone_ids.r_2_phalanx_intermediate, image_path=path_obj.r_2_phalanx_intermediate, name=bone_names.r_2_phalanx_intermediate, colors=colors)
        else:
            super().__init__(bone_id=bone_ids.l_2_phalanx_intermediate, image_path=path_obj.l_2_phalanx_intermediate, name=bone_names.l_2_phalanx_intermediate, colors=colors)
        self.right = right


class SecondDistal(Bone):
    def __init__(self, bone_ids=None,  path_obj=None, bone_names=None, right=True, colors=None):
        if right:
            super().__init__(bone_id=bone_ids.r_2_phalanx_distal, image_path=path_obj.r_2_phalanx_distal, name=bone_names.r_2_phalanx_distal, colors=colors)
        else:
            super().__init__(bone_id=bone_ids.l_2_phalanx_distal, image_path=path_obj.l_2_phalanx_distal, name=bone_names.l_2_phalanx_distal, colors=colors)
        self.right = right


#   Third toe
class ThirdProximal(Bone):
    def __init__(self, bone_ids=None,  path_obj=None, bone_names=None, right=True, colors=None):
        if right:
            super().__init__(bone_id=bone_ids.r_3_phalanx_proximal, image_path=path_obj.r_3_phalanx_proximal, name=bone_names.r_3_phalanx_proximal, colors=colors)
        else:
            super().__init__(bone_id=bone_ids.l_3_phalanx_proximal, image_path=path_obj.l_3_phalanx_proximal, name=bone_names.l_3_phalanx_proximal, colors=colors)
        self.right = right


class ThirdIntermediate(Bone):
    def __init__(self, bone_ids=None,  path_obj=None, bone_names=None, right=True, colors=None):
        if right:
            super().__init__(bone_id=bone_ids.r_3_phalanx_intermediate, image_path=path_obj.r_3_phalanx_intermediate, name=bone_names.r_3_phalanx_intermediate, colors=colors)
        else:
            super().__init__(bone_id=bone_ids.l_3_phalanx_intermediate, image_path=path_obj.l_3_phalanx_intermediate, name=bone_names.l_3_phalanx_intermediate, colors=colors)
        self.right = right


class ThirdDistal(Bone):
    def __init__(self, bone_ids=None,  path_obj=None, bone_names=None, right=True, colors=None):
        if right:
            super().__init__(bone_id=bone_ids.r_3_phalanx_distal, image_path=path_obj.r_3_phalanx_distal, name=bone_names.r_3_phalanx_distal, colors=colors)
        else:
            super().__init__(bone_id=bone_ids.l_3_phalanx_distal, image_path=path_obj.l_3_phalanx_distal, name=bone_names.l_3_phalanx_distal, colors=colors)
        self.right = right


#   Fourth toe
class FourthProximal(Bone):
    def __init__(self, bone_ids=None,  path_obj=None, bone_names=None, right=True, colors=None):
        if right:
            super().__init__(bone_id=bone_ids.r_4_phalanx_proximal, image_path=path_obj.r_4_phalanx_proximal, name=bone_names.r_4_phalanx_proximal, colors=colors)
        else:
            super().__init__(bone_id=bone_ids.l_4_phalanx_proximal, image_path=path_obj.l_4_phalanx_proximal, name=bone_names.l_4_phalanx_proximal, colors=colors)
        self.right = right


class FourthIntermediate(Bone):
    def __init__(self, bone_ids=None,  path_obj=None, bone_names=None, right=True, colors=None):
        if right:
            super().__init__(bone_id=bone_ids.r_4_phalanx_intermediate, image_path=path_obj.r_4_phalanx_intermediate, name=bone_names.r_4_phalanx_intermediate, colors=colors)
        else:
            super().__init__(bone_id=bone_ids.l_4_phalanx_intermediate, image_path=path_obj.l_4_phalanx_intermediate, name=bone_names.l_4_phalanx_intermediate, colors=colors)
        self.right = right


class FourthDistal(Bone):
    def __init__(self, bone_ids=None,  path_obj=None, bone_names=None, right=True, colors=None):
        if right:
            super().__init__(bone_id=bone_ids.r_4_phalanx_distal, image_path=path_obj.r_4_phalanx_distal, name=bone_names.r_4_phalanx_distal, colors=colors)
        else:
            super().__init__(bone_id=bone_ids.l_4_phalanx_distal, image_path=path_obj.l_4_phalanx_distal, name=bone_names.l_4_phalanx_distal, colors=colors)
        self.right = right


#   Fifth toe
class FifthProximal(Bone):
    def __init__(self, bone_ids=None,  path_obj=None, bone_names=None, right=True, colors=None):
        if right:
            super().__init__(bone_id=bone_ids.r_5_phalanx_proximal, image_path=path_obj.r_5_phalanx_proximal, name=bone_names.r_5_phalanx_proximal, colors=colors)
        else:
            super().__init__(bone_id=bone_ids.l_5_phalanx_proximal, image_path=path_obj.l_5_phalanx_proximal, name=bone_names.l_5_phalanx_proximal, colors=colors)
        self.right = right


class FifthIntermediate(Bone):
    def __init__(self, bone_ids=None,  path_obj=None, bone_names=None, right=True, colors=None):
        if right:
            super().__init__(bone_id=bone_ids.r_5_phalanx_intermediate, image_path=path_obj.r_5_phalanx_intermediate, name=bone_names.r_5_phalanx_intermediate, colors=colors)
        else:
            super().__init__(bone_id=bone_ids.l_5_phalanx_intermediate, image_path=path_obj.l_5_phalanx_intermediate, name=bone_names.l_5_phalanx_intermediate, colors=colors)
        self.right = right


class FifthDistal(Bone):
    def __init__(self, bone_ids=None,  path_obj=None, bone_names=None, right=True, colors=None):
        if right:
            super().__init__(bone_id=bone_ids.r_5_phalanx_distal, image_path=path_obj.r_5_phalanx_distal, name=bone_names.r_5_phalanx_distal, colors=colors)
        else:
            super().__init__(bone_id=bone_ids.l_5_phalanx_distal, image_path=path_obj.l_5_phalanx_distal, name=bone_names.l_5_phalanx_distal, colors=colors)
        self.right = right
