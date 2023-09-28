from data_models.anatomy.skeleton.bone import Bone
"""
For carpals
"""


class Carpals:
    def __init__(self, bone_ids=None,  path_obj=None, bone_names=None, right=True, colors=None):
        self.scaphoid = Scaphoid(bone_ids=bone_ids, path_obj=path_obj, bone_names=bone_names, right=right, colors=colors)
        self.lunate = Lunate(bone_ids=bone_ids, path_obj=path_obj, bone_names=bone_names, right=right, colors=colors)
        self.triquetrum = Triquetrum(bone_ids=bone_ids, path_obj=path_obj, bone_names=bone_names, right=right, colors=colors)
        self.pisiform = Pisiform(bone_ids=bone_ids, path_obj=path_obj, bone_names=bone_names, right=right, colors=colors)
        self.trapezium = Trapezium(bone_ids=bone_ids, path_obj=path_obj, bone_names=bone_names, right=right, colors=colors)
        self.trapezoid = Trapezoid(bone_ids=bone_ids, path_obj=path_obj, bone_names=bone_names, right=right, colors=colors)
        self.capitate = Capitate(bone_ids=bone_ids, path_obj=path_obj, bone_names=bone_names, right=right, colors=colors)
        self.hamate = Hamate(bone_ids=bone_ids, path_obj=path_obj, bone_names=bone_names, right=right, colors=colors)
        self.right = right


class Scaphoid(Bone):
    def __init__(self, bone_ids=None,  path_obj=None, bone_names=None, right=True, colors=None):
        if right:
            super().__init__(bone_id=bone_ids.r_scaphoid, image_path=path_obj.r_scaphoid, name=bone_names.r_scaphoid, colors=colors)
        else:
            super().__init__(bone_id=bone_ids.l_scaphoid, image_path=path_obj.l_scaphoid, name=bone_names.l_scaphoid, colors=colors)
        self.right = right


class Lunate(Bone):
    def __init__(self, bone_ids=None,  path_obj=None, bone_names=None, right=True, colors=None):
        if right:
            super().__init__(bone_id=bone_ids.r_lunate, image_path=path_obj.r_lunate, name=bone_names.r_lunate, colors=colors)
        else:
            super().__init__(bone_id=bone_ids.l_lunate, image_path=path_obj.l_lunate, name=bone_names.l_lunate, colors=colors)
        self.right = right


class Triquetrum(Bone):
    def __init__(self, bone_ids=None,  path_obj=None, bone_names=None, right=True, colors=None):
        if right:
            super().__init__(bone_id=bone_ids.r_triquetrum, image_path=path_obj.r_triquetrum, name=bone_names.r_triquetrum, colors=colors)
        else:
            super().__init__(bone_id=bone_ids.l_triquetrum, image_path=path_obj.l_triquetrum, name=bone_names.l_triquetrum, colors=colors)
        self.right = right


class Pisiform(Bone):
    def __init__(self, bone_ids=None,  path_obj=None, bone_names=None, right=True, colors=None):
        if right:
            super().__init__(bone_id=bone_ids.r_pisiform, image_path=path_obj.r_pisiform, name=bone_names.r_pisiform, colors=colors)
        else:
            super().__init__(bone_id=bone_ids.l_pisiform, image_path=path_obj.l_pisiform, name=bone_names.l_pisiform, colors=colors)
        self.right = right


class Trapezium(Bone):
    def __init__(self, bone_ids=None,  path_obj=None, bone_names=None, right=True, colors=None):
        if right:
            super().__init__(bone_id=bone_ids.r_trapezium, image_path=path_obj.r_trapezium, name=bone_names.r_trapezium, colors=colors)
        else:
            super().__init__(bone_id=bone_ids.l_trapezium, image_path=path_obj.l_trapezium, name=bone_names.l_trapezium, colors=colors)
        self.right = right


class Trapezoid(Bone):
    def __init__(self, bone_ids=None,  path_obj=None, bone_names=None, right=True, colors=None):
        if right:
            super().__init__(bone_id=bone_ids.r_trapezoid, image_path=path_obj.r_trapezoid, name=bone_names.r_trapezoid, colors=colors)
        else:
            super().__init__(bone_id=bone_ids.l_trapezoid, image_path=path_obj.l_trapezoid, name=bone_names.l_trapezoid, colors=colors)
        self.right = right


class Capitate(Bone):
    def __init__(self, bone_ids=None,  path_obj=None, bone_names=None, right=True, colors=None):
        if right:
            super().__init__(bone_id=bone_ids.r_capitate, image_path=path_obj.r_capitate, name=bone_names.r_capitate, colors=colors)
        else:
            super().__init__(bone_id=bone_ids.l_capitate, image_path=path_obj.l_capitate, name=bone_names.l_capitate, colors=colors)
        self.right = right


class Hamate(Bone):
    def __init__(self, bone_ids=None,  path_obj=None, bone_names=None, right=True, colors=None):
        if right:
            super().__init__(bone_id=bone_ids.r_hamate, image_path=path_obj.r_hamate, name=bone_names.r_hamate, colors=colors)
        else:
            super().__init__(bone_id=bone_ids.l_hamate, image_path=path_obj.l_hamate, name=bone_names.l_hamate, colors=colors)
        self.right = right
