from data_models.anatomy.skeleton.bone import Bone


class Cranium:
    def __init__(self, bone_ids=None,  path_obj=None, bone_names=None):
        self.frontal = Frontal(bone_ids=bone_ids, path_obj=path_obj, bone_names=bone_names)
        self.left_parietal = Parietal(bone_ids=bone_ids, path_obj=path_obj, bone_names=bone_names, right=False)
        self.right_parietal = Parietal(bone_ids=bone_ids, path_obj=path_obj, bone_names=bone_names, right=True)
        self.left_temporal = Temporal(bone_ids=bone_ids, path_obj=path_obj, bone_names=bone_names, right=False)
        self.right_temporal = Temporal(bone_ids=bone_ids, path_obj=path_obj, bone_names=bone_names, right=True)
        self.occipital = Occipital(bone_ids=bone_ids, path_obj=path_obj, bone_names=bone_names)
        self.sphenoid = Sphenoid(bone_ids=bone_ids, path_obj=path_obj, bone_names=bone_names)
        self.ethmoid = Ethmoid(bone_ids=bone_ids, path_obj=path_obj, bone_names=bone_names)


class Frontal(Bone):
    def __init__(self, bone_ids=None,  path_obj=None, bone_names=None):
        super().__init__(bone_id=bone_ids.cranium_frontal, image_path=path_obj.cranium_frontal, name=bone_names.cranium_frontal)


class Parietal(Bone):
    def __init__(self, bone_ids=None,  path_obj=None, bone_names=None, right=True):
        if right:
            super().__init__(bone_id=bone_ids.cranium_r_parietal, image_path=path_obj.cranium_r_parietal, name=bone_names.cranium_r_parietal)
        else:
            super().__init__(bone_id=bone_ids.cranium_l_parietal, image_path=path_obj.cranium_l_parietal, name=bone_names.cranium_l_parietal)
        self.right = right


class Temporal(Bone):
    def __init__(self, bone_ids=None,  path_obj=None, bone_names=None, right=True):
        if right:
            super().__init__(bone_id=bone_ids.cranium_r_temporal, image_path=path_obj.cranium_r_temporal, name=bone_names.cranium_r_temporal)
        else:
            super().__init__(bone_id=bone_ids.cranium_l_temporal, image_path=path_obj.cranium_l_temporal, name=bone_names.cranium_l_temporal)
        self.right = right


class Occipital(Bone):
    def __init__(self, bone_ids=None,  path_obj=None, bone_names=None):
        super().__init__(bone_id=bone_ids.cranium_occipital, image_path=path_obj.cranium_occipital, name=bone_names.cranium_occipital)


class Sphenoid(Bone):
    def __init__(self, bone_ids=None,  path_obj=None, bone_names=None):
        super().__init__(bone_id=bone_ids.cranium_sphenoid, image_path=path_obj.cranium_sphenoid, name=bone_names.cranium_sphenoid)


class Ethmoid(Bone):
    def __init__(self, bone_ids=None,  path_obj=None, bone_names=None):
        super().__init__(bone_id=bone_ids.cranium_ethmoid, image_path=path_obj.cranium_ethmoid, name=bone_names.cranium_ethmoid)
