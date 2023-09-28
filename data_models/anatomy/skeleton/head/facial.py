from data_models.anatomy.skeleton.bone import Bone


class Facial:
    def __init__(self, bone_ids=None,  path_obj=None, bone_names=None, colors=None):
        self.mandible = Mandible(bone_ids=bone_ids, path_obj=path_obj, bone_names=bone_names, colors=colors)
        self.right_maxilla = Maxilla(bone_ids=bone_ids, path_obj=path_obj, bone_names=bone_names, right=True, colors=colors)
        self.left_maxilla = Maxilla(bone_ids=bone_ids, path_obj=path_obj, bone_names=bone_names, right=False, colors=colors)
        self.right_palatine = Palatine(bone_ids=bone_ids, path_obj=path_obj, bone_names=bone_names, right=True, colors=colors)
        self.left_palatine = Palatine(bone_ids=bone_ids, path_obj=path_obj, bone_names=bone_names, right=False, colors=colors)
        self.right_zygomatic = Zygomatic(bone_ids=bone_ids, path_obj=path_obj, bone_names=bone_names, right=True, colors=colors)
        self.left_zygomatic = Zygomatic(bone_ids=bone_ids, path_obj=path_obj, bone_names=bone_names, right=False, colors=colors)
        self.right_nasal = Nasal(bone_ids=bone_ids, path_obj=path_obj, bone_names=bone_names, right=True, colors=colors)
        self.left_nasal = Nasal(bone_ids=bone_ids, path_obj=path_obj, bone_names=bone_names, right=False, colors=colors)
        self.right_lacrimal = Lacrimal(bone_ids=bone_ids, path_obj=path_obj, bone_names=bone_names, right=True, colors=colors)
        self.left_lacrimal = Lacrimal(bone_ids=bone_ids, path_obj=path_obj, bone_names=bone_names, right=False, colors=colors)
        self.vomer = Vomer(bone_ids=bone_ids, path_obj=path_obj, bone_names=bone_names, colors=colors)
        self.right_inferior_nasal_conchae = InferiorNasalConchae(bone_ids=bone_ids, path_obj=path_obj, bone_names=bone_names, right=True, colors=colors)
        self.left_inferior_nasal_conchae = InferiorNasalConchae(bone_ids=bone_ids, path_obj=path_obj, bone_names=bone_names, right=False, colors=colors)


class Mandible(Bone):
    def __init__(self, bone_ids=None,  path_obj=None, bone_names=None, colors=None):
        super().__init__(bone_id=bone_ids.facial_mandible, image_path=path_obj.facial_mandible, name=bone_names.facial_mandible, colors=colors)


class Maxilla(Bone):
    def __init__(self, bone_ids=None,  path_obj=None, bone_names=None, right=True, colors=None):
        if right:
            super().__init__(bone_id=bone_ids.facial_r_maxilla, image_path=path_obj.facial_r_maxilla, name=bone_names.facial_r_maxilla, colors=colors)
        else:
            super().__init__(bone_id=bone_ids.facial_l_maxilla, image_path=path_obj.facial_l_maxilla, name=bone_names.facial_l_maxilla, colors=colors)
        self.right = right


class Palatine(Bone):
    def __init__(self, bone_ids=None,  path_obj=None, bone_names=None, right=True, colors=None):
        if right:
            super().__init__(bone_id=bone_ids.facial_r_palatine, image_path=path_obj.facial_r_palatine, name=bone_names.facial_r_palatine, colors=colors)
        else:
            super().__init__(bone_id=bone_ids.facial_l_palatine, image_path=path_obj.facial_l_palatine, name=bone_names.facial_l_palatine, colors=colors)
        self.right = right


class Zygomatic(Bone):
    def __init__(self, bone_ids=None,  path_obj=None, bone_names=None, right=True, colors=None):
        if right:
            super().__init__(bone_id=bone_ids.facial_r_zygomatic, image_path=path_obj.facial_r_zygomatic, name=bone_names.facial_r_zygomatic, colors=colors)
        else:
            super().__init__(bone_id=bone_ids.facial_l_zygomatic, image_path=path_obj.facial_l_zygomatic, name=bone_names.facial_l_zygomatic, colors=colors)
        self.right = right


class Nasal(Bone):
    def __init__(self, bone_ids=None,  path_obj=None, bone_names=None, right=True, colors=None):
        if right:
            super().__init__(bone_id=bone_ids.facial_r_nasal, image_path=path_obj.facial_r_nasal, name=bone_names.facial_r_nasal, colors=colors)
        else:
            super().__init__(bone_id=bone_ids.facial_l_nasal, image_path=path_obj.facial_l_nasal, name=bone_names.facial_l_nasal, colors=colors)
        self.right = right


class Lacrimal(Bone):
    def __init__(self, bone_ids=None,  path_obj=None, bone_names=None, right=True, colors=None):
        if right:
            super().__init__(bone_id=bone_ids.facial_r_lacrimal, image_path=path_obj.facial_r_lacrimal, name=bone_names.facial_r_lacrimal, colors=colors)
        else:
            super().__init__(bone_id=bone_ids.facial_l_lacrimal, image_path=path_obj.facial_l_lacrimal, name=bone_names.facial_l_lacrimal, colors=colors)
        self.right = right


class Vomer(Bone):
    def __init__(self, bone_ids=None,  path_obj=None, bone_names=None, colors=None):
        super().__init__(bone_id=bone_ids.facial_vomer, image_path=path_obj.facial_vomer, name=bone_names.facial_vomer, colors=colors)


class InferiorNasalConchae(Bone):
    def __init__(self, bone_ids=None,  path_obj=None, bone_names=None, right=True, colors=None):
        if right:
            super().__init__(bone_id=bone_ids.facial_r_inferior_nasal_conchae, image_path=path_obj.facial_r_inferior_nasal_conchae, name=bone_names.facial_r_inferior_nasal_conchae, colors=colors)
        else:
            super().__init__(bone_id=bone_ids.facial_l_inferior_nasal_conchae, image_path=path_obj.facial_l_inferior_nasal_conchae, name=bone_names.facial_l_inferior_nasal_conchae, colors=colors)
        self.right = right
