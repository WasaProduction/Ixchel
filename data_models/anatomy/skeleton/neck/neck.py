from data_models.anatomy.skeleton.bone import Bone


class Hyoid(Bone):
    def __init__(self, bone_ids=None,  path_obj=None, bone_names=None):
        super().__init__(bone_id=bone_ids.hyoid, image_path=path_obj.hyoid, name=bone_names.hyoid)
