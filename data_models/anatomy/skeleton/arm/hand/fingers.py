from data_models.anatomy.skeleton.arm.hand.phalanges import *
"""
For fingers
"""


class Fingers:
    def __init__(self, bone_ids=None,  path_obj=None, bone_names=None, right=True, colors=None):
        self.thumb = Thumb(bone_ids=bone_ids, path_obj=path_obj, bone_names=bone_names, right=right, colors=colors)
        self.index = Index(bone_ids=bone_ids, path_obj=path_obj, bone_names=bone_names,  right=right, colors=colors)
        self.middle = Middle(bone_ids=bone_ids, path_obj=path_obj, bone_names=bone_names,  right=right, colors=colors)
        self.ring = Ring(bone_ids=bone_ids, path_obj=path_obj, bone_names=bone_names,  right=right, colors=colors)
        self.pinky = Pinky(bone_ids=bone_ids, path_obj=path_obj, bone_names=bone_names,  right=right, colors=colors)


"""
    Phalanges
    First letter of the finger + Proximal || Intermediate || Distal
"""


class Thumb:
    def __init__(self, bone_ids=None,  path_obj=None, bone_names=None, right=True, colors=None):
        self.proximal_phalanges = TProximal(bone_ids=bone_ids,  path_obj=path_obj, bone_names=bone_names, right=right, colors=colors)
        self.distal_phalanges = TDistal(bone_ids=bone_ids,  path_obj=path_obj, bone_names=bone_names, right=right, colors=colors)
        self.path_obj = path_obj
        self.bone_names = bone_names
        self.right = right


class Index:
    def __init__(self, bone_ids=None,  path_obj=None, bone_names=None, right=True, colors=None):
        self.proximal_phalanges = IProximal(bone_ids=bone_ids,  path_obj=path_obj, bone_names=bone_names, right=right, colors=colors)
        self.intermediate_phalanges = IIntermediate(bone_ids=bone_ids,  path_obj=path_obj, bone_names=bone_names, right=right, colors=colors)
        self.distal_phalanges = IDistal(bone_ids=bone_ids,  path_obj=path_obj, bone_names=bone_names, right=right, colors=colors)
        self.path_obj = path_obj
        self.bone_names = bone_names
        self.right = right


class Middle:
    def __init__(self, bone_ids=None,  path_obj=None, bone_names=None, right=True, colors=None):
        self.proximal_phalanges = MProximal(bone_ids=bone_ids,  path_obj=path_obj, bone_names=bone_names, right=right, colors=colors)
        self.intermediate_phalanges = MIntermediate(bone_ids=bone_ids,  path_obj=path_obj, bone_names=bone_names, right=right, colors=colors)
        self.distal_phalanges = MDistal(bone_ids=bone_ids,  path_obj=path_obj, bone_names=bone_names, right=right, colors=colors)
        self.path_obj = path_obj
        self.bone_names = bone_names
        self.right = right


class Ring:
    def __init__(self, bone_ids=None,  path_obj=None, bone_names=None, right=True, colors=None):
        self.proximal_phalanges = RProximal(bone_ids=bone_ids,  path_obj=path_obj, bone_names=bone_names, right=right, colors=colors)
        self.intermediate_phalanges = RIntermediate(bone_ids=bone_ids,  path_obj=path_obj, bone_names=bone_names, right=right, colors=colors)
        self.distal_phalanges = RDistal(bone_ids=bone_ids,  path_obj=path_obj, bone_names=bone_names, right=right, colors=colors)
        self.path_obj = path_obj
        self.bone_names = bone_names
        self.right = right


class Pinky:
    def __init__(self, bone_ids=None,  path_obj=None, bone_names=None, right=True, colors=None):
        self.proximal_phalanges = PProximal(bone_ids=bone_ids,  path_obj=path_obj, bone_names=bone_names, right=right, colors=colors)
        self.intermediate_phalanges = PIntermediate(bone_ids=bone_ids,  path_obj=path_obj, bone_names=bone_names, right=right, colors=colors)
        self.distal_phalanges = PDistal(bone_ids=bone_ids,  path_obj=path_obj, bone_names=bone_names, right=right, colors=colors)
        self.path_obj = path_obj
        self.bone_names = bone_names
        self.right = right
