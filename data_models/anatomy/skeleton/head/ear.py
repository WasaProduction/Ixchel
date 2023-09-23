from data_models.anatomy.skeleton.bone import Bone


class Ear:
    def __init__(self, bone_ids=None,  path_obj=None, right=True, bone_names=None):
        self.right = right
        self.malleus = Malleus(bone_ids=bone_ids, path_obj=path_obj, bone_names=bone_names, right=self.right)
        self.incus = Incus(bone_ids=bone_ids, path_obj=path_obj, bone_names=bone_names, right=self.right)
        self.stapes = Stapes(bone_ids=bone_ids, path_obj=path_obj, bone_names=bone_names, right=self.right)


class Malleus(Bone):
    def __init__(self, bone_ids=None,  path_obj=None, bone_names=None, right=True):
        if right:
            super().__init__(bone_id=bone_ids.r_ear_malleus, image_path=path_obj.r_ear_malleus, name=bone_names.r_ear_malleus)
        else:
            super().__init__(bone_id=bone_ids.l_ear_malleus, image_path=path_obj.l_ear_malleus, name=bone_names.l_ear_malleus)
        self.right = right


class Incus(Bone):
    def __init__(self, bone_ids=None,  path_obj=None, bone_names=None, right=True):
        if right:
            super().__init__(bone_id=bone_ids.r_ear_incus, image_path=path_obj.r_ear_incus, name=bone_names.r_ear_incus)
        else:
            super().__init__(bone_id=bone_ids.l_ear_incus, image_path=path_obj.l_ear_incus, name=bone_names.l_ear_incus)
        self.right = right


class Stapes(Bone):
    def __init__(self, bone_ids=None,  path_obj=None, bone_names=None, right=True):
        if right:
            super().__init__(bone_id=bone_ids.r_ear_stapes, image_path=path_obj.r_ear_stapes, name=bone_names.r_ear_stapes)
        else:
            super().__init__(bone_id=bone_ids.l_ear_stapes, image_path=path_obj.l_ear_stapes, name=bone_names.l_ear_stapes)
        self.right = right
