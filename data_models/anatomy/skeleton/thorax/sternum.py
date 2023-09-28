from data_models.anatomy.skeleton.bone import Bone


class Sternum(Bone):
    def __init__(self, bone_ids=None,  path_obj=None, bone_names=None, colors=None):
        super().__init__(bone_id=bone_ids.sternum, image_path=path_obj.sternum, name=bone_names.sternum, colors=colors)

