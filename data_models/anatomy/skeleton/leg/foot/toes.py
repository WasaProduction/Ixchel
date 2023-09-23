from data_models.anatomy.skeleton.leg.foot.phalanges import *
"""
For toes
"""


class Toes:
    def __init__(self, bone_ids=None,  path_obj=None, bone_names=None, right=None):
        self.first_toe = FirstToe(bone_ids=bone_ids, path_obj=path_obj, bone_names=bone_names, right=right)
        self.second_toe = SecondToe(bone_ids=bone_ids, path_obj=path_obj, bone_names=bone_names, right=right)
        self.third_toe = ThirdToe(bone_ids=bone_ids, path_obj=path_obj, bone_names=bone_names, right=right)
        self.fourth_toe = FourthToe(bone_ids=bone_ids, path_obj=path_obj, bone_names=bone_names, right=right)
        self.fifth_toe = FifthToe(bone_ids=bone_ids, path_obj=path_obj, bone_names=bone_names, right=right)


class FirstToe:
    def __init__(self, bone_ids=None,  path_obj=None, bone_names=None, right=None):
        self.proximal_phalanges = FirstProximal(bone_ids=bone_ids, path_obj=path_obj, bone_names=bone_names, right=right)
        self.distal_phalanges = FirstProximal(bone_ids=bone_ids, path_obj=path_obj, bone_names=bone_names, right=right)


class SecondToe:
    def __init__(self, bone_ids=None,  path_obj=None, bone_names=None, right=None):
        self.proximal_phalanges = SecondProximal(bone_ids=bone_ids, path_obj=path_obj, bone_names=bone_names, right=right)
        self.intermediate_phalanges = SecondIntermediate(bone_ids=bone_ids, path_obj=path_obj, bone_names=bone_names, right=right)
        self.distal_phalanges = SecondDistal(bone_ids=bone_ids, path_obj=path_obj, bone_names=bone_names, right=right)


class ThirdToe:
    def __init__(self, bone_ids=None,  path_obj=None, bone_names=None, right=None):
        self.proximal_phalanges = ThirdProximal(bone_ids=bone_ids, path_obj=path_obj, bone_names=bone_names, right=right)
        self.intermediate_phalanges = ThirdIntermediate(bone_ids=bone_ids, path_obj=path_obj, bone_names=bone_names, right=right)
        self.distal_phalanges = ThirdDistal(bone_ids=bone_ids, path_obj=path_obj, bone_names=bone_names, right=right)


class FourthToe:
    def __init__(self, bone_ids=None,  path_obj=None, bone_names=None, right=None):
        self.proximal_phalanges = FourthProximal(bone_ids=bone_ids, path_obj=path_obj, bone_names=bone_names, right=right)
        self.intermediate_phalanges = FourthIntermediate(bone_ids=bone_ids, path_obj=path_obj, bone_names=bone_names, right=right)
        self.distal_phalanges = FourthDistal(bone_ids=bone_ids, path_obj=path_obj, bone_names=bone_names, right=right)


class FifthToe:
    def __init__(self, bone_ids=None,  path_obj=None, bone_names=None, right=None):
        self.proximal_phalanges = FifthProximal(bone_ids=bone_ids, path_obj=path_obj, bone_names=bone_names, right=right)
        self.intermediate_phalanges = FifthIntermediate(bone_ids=bone_ids, path_obj=path_obj, bone_names=bone_names, right=right)
        self.distal_phalanges = FifthDistal(bone_ids=bone_ids, path_obj=path_obj, bone_names=bone_names, right=right)
