from data_models.anatomy.skeleton.bone import Bone
"""
For tarsals
"""


class Tarsals:
    def __init__(self, bone_ids=None,  path_obj=None, bone_names=None, right=None):
        self.calcaneus = Calcaneus(bone_ids=bone_ids, path_obj=path_obj, bone_names=bone_names, right=right)
        self.talus = Talus(bone_ids=bone_ids, path_obj=path_obj, bone_names=bone_names, right=right)
        self.navicular = Navicular(bone_ids=bone_ids, path_obj=path_obj, bone_names=bone_names, right=right)
        self.medial_cuneiform = MedialCuneiform(bone_ids=bone_ids, path_obj=path_obj, bone_names=bone_names, right=right)
        self.intermediate_cuneiform = IntermediateCuneiform(bone_ids=bone_ids, path_obj=path_obj, bone_names=bone_names, right=right)
        self.lateral_cuneiform = LateralCuneiform(bone_ids=bone_ids, path_obj=path_obj, bone_names=bone_names, right=right)
        self.cuboid = Cuboid(bone_ids=bone_ids, path_obj=path_obj, bone_names=bone_names, right=right)


class Calcaneus(Bone):
    def __init__(self, bone_ids=None,  path_obj=None, bone_names=None, right=True):
        if right:
            super().__init__(bone_id=bone_ids.r_calcaneus, image_path=path_obj.r_calcaneus, name=bone_names.r_calcaneus)
        else:
            super().__init__(bone_id=bone_ids.l_calcaneus, image_path=path_obj.l_calcaneus, name=bone_names.l_calcaneus)


class Talus(Bone):
    def __init__(self, bone_ids=None,  path_obj=None, bone_names=None, right=True):
        if right:
            super().__init__(bone_id=bone_ids.r_talus, image_path=path_obj.r_talus, name=bone_names.r_talus)
        else:
            super().__init__(bone_id=bone_ids.l_talus, image_path=path_obj.l_talus, name=bone_names.l_talus)


class Navicular(Bone):
    def __init__(self, bone_ids=None,  path_obj=None, bone_names=None, right=True):
        if right:
            super().__init__(bone_id=bone_ids.r_navicular, image_path=path_obj.r_navicular, name=bone_names.r_navicular)
        else:
            super().__init__(bone_id=bone_ids.l_navicular, image_path=path_obj.l_navicular, name=bone_names.l_navicular)


class MedialCuneiform(Bone):
    def __init__(self, bone_ids=None,  path_obj=None, bone_names=None, right=True):
        if right:
            super().__init__(bone_id=bone_ids.r_medial_cuneiform, image_path=path_obj.r_medial_cuneiform, name=bone_names.r_medial_cuneiform)
        else:
            super().__init__(bone_id=bone_ids.l_medial_cuneiform, image_path=path_obj.l_medial_cuneiform, name=bone_names.l_medial_cuneiform)


class IntermediateCuneiform(Bone):
    def __init__(self, bone_ids=None,  path_obj=None, bone_names=None, right=True):
        if right:
            super().__init__(bone_id=bone_ids.r_intermediate_cuneiform, image_path=path_obj.r_intermediate_cuneiform, name=bone_names.r_intermediate_cuneiform)
        else:
            super().__init__(bone_id=bone_ids.l_intermediate_cuneiform, image_path=path_obj.l_intermediate_cuneiform, name=bone_names.l_intermediate_cuneiform)


class LateralCuneiform(Bone):
    def __init__(self, bone_ids=None,  path_obj=None, bone_names=None, right=True):
        if right:
            super().__init__(bone_id=bone_ids.r_lateral_cuneiform, image_path=path_obj.r_lateral_cuneiform, name=bone_names.r_lateral_cuneiform)
        else:
            super().__init__(bone_id=bone_ids.l_lateral_cuneiform, image_path=path_obj.l_lateral_cuneiform, name=bone_names.l_lateral_cuneiform)


class Cuboid(Bone):
    def __init__(self, bone_ids=None,  path_obj=None, bone_names=None, right=True):
        if right:
            super().__init__(bone_id=bone_ids.r_cuboid, image_path=path_obj.r_cuboid, name=bone_names.r_cuboid)
        else:
            super().__init__(bone_id=bone_ids.l_cuboid, image_path=path_obj.l_cuboid, name=bone_names.l_cuboid)
