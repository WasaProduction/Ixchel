from data_models.anatomy.skeleton.thorax.rib_accessory import *
from data_models.anatomy.skeleton.thorax.rib_floating import *
from data_models.anatomy.skeleton.thorax.rib_rib_sternum import *
from data_models.anatomy.skeleton.thorax.rib_sternum import *
from data_models.anatomy.skeleton.thorax.sternum import *


class Thorax:
    def __init__(self, bone_ids=None,  path_obj=None, bone_names=None, colors=None):
        self.sternum = Sternum(bone_ids=bone_ids, path_obj=path_obj, bone_names=bone_names, colors=colors)
        """     Ribs        """
        #   Rib-accessory
        self.r_a01 = A1(bone_ids=bone_ids, path_obj=path_obj, bone_names=bone_names, right=True, colors=colors)
        self.l_a01 = A1(bone_ids=bone_ids, path_obj=path_obj, bone_names=bone_names, right=False, colors=colors)
        #   Rib-sternum
        self.r_t01 = T1(bone_ids=bone_ids, path_obj=path_obj, bone_names=bone_names, right=True, colors=colors)
        self.l_t01 = T1(bone_ids=bone_ids, path_obj=path_obj, bone_names=bone_names, right=False, colors=colors)
        self.r_t02 = T2(bone_ids=bone_ids, path_obj=path_obj, bone_names=bone_names, right=True, colors=colors)
        self.l_t02 = T2(bone_ids=bone_ids, path_obj=path_obj, bone_names=bone_names, right=False, colors=colors)
        self.r_t03 = T3(bone_ids=bone_ids, path_obj=path_obj, bone_names=bone_names, right=True, colors=colors)
        self.l_t03 = T3(bone_ids=bone_ids, path_obj=path_obj, bone_names=bone_names, right=False, colors=colors)
        self.r_t04 = T4(bone_ids=bone_ids, path_obj=path_obj, bone_names=bone_names, right=True, colors=colors)
        self.l_t04 = T4(bone_ids=bone_ids, path_obj=path_obj, bone_names=bone_names, right=False, colors=colors)
        self.r_t05 = T5(bone_ids=bone_ids, path_obj=path_obj, bone_names=bone_names, right=True, colors=colors)
        self.l_t05 = T5(bone_ids=bone_ids, path_obj=path_obj, bone_names=bone_names, right=False, colors=colors)
        self.r_t06 = T6(bone_ids=bone_ids, path_obj=path_obj, bone_names=bone_names, right=True, colors=colors)
        self.l_t06 = T6(bone_ids=bone_ids, path_obj=path_obj, bone_names=bone_names, right=False, colors=colors)
        self.r_t07 = T7(bone_ids=bone_ids, path_obj=path_obj, bone_names=bone_names, right=True, colors=colors)
        self.l_t07 = T7(bone_ids=bone_ids, path_obj=path_obj, bone_names=bone_names, right=False, colors=colors)
        #   Rib-rib-sternum
        self.r_t08 = T8(bone_ids=bone_ids, path_obj=path_obj, bone_names=bone_names, right=True, colors=colors)
        self.l_t08 = T8(bone_ids=bone_ids, path_obj=path_obj, bone_names=bone_names, right=False, colors=colors)
        self.r_t09 = T9(bone_ids=bone_ids, path_obj=path_obj, bone_names=bone_names, right=True, colors=colors)
        self.l_t09 = T9(bone_ids=bone_ids, path_obj=path_obj, bone_names=bone_names, right=False, colors=colors)
        self.r_t10 = T10(bone_ids=bone_ids, path_obj=path_obj, bone_names=bone_names, right=True, colors=colors)
        self.l_t10 = T10(bone_ids=bone_ids, path_obj=path_obj, bone_names=bone_names, right=False, colors=colors)
        #   Rib-floating
        self.r_t11 = T11(bone_ids=bone_ids, path_obj=path_obj, bone_names=bone_names, right=True, colors=colors)
        self.l_t11 = T11(bone_ids=bone_ids, path_obj=path_obj, bone_names=bone_names, right=False, colors=colors)
        self.r_t12 = T12(bone_ids=bone_ids, path_obj=path_obj, bone_names=bone_names, right=True, colors=colors)
        self.l_t12 = T12(bone_ids=bone_ids, path_obj=path_obj, bone_names=bone_names, right=False, colors=colors)
