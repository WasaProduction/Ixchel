from data_models.anatomy.skeleton.bone import Bone
"""
For Phalanges
Classes:
    TProximal, IProximal, MProximal, RProximal, PProximal,  
    IIntermediate, MIntermediate, PIntermediate
    TDistal, IDistal, MDistal, RDistal, PDistal

Nomenclature:
    Class:
        First letter of the finger + _ + Proximal || Intermediate || Distal
    Image:
        First letter of left/right + _ + First letter of the finger + _ + Proximal || Intermediate || Distal
"""


"""     Thumb       """


class TProximal(Bone):
    def __init__(self, bone_ids=None,  path_obj=None, bone_names=None, right=True):
        if right:
            super().__init__(bone_id=bone_ids.r_t_phalanx_proximal, image_path=path_obj.r_t_phalanx_proximal, name=bone_names.r_t_phalanx_proximal)
        else:
            super().__init__(bone_id=bone_ids.l_t_phalanx_proximal, image_path=path_obj.l_t_phalanx_proximal, name=bone_names.l_t_phalanx_proximal)
        self.right = right


class TDistal(Bone):
    def __init__(self, bone_ids=None,  path_obj=None, bone_names=None, right=True):
        if right:
            super().__init__(bone_id=bone_ids.r_t_phalanx_distal, image_path=path_obj.r_t_phalanx_distal, name=bone_names.r_t_phalanx_distal)
        else:
            super().__init__(bone_id=bone_ids.l_t_phalanx_distal, image_path=path_obj.l_t_phalanx_distal, name=bone_names.l_t_phalanx_distal)
        self.right = right


"""     Index       """


class IProximal(Bone):
    def __init__(self, bone_ids=None,  path_obj=None, bone_names=None, right=True):
        if right:
            super().__init__(bone_id=bone_ids.r_i_phalanx_proximal, image_path=path_obj.r_i_phalanx_proximal, name=bone_names.r_i_phalanx_proximal)
        else:
            super().__init__(bone_id=bone_ids.l_i_phalanx_proximal, image_path=path_obj.l_i_phalanx_proximal, name=bone_names.l_i_phalanx_proximal)
        self.right = right


class IIntermediate(Bone):
    def __init__(self, bone_ids=None,  path_obj=None, bone_names=None, right=True):
        if right:
            super().__init__(bone_id=bone_ids.r_i_phalanx_intermediate, image_path=path_obj.r_i_phalanx_intermediate, name=bone_names.r_i_phalanx_intermediate)
        else:
            super().__init__(bone_id=bone_ids.l_i_phalanx_intermediate, image_path=path_obj.l_i_phalanx_intermediate, name=bone_names.l_i_phalanx_intermediate)
        self.right = right


class IDistal(Bone):
    def __init__(self, bone_ids=None,  path_obj=None, bone_names=None, right=True):
        if right:
            super().__init__(bone_id=bone_ids.r_i_phalanx_distal, image_path=path_obj.r_i_phalanx_distal, name=bone_names.r_i_phalanx_distal)
        else:
            super().__init__(bone_id=bone_ids.l_i_phalanx_distal, image_path=path_obj.l_i_phalanx_distal, name=bone_names.l_i_phalanx_distal)
        self.right = right


"""     Middle      """


class MProximal(Bone):
    def __init__(self, bone_ids=None,  path_obj=None, bone_names=None, right=True):
        if right:
            super().__init__(bone_id=bone_ids.r_m_phalanx_proximal, image_path=path_obj.r_m_phalanx_proximal, name=bone_names.r_m_phalanx_proximal)
        else:
            super().__init__(bone_id=bone_ids.l_m_phalanx_proximal, image_path=path_obj.l_m_phalanx_proximal, name=bone_names.l_m_phalanx_proximal)
        self.right = right


