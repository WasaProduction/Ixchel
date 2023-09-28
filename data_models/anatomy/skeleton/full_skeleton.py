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
from mongodb.read.get_bone_colors import GetBoneColors


class FullSkeleton:
    def __init__(self):
        image_paths = SkeletonPaths()
        bone_names = GetBoneNames(language=1)
        bone_ids = GetBoneIds()
        colors = GetBoneColors().colors_arr
        """     Head        """
        self.cranium = Cranium(bone_ids=bone_ids, path_obj=image_paths, bone_names=bone_names, colors=colors)
        self.right_ear = Ear(bone_ids=bone_ids, path_obj=image_paths, bone_names=bone_names, right=True, colors=colors)
        self.left_ear = Ear(bone_ids=bone_ids, path_obj=image_paths, bone_names=bone_names, right=False, colors=colors)
        self.facial = Facial(bone_ids=bone_ids, path_obj=image_paths, bone_names=bone_names, colors=colors)
        """     Neck        """
        self.hyoid = Hyoid(bone_ids=bone_ids, path_obj=image_paths, bone_names=bone_names, colors=colors)
        """     Thorax      """
        self.thorax = Thorax(bone_ids=bone_ids, path_obj=image_paths, bone_names=bone_names, colors=colors)
        """     Vertebrae   """
        self.vertebrae = Vertebrae(bone_ids=bone_ids, path_obj=image_paths, bone_names=bone_names, colors=colors)
        """     Shoulder    """
        self.r_omoplatae = Omoplatae(bone_ids=bone_ids, path_obj=image_paths, bone_names=bone_names, right=True,
                                     colors=colors)
        self.l_omoplatae = Omoplatae(bone_ids=bone_ids, path_obj=image_paths, bone_names=bone_names, right=False,
                                     colors=colors)
        self.r_clavicle = Clavicle(bone_ids=bone_ids, path_obj=image_paths, bone_names=bone_names, right=True,
                                   colors=colors)
        self.l_clavicle = Clavicle(bone_ids=bone_ids, path_obj=image_paths, bone_names=bone_names, right=False,
                                   colors=colors)
        """     Arms        """
        self.r_arm = Arm(bone_ids=bone_ids, path_obj=image_paths, bone_names=bone_names, right=False, colors=colors)
        self.l_arm = Arm(bone_ids=bone_ids, path_obj=image_paths, bone_names=bone_names, right=False, colors=colors)
        """     Pelvis      """
        self.sacrum = Sacrum(bone_ids=bone_ids, path_obj=image_paths, bone_names=bone_names, colors=colors)
        self.coccyx = Coccyx(bone_ids=bone_ids, path_obj=image_paths, bone_names=bone_names, colors=colors)
        self.r_hip = Hip(bone_ids=bone_ids, path_obj=image_paths, bone_names=bone_names, right=True, colors=colors)
        self.l_hip = Hip(bone_ids=bone_ids, path_obj=image_paths, bone_names=bone_names, right=False, colors=colors)
        """     Legs        """
        self.r_leg = Leg(bone_ids=bone_ids, path_obj=image_paths, bone_names=bone_names, right=True, colors=colors)
        self.l_leg = Leg(bone_ids=bone_ids, path_obj=image_paths, bone_names=bone_names, right=False, colors=colors)

        self.all_bones = [
            self.cranium.frontal, self.cranium.right_parietal, self.cranium.left_parietal,
            self.cranium.right_temporal, self.cranium.left_temporal, self.cranium.occipital,
            self.cranium.sphenoid, self.cranium.ethmoid, self.right_ear.malleus,
            self.right_ear.incus, self.right_ear.stapes, self.left_ear.malleus,
            self.left_ear.incus, self.left_ear.stapes, self.facial.mandible,
            self.facial.right_maxilla, self.facial.left_maxilla, self.facial.right_palatine,
            self.facial.left_palatine, self.facial.right_zygomatic, self.facial.left_zygomatic,
            self.facial.right_nasal, self.facial.left_nasal, self.facial.right_lacrimal,
            self.facial.left_lacrimal, self.facial.vomer, self.facial.right_inferior_nasal_conchae,
            self.facial.left_inferior_nasal_conchae, self.hyoid, self.thorax.sternum,
            self.thorax.r_a01, self.thorax.l_a01, self.thorax.r_t01,
            self.thorax.l_t01, self.thorax.r_t02, self.thorax.l_t02,
            self.thorax.r_t03, self.thorax.l_t03, self.thorax.r_t04,
            self.thorax.l_t04, self.thorax.r_t05, self.thorax.l_t05,
            self.thorax.r_t06, self.thorax.l_t06, self.thorax.r_t07,
            self.thorax.l_t07, self.thorax.r_t08, self.thorax.l_t08,
            self.thorax.r_t09, self.thorax.l_t09, self.thorax.r_t10,
            self.thorax.l_t10, self.thorax.r_t11, self.thorax.l_t11,
            self.thorax.r_t12, self.thorax.l_t12, self.vertebrae.C1,
            self.vertebrae.C2, self.vertebrae.C3, self.vertebrae.C4,
            self.vertebrae.C5, self.vertebrae.C6, self.vertebrae.C7,
            self.vertebrae.L1, self.vertebrae.L2, self.vertebrae.L3,
            self.vertebrae.L4, self.vertebrae.L5, self.vertebrae.T1,
            self.vertebrae.T2, self.vertebrae.T3, self.vertebrae.T4,
            self.vertebrae.T5, self.vertebrae.T6, self.vertebrae.T7,
            self.vertebrae.T8, self.vertebrae.T9, self.vertebrae.T10,
            self.vertebrae.T11, self.vertebrae.T12, self.r_omoplatae,
            self.l_omoplatae, self.r_clavicle, self.l_clavicle,
            self.r_arm.humerus, self.l_arm.humerus, self.r_arm.radius,
            self.l_arm.radius, self.r_arm.ulna, self.l_arm.ulna,
            self.r_arm.hand.carpals.scaphoid, self.l_arm.hand.carpals.scaphoid, self.r_arm.hand.carpals.lunate,
            self.l_arm.hand.carpals.lunate, self.r_arm.hand.carpals.triquetrum, self.l_arm.hand.carpals.triquetrum,
            self.r_arm.hand.carpals.pisiform, self.l_arm.hand.carpals.pisiform, self.r_arm.hand.carpals.trapezium,
            self.l_arm.hand.carpals.trapezium, self.r_arm.hand.carpals.trapezoid, self.l_arm.hand.carpals.trapezoid,
            self.r_arm.hand.carpals.capitate, self.l_arm.hand.carpals.capitate, self.r_arm.hand.carpals.hamate,
            self.l_arm.hand.carpals.hamate, self.r_arm.hand.metacarpals.first, self.l_arm.hand.metacarpals.first,
            self.r_arm.hand.metacarpals.second, self.l_arm.hand.metacarpals.second, self.r_arm.hand.metacarpals.third,
            self.l_arm.hand.metacarpals.third, self.r_arm.hand.metacarpals.fourth, self.l_arm.hand.metacarpals.fourth,
            self.r_arm.hand.metacarpals.fifth, self.l_arm.hand.metacarpals.fifth, self.r_leg.foot.metatarsal.first,
            self.l_leg.foot.metatarsal.first, self.r_leg.foot.metatarsal.second, self.l_leg.foot.metatarsal.second,
            self.r_leg.foot.metatarsal.third, self.l_leg.foot.metatarsal.third, self.r_leg.foot.metatarsal.fourth,
            self.l_leg.foot.metatarsal.fourth, self.r_leg.foot.metatarsal.fifth, self.l_leg.foot.metatarsal.fifth,
            self.r_leg.foot.tarsals.calcaneus, self.l_leg.foot.tarsals.calcaneus, self.r_leg.foot.tarsals.talus,
            self.l_leg.foot.tarsals.talus, self.r_leg.foot.tarsals.navicular, self.l_leg.foot.tarsals.navicular,
            self.r_leg.foot.tarsals.medial_cuneiform, self.l_leg.foot.tarsals.medial_cuneiform,
            self.r_leg.foot.tarsals.lateral_cuneiform, self.l_leg.foot.tarsals.lateral_cuneiform,
            self.r_leg.foot.tarsals.cuboid, self.l_leg.foot.tarsals.cuboid,
            self.r_arm.hand.fingers.thumb.proximal_phalanges, self.l_arm.hand.fingers.thumb.proximal_phalanges,
            self.r_arm.hand.fingers.thumb.distal_phalanges, self.l_arm.hand.fingers.thumb.proximal_phalanges,
            self.r_arm.hand.fingers.index.proximal_phalanges, self.l_arm.hand.fingers.index.proximal_phalanges,
            self.r_arm.hand.fingers.index.intermediate_phalanges, self.l_arm.hand.fingers.index.intermediate_phalanges,
            self.r_arm.hand.fingers.index.distal_phalanges, self.l_arm.hand.fingers.index.distal_phalanges,
            self.r_arm.hand.fingers.middle.proximal_phalanges, self.l_arm.hand.fingers.middle.proximal_phalanges,
            self.r_arm.hand.fingers.middle.intermediate_phalanges,
            self.l_arm.hand.fingers.middle.intermediate_phalanges, self.r_arm.hand.fingers.middle.distal_phalanges,
            self.l_arm.hand.fingers.middle.distal_phalanges,
            self.r_arm.hand.fingers.ring.proximal_phalanges, self.l_arm.hand.fingers.ring.proximal_phalanges,
            self.r_arm.hand.fingers.ring.intermediate_phalanges, self.l_arm.hand.fingers.ring.intermediate_phalanges,
            self.r_arm.hand.fingers.ring.distal_phalanges, self.l_arm.hand.fingers.ring.distal_phalanges,
            self.r_arm.hand.fingers.pinky.proximal_phalanges, self.l_arm.hand.fingers.pinky.proximal_phalanges,
            self.r_arm.hand.fingers.pinky.intermediate_phalanges, self.l_arm.hand.fingers.pinky.intermediate_phalanges,
            self.r_arm.hand.fingers.pinky.distal_phalanges, self.l_arm.hand.fingers.pinky.distal_phalanges, self.sacrum,
            self.coccyx,
            self.r_hip, self.l_hip, self.r_leg.femur, self.l_leg.femur,
            self.r_leg.patella, self.l_leg.patella, self.r_leg.tibia,
            self.l_leg.tibia, self.r_leg.fibula, self.l_leg.fibula,
            self.r_leg.foot.toes.first_toe.proximal_phalanges, self.l_leg.foot.toes.first_toe.proximal_phalanges,
            self.r_leg.foot.toes.first_toe.distal_phalanges, self.l_leg.foot.toes.first_toe.distal_phalanges,
            self.r_leg.foot.toes.second_toe.proximal_phalanges, self.l_leg.foot.toes.second_toe.proximal_phalanges,
            self.r_leg.foot.toes.second_toe.intermediate_phalanges,
            self.l_leg.foot.toes.second_toe.intermediate_phalanges, self.r_leg.foot.toes.second_toe.distal_phalanges,
            self.l_leg.foot.toes.second_toe.distal_phalanges, self.r_leg.foot.toes.third_toe.proximal_phalanges,
            self.l_leg.foot.toes.third_toe.proximal_phalanges,
            self.r_leg.foot.toes.third_toe.intermediate_phalanges,
            self.l_leg.foot.toes.third_toe.intermediate_phalanges, self.r_leg.foot.toes.third_toe.distal_phalanges,
            self.l_leg.foot.toes.third_toe.distal_phalanges, self.r_leg.foot.toes.fourth_toe.proximal_phalanges,
            self.l_leg.foot.toes.fourth_toe.proximal_phalanges,
            self.r_leg.foot.toes.fourth_toe.intermediate_phalanges,
            self.l_leg.foot.toes.fourth_toe.intermediate_phalanges, self.r_leg.foot.toes.fourth_toe.distal_phalanges,
            self.l_leg.foot.toes.fourth_toe.distal_phalanges, self.r_leg.foot.toes.fifth_toe.proximal_phalanges,
            self.l_leg.foot.toes.fifth_toe.proximal_phalanges,
            self.r_leg.foot.toes.fifth_toe.intermediate_phalanges,
            self.l_leg.foot.toes.fifth_toe.intermediate_phalanges, self.r_leg.foot.toes.fifth_toe.distal_phalanges,
            self.l_leg.foot.toes.fifth_toe.distal_phalanges
        ]

    def update_skeleton(self):
        #   Update all bones.
        for bone in self.all_bones:
            bone.update_bone()
        pass

        #   TODO
        """
        for index, bone in enumerate(self.all_bones):
            #print("Id:", bone.bone_id, "Position:", index, "Bone:", bone.name)
            if int(bone.bone_id) != index + 1:
                print("Id:", bone.bone_id, "Position:", index, "Bone:", bone.name)
        """
