from data_models.anatomy.skeleton.leg.foot.tarsals import *
from data_models.anatomy.skeleton.leg.foot.metatarsal import *
from data_models.anatomy.skeleton.leg.foot.toes import Toes


class Foot:
    def __init__(self, bone_ids=None,  path_obj=None, bone_names=None, right=True, colors=None):
        self.tarsals = Tarsals(bone_ids=bone_ids, path_obj=path_obj, bone_names=bone_names, right=right, colors=colors)
        self.metatarsal = Metatarsal(bone_ids=bone_ids, path_obj=path_obj, bone_names=bone_names, right=right, colors=colors)
        self.toes = Toes(bone_ids=bone_ids, path_obj=path_obj, bone_names=bone_names, right=right, colors=colors)