class MIntermediate(Bone):
    def __init__(self, bone_ids=None,  path_obj=None, bone_names=None, right=True):
        if right:
            super().__init__(bone_id=bone_ids.r_m_phalanx_intermediate, image_path=path_obj.r_m_phalanx_intermediate, name=bone_names.r_m_phalanx_intermediate)
        else:
            super().__init__(bone_id=bone_ids.l_m_phalanx_intermediate, image_path=path_obj.l_m_phalanx_intermediate, name=bone_names.l_m_phalanx_intermediate)
        self.right = right


class MDistal(Bone):
    def __init__(self, bone_ids=None,  path_obj=None, bone_names=None, right=True):
        if right:
            super().__init__(bone_id=bone_ids.r_m_phalanx_distal, image_path=path_obj.r_m_phalanx_distal, name=bone_names.r_m_phalanx_distal)
        else:
            super().__init__(bone_id=bone_ids.l_m_phalanx_distal, image_path=path_obj.l_m_phalanx_distal, name=bone_names.l_m_phalanx_distal)
        self.right = right


"""     Ring        """


class RProximal(Bone):
    def __init__(self, bone_ids=None,  path_obj=None, bone_names=None, right=True):
        if right:
            super().__init__(bone_id=bone_ids.r_r_phalanx_proximal, image_path=path_obj.r_r_phalanx_proximal, name=bone_names.r_r_phalanx_proximal)
        else:
            super().__init__(bone_id=bone_ids.l_r_phalanx_proximal, image_path=path_obj.l_r_phalanx_proximal, name=bone_names.l_r_phalanx_proximal)
        self.right = right


class RIntermediate(Bone):
    def __init__(self, bone_ids=None,  path_obj=None, bone_names=None, right=True):
        if right:
            super().__init__(bone_id=bone_ids.r_r_phalanx_intermediate, image_path=path_obj.r_r_phalanx_intermediate, name=bone_names.r_r_phalanx_intermediate)
        else:
            super().__init__(bone_id=bone_ids.l_r_phalanx_intermediate, image_path=path_obj.l_r_phalanx_intermediate, name=bone_names.l_r_phalanx_intermediate)
        self.right = right


class RDistal(Bone):
    def __init__(self, bone_ids=None,  path_obj=None, bone_names=None, right=True):
        if right:
            super().__init__(bone_id=bone_ids.r_r_phalanx_distal, image_path=path_obj.r_r_phalanx_distal, name=bone_names.r_r_phalanx_distal)
        else:
            super().__init__(bone_id=bone_ids.l_r_phalanx_distal, image_path=path_obj.l_r_phalanx_distal, name=bone_names.l_r_phalanx_distal)
        self.right = right


"""     Pinky       """


class PProximal(Bone):
    def __init__(self, bone_ids=None,  path_obj=None, bone_names=None, right=True):
        if right:
            super().__init__(bone_id=bone_ids.r_p_phalanx_proximal, image_path=path_obj.r_p_phalanx_proximal, name=bone_names.r_p_phalanx_proximal)
        else:
            super().__init__(bone_id=bone_ids.l_p_phalanx_proximal, image_path=path_obj.l_p_phalanx_proximal, name=bone_names.l_p_phalanx_proximal)
        self.right = right


class PIntermediate(Bone):
    def __init__(self, bone_ids=None,  path_obj=None, bone_names=None, right=True):
        if right:
            super().__init__(bone_id=bone_ids.r_p_phalanx_intermediate, image_path=path_obj.r_p_phalanx_intermediate, name=bone_names.r_p_phalanx_intermediate)
        else:
            super().__init__(bone_id=bone_ids.l_p_phalanx_intermediate, image_path=path_obj.l_p_phalanx_intermediate, name=bone_names.l_p_phalanx_intermediate)
        self.right = right


class PDistal(Bone):
    def __init__(self, bone_ids=None,  path_obj=None, bone_names=None, right=True):
        if right:
            super().__init__(bone_id=bone_ids.r_p_phalanx_distal, image_path=path_obj.r_p_phalanx_distal, name=bone_names.r_p_phalanx_distal)
        else:
            super().__init__(bone_id=bone_ids.l_p_phalanx_distal, image_path=path_obj.l_p_phalanx_distal, name=bone_names.l_p_phalanx_distal)
        self.right = right
