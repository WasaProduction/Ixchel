from assets.anatomy_pixmaps.skeleton.skeleton_paths import SkeletonPaths
from data_models.anatomy.skeleton.head.cranium import Cranium
from data_models.anatomy.skeleton.head.ear import Ear
from data_models.anatomy.skeleton.head.facial import Facial
from data_models.anatomy.skeleton.thorax.thorax import Thorax
from data_models.anatomy.skeleton.pelvis.pelvis import *
from data_models.anatomy.skeleton.neck.neck import Hyoid
from data_models.anatomy.skeleton.vertebrae.vertebrae import Vertebrae
from data_models.anatomy.skeleton.shoulder.shoulder import *
from data_models.anatomy.skeleton.arm.arm import Arm
from data_models.anatomy.skeleton.leg.leg import Leg
from mongodb.read.get_bone_names import GetBoneNames
from mongodb.read.get_bone_ids import GetBoneIds


class FullSkeleton:
    def __init__(self):
        image_paths = SkeletonPaths()
        bone_names = GetBoneNames(language=1)
        bone_ids = GetBoneIds()
        """     Head        """
        self.cranium = Cranium(bone_ids=bone_ids, path_obj=image_paths, bone_names=bone_names)
        self.right_ear = Ear(bone_ids=bone_ids, path_obj=image_paths, bone_names=bone_names, right=True)
        self.left_ear = Ear(bone_ids=bone_ids, path_obj=image_paths, bone_names=bone_names, right=False)
        self.facial = Facial(bone_ids=bone_ids, path_obj=image_paths, bone_names=bone_names)
        """     Neck        """
        self.hyoid = Hyoid(bone_ids=bone_ids, path_obj=image_paths, bone_names=bone_names)
        """     Thorax      """
        self.thorax = Thorax(bone_ids=bone_ids, path_obj=image_paths, bone_names=bone_names)
        """     Vertebrae   """
        self.vertebrae = Vertebrae(bone_ids=bone_ids, path_obj=image_paths, bone_names=bone_names)
        """     Shoulder    """
        self.r_omoplatae = Omoplatae(bone_ids=bone_ids, path_obj=image_paths, bone_names=bone_names, right=True)
        self.l_omoplatae = Omoplatae(bone_ids=bone_ids, path_obj=image_paths, bone_names=bone_names, right=False)
        self.r_clavicle = Clavicle(bone_ids=bone_ids, path_obj=image_paths, bone_names=bone_names, right=True)
        self.l_clavicle = Clavicle(bone_ids=bone_ids, path_obj=image_paths, bone_names=bone_names, right=False)
        """     Arms        """
        self.r_arm = Arm(bone_ids=bone_ids, path_obj=image_paths, bone_names=bone_names, right=False)
        self.l_arm = Arm(bone_ids=bone_ids, path_obj=image_paths, bone_names=bone_names, right=False)
        """     Pelvis      """
        self.sacrum = Sacrum(bone_ids=bone_ids, path_obj=image_paths, bone_names=bone_names)
        self.coccyx = Coccyx(bone_ids=bone_ids, path_obj=image_paths, bone_names=bone_names)
        self.r_hip = Hip(bone_ids=bone_ids, path_obj=image_paths, bone_names=bone_names, right=True)
        self.l_hip = Hip(bone_ids=bone_ids, path_obj=image_paths, bone_names=bone_names, right=False)
        """     Legs        """
        self.r_leg = Leg(bone_ids=bone_ids, path_obj=image_paths, bone_names=bone_names, right=True)
        self.l_leg = Leg(bone_ids=bone_ids, path_obj=image_paths, bone_names=bone_names, right=False)
