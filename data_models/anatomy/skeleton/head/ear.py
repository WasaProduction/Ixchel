from data_models.anatomy.skeleton.bone import Bone


class Ear:
    def __init__(self, bone_ids=None,  path_obj=None, right=True, bone_names=None, colors=None):
        self.right = right
        self.malleus = Malleus(bone_ids=bone_ids, path_obj=path_obj, bone_names=bone_names, right=self.right, colors=colors)
        self.incus = Incus(bone_ids=bone_ids, path_obj=path_obj, bone_names=bone_names, right=self.right, colors=colors)
        self.stapes = Stapes(bone_ids=bone_ids, path_obj=path_obj, bone_names=bone_names, right=self.right, colors=colors)


class Malleus(Bone):
    def __init__(self, bone_ids=None,  path_obj=None, bone_names=None, right=True, colors=None):
        if right:
            super().__init__(bone_id=bone_ids.r_ear_malleus, image_path=path_obj.r_ear_malleus, name=bone_names.r_ear_malleus, colors=colors)
        else:
            super().__init__(bone_id=bone_ids.l_ear_malleus, image_path=path_obj.l_ear_malleus, name=bone_names.l_ear_malleus, colors=colors)
        self.right = right


class Incus(Bone):
    def __init__(self, bone_ids=None,  path_obj=None, bone_names=None, right=True, colors=None):
        if right:
            super().__init__(bone_id=bone_ids.r_ear_incus, image_path=path_obj.r_ear_incus, name=bone_names.r_ear_incus, colors=colors)
        else:
            super().__init__(bone_id=bone_ids.l_ear_incus, image_path=path_obj.l_ear_incus, name=bone_names.l_ear_incus, colors=colors)
        self.right = right


class Stapes(Bone):
    def __init__(self, bone_ids=None,  path_obj=None, bone_names=None, right=True, colors=None):
        if right:
            super().__init__(bone_id=bone_ids.r_ear_stapes, image_path=path_obj.r_ear_stapes, name=bone_names.r_ear_stapes, colors=colors)
        else:
            super().__init__(bone_id=bone_ids.l_ear_stapes, image_path=path_obj.l_ear_stapes, name=bone_names.l_ear_stapes, colors=colors)
        self.right = right
