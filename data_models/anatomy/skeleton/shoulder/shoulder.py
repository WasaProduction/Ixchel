from data_models.anatomy.skeleton.bone import Bone


class Omoplatae(Bone):
    def __init__(self, bone_ids=None,  path_obj=None, bone_names=None, right=True, colors=None):
        if right:
            super().__init__(bone_id=bone_ids.r_omoplatae, image_path=path_obj.r_omoplatae, name=bone_names.r_omoplatae,
                             colors=colors)
        else:
            super().__init__(bone_id=bone_ids.l_omoplatae, image_path=path_obj.l_omoplatae, name=bone_names.l_omoplatae,
                             colors=colors)
        self.right = right


class Clavicle(Bone):
    def __init__(self, bone_ids=None,  path_obj=None, bone_names=None, right=True, colors=None):
        if right:
            super().__init__(bone_id=bone_ids.r_clavicle, image_path=path_obj.r_clavicle, name=bone_names.r_clavicle,
                             colors=colors)
        else:
            super().__init__(bone_id=bone_ids.l_clavicle, image_path=path_obj.l_clavicle, name=bone_names.l_clavicle,
                             colors=colors)
        self.right = right
