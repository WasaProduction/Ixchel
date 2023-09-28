from data_models.anatomy.skeleton.leg.foot.phalanges import *
"""
For toes
"""


class Toes:
    def __init__(self, bone_ids=None,  path_obj=None, bone_names=None, right=None, colors=None):
        self.first_toe = FirstToe(bone_ids=bone_ids, path_obj=path_obj, bone_names=bone_names, right=right, colors=colors)
        self.second_toe = SecondToe(bone_ids=bone_ids, path_obj=path_obj, bone_names=bone_names, right=right, colors=colors)
        self.third_toe = ThirdToe(bone_ids=bone_ids, path_obj=path_obj, bone_names=bone_names, right=right, colors=colors)
        self.fourth_toe = FourthToe(bone_ids=bone_ids, path_obj=path_obj, bone_names=bone_names, right=right, colors=colors)
        self.fifth_toe = FifthToe(bone_ids=bone_ids, path_obj=path_obj, bone_names=bone_names, right=right, colors=colors)


class FirstToe:
    def __init__(self, bone_ids=None,  path_obj=None, bone_names=None, right=None, colors=None):
        self.proximal_phalanges = FirstProximal(bone_ids=bone_ids, path_obj=path_obj, bone_names=bone_names, right=right, colors=colors)
        self.distal_phalanges = FirstProximal(bone_ids=bone_ids, path_obj=path_obj, bone_names=bone_names, right=right, colors=colors)


class SecondToe:
    def __init__(self, bone_ids=None,  path_obj=None, bone_names=None, right=None, colors=None):
        self.proximal_phalanges = SecondProximal(bone_ids=bone_ids, path_obj=path_obj, bone_names=bone_names, right=right, colors=colors)
        self.intermediate_phalanges = SecondIntermediate(bone_ids=bone_ids, path_obj=path_obj, bone_names=bone_names, right=right, colors=colors)
        self.distal_phalanges = SecondDistal(bone_ids=bone_ids, path_obj=path_obj, bone_names=bone_names, right=right, colors=colors)


class ThirdToe:
    def __init__(self, bone_ids=None,  path_obj=None, bone_names=None, right=None, colors=None):
        self.proximal_phalanges = ThirdProximal(bone_ids=bone_ids, path_obj=path_obj, bone_names=bone_names, right=right, colors=colors)
        self.intermediate_phalanges = ThirdIntermediate(bone_ids=bone_ids, path_obj=path_obj, bone_names=bone_names, right=right, colors=colors)
        self.distal_phalanges = ThirdDistal(bone_ids=bone_ids, path_obj=path_obj, bone_names=bone_names, right=right, colors=colors)


class FourthToe:
    def __init__(self, bone_ids=None,  path_obj=None, bone_names=None, right=None, colors=None):
        self.proximal_phalanges = FourthProximal(bone_ids=bone_ids, path_obj=path_obj, bone_names=bone_names, right=right, colors=colors)
        self.intermediate_phalanges = FourthIntermediate(bone_ids=bone_ids, path_obj=path_obj, bone_names=bone_names, right=right, colors=colors)
        self.distal_phalanges = FourthDistal(bone_ids=bone_ids, path_obj=path_obj, bone_names=bone_names, right=right, colors=colors)


class FifthToe:
    def __init__(self, bone_ids=None,  path_obj=None, bone_names=None, right=None, colors=None):
        self.proximal_phalanges = FifthProximal(bone_ids=bone_ids, path_obj=path_obj, bone_names=bone_names, right=right, colors=colors)
        self.intermediate_phalanges = FifthIntermediate(bone_ids=bone_ids, path_obj=path_obj, bone_names=bone_names, right=right, colors=colors)
        self.distal_phalanges = FifthDistal(bone_ids=bone_ids, path_obj=path_obj, bone_names=bone_names, right=right, colors=colors)
