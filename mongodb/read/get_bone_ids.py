from mongodb.connection_handlers.mongo_local_database import MongoLocalDatabase
import re


class GetBoneIds:
    def __init__(self):
        self.name = ''
        self.bone_names = MongoLocalDatabase('bone_ids').collection
        self.get_bone_ids()

    def get_bone_ids(self):
        self.json_into_self(self.bone_names.find())

    def json_into_self(self, json):
        for element in json:
            """     Head        """
            #   Cranium
            self.cranium_frontal = element['bones']['cranium_frontal']
            self.cranium_r_parietal = element['bones']['cranium_r_parietal']
            self.cranium_l_parietal = element['bones']['cranium_l_parietal']
            self.cranium_r_temporal = element['bones']['cranium_r_temporal']
            self.cranium_l_temporal = element['bones']['cranium_l_temporal']
            self.cranium_occipital = element['bones']['cranium_occipital']
            self.cranium_sphenoid = element['bones']['cranium_sphenoid']
            self.cranium_ethmoid = element['bones']['cranium_ethmoid']

            self.r_ear_malleus = element['bones']['r_ear_malleus']
            self.r_ear_incus = element['bones']['r_ear_incus']
            self.r_ear_stapes = element['bones']['r_ear_stapes']
            self.l_ear_malleus = element['bones']['l_ear_malleus']
            self.l_ear_incus = element['bones']['l_ear_incus']
            self.l_ear_stapes = element['bones']['l_ear_stapes']

            self.facial_mandible = element['bones']['facial_mandible']
            self.facial_r_maxilla = element['bones']['facial_r_maxilla']
            self.facial_l_maxilla = element['bones']['facial_l_maxilla']
            self.facial_r_palatine = element['bones']['facial_r_palatine']
            self.facial_l_palatine = element['bones']['facial_l_palatine']
            self.facial_r_zygomatic = element['bones']['facial_r_zygomatic']
            self.facial_l_zygomatic = element['bones']['facial_l_zygomatic']
            self.facial_r_nasal = element['bones']['facial_r_nasal']
            self.facial_l_nasal = element['bones']['facial_l_nasal']
            self.facial_r_lacrimal = element['bones']['facial_r_lacrimal']
            self.facial_l_lacrimal = element['bones']['facial_l_lacrimal']
            self.facial_vomer = element['bones']['facial_vomer']
            self.facial_r_inferior_nasal_conchae = element['bones']['facial_r_inferior_nasal_conchae']
            self.facial_l_inferior_nasal_conchae = element['bones']['facial_l_inferior_nasal_conchae']

            # Teeth

            # Neck
            self.hyoid = element['bones']['hyoid']

            # Thorax
            self.sternum = element['bones']['sternum']

            # Accessory
            self.rib_r_a01 = element['bones']['rib_r_a01']
            self.rib_l_a01 = element['bones']['rib_l_a01']

            # Rib-sternum
            self.rib_r_t01 = element['bones']['rib_r_t01']
            self.rib_l_t01 = element['bones']['rib_l_t01']
            self.rib_r_t02 = element['bones']['rib_r_t02']
            self.rib_l_t02 = element['bones']['rib_l_t02']
            self.rib_r_t03 = element['bones']['rib_r_t03']
            self.rib_l_t03 = element['bones']['rib_l_t03']
            self.rib_r_t04 = element['bones']['rib_r_t04']
            self.rib_l_t04 = element['bones']['rib_l_t04']
            self.rib_r_t05 = element['bones']['rib_r_t05']
            self.rib_l_t05 = element['bones']['rib_l_t05']
            self.rib_r_t06 = element['bones']['rib_r_t06']
            self.rib_l_t06 = element['bones']['rib_l_t06']
            self.rib_r_t07 = element['bones']['rib_r_t07']
            self.rib_l_t07 = element['bones']['rib_l_t07']

            # Rib-rib-sternum
            self.rib_r_t08 = element['bones']['rib_r_t08']
            self.rib_l_t08 = element['bones']['rib_l_t08']
            self.rib_r_t09 = element['bones']['rib_r_t09']
            self.rib_l_t09 = element['bones']['rib_l_t09']
            self.rib_r_t10 = element['bones']['rib_r_t10']
            self.rib_l_t10 = element['bones']['rib_l_t10']

            # Floating
            self.rib_r_t11 = element['bones']['rib_r_t11']
            self.rib_l_t11 = element['bones']['rib_l_t11']
            self.rib_r_t12 = element['bones']['rib_r_t12']
            self.rib_l_t12 = element['bones']['rib_l_t12']

            # Vertebrae

            # Cervical
            self.c1 = element['bones']['c1']
            self.c2 = element['bones']['c2']
            self.c3 = element['bones']['c3']
            self.c4 = element['bones']['c4']
            self.c5 = element['bones']['c5']
            self.c6 = element['bones']['c6']
            self.c7 = element['bones']['c7']

            # Lumbar
            self.l1 = element['bones']['l1']
            self.l2 = element['bones']['l2']
            self.l3 = element['bones']['l3']
            self.l4 = element['bones']['l4']
            self.l5 = element['bones']['l5']

            # Thoracic
            self.t1 = element['bones']['t1']
            self.t2 = element['bones']['t2']
            self.t3 = element['bones']['t3']
            self.t4 = element['bones']['t4']
            self.t5 = element['bones']['t5']
            self.t6 = element['bones']['t6']
            self.t7 = element['bones']['t7']
            self.t8 = element['bones']['t8']
            self.t9 = element['bones']['t9']
            self.t10 = element['bones']['t10']
            self.t11 = element['bones']['t11']
            self.t12 = element['bones']['t12']

            # Shoulder
            self.r_omoplatae = element['bones']['r_omoplatae']
            self.l_omoplatae = element['bones']['l_omoplatae']
            self.r_clavicle = element['bones']['r_clavicle']
            self.l_clavicle = element['bones']['l_clavicle']

            # Arms
            self.r_humerus = element['bones']['r_humerus']
            self.l_humerus = element['bones']['l_humerus']
            self.r_radius = element['bones']['r_radius']
            self.l_radius = element['bones']['l_radius']
            self.r_ulna = element['bones']['r_ulna']
            self.l_ulna = element['bones']['l_ulna']

            # Hands

            # Carpals
            self.r_scaphoid = element['bones']['r_scaphoid']
            self.l_scaphoid = element['bones']['l_scaphoid']
            self.r_lunate = element['bones']['r_lunate']
            self.l_lunate = element['bones']['l_lunate']
            self.r_triquetrum = element['bones']['r_triquetrum']
            self.l_triquetrum = element['bones']['l_triquetrum']
            self.r_pisiform = element['bones']['r_pisiform']
            self.l_pisiform = element['bones']['l_pisiform']
            self.r_trapezium = element['bones']['r_trapezium']
            self.l_trapezium = element['bones']['l_trapezium']
            self.r_trapezoid = element['bones']['r_trapezoid']
            self.l_trapezoid = element['bones']['l_trapezoid']
            self.r_capitate = element['bones']['r_capitate']
            self.l_capitate = element['bones']['l_capitate']
            self.r_hamate = element['bones']['r_hamate']
            self.l_hamate = element['bones']['l_hamate']
            # Metacarpals
            self.r_first_metacarpal = element['bones']['r_first_metacarpal']
            self.l_first_metacarpal = element['bones']['l_first_metacarpal']
            self.r_second_metacarpal = element['bones']['r_second_metacarpal']
            self.l_second_metacarpal = element['bones']['l_second_metacarpal']
            self.r_third_metacarpal = element['bones']['r_third_metacarpal']
            self.l_third_metacarpal = element['bones']['l_third_metacarpal']
            self.r_fourth_metacarpal = element['bones']['r_fourth_metacarpal']
            self.l_fourth_metacarpal = element['bones']['l_fourth_metacarpal']
            self.r_fifth_metacarpal = element['bones']['r_fifth_metacarpal']
            self.l_fifth_metacarpal = element['bones']['l_fifth_metacarpal']

            # Phalanges

            # Thumb
            self.r_t_phalanx_proximal = element['bones']['r_t_phalanx_proximal']
            self.l_t_phalanx_proximal = element['bones']['l_t_phalanx_proximal']
            self.r_t_phalanx_distal = element['bones']['r_t_phalanx_distal']
            self.l_t_phalanx_distal = element['bones']['l_t_phalanx_distal']

            # Index
            self.r_i_phalanx_proximal = element['bones']['r_i_phalanx_proximal']
            self.l_i_phalanx_proximal = element['bones']['l_i_phalanx_proximal']
            self.r_i_phalanx_intermediate = element['bones']['r_i_phalanx_intermediate']
            self.l_i_phalanx_intermediate = element['bones']['l_i_phalanx_intermediate']
            self.r_i_phalanx_distal = element['bones']['r_i_phalanx_distal']
            self.l_i_phalanx_distal = element['bones']['l_i_phalanx_distal']

            # Middle
            self.r_m_phalanx_proximal = element['bones']['r_m_phalanx_proximal']
            self.l_m_phalanx_proximal = element['bones']['l_m_phalanx_proximal']
            self.r_m_phalanx_intermediate = element['bones']['r_m_phalanx_intermediate']
            self.l_m_phalanx_intermediate = element['bones']['l_m_phalanx_intermediate']
            self.r_m_phalanx_distal = element['bones']['r_m_phalanx_distal']
            self.l_m_phalanx_distal = element['bones']['l_m_phalanx_distal']

            # Ring
            self.r_r_phalanx_proximal = element['bones']['r_r_phalanx_proximal']
            self.l_r_phalanx_proximal = element['bones']['l_r_phalanx_proximal']
            self.r_r_phalanx_intermediate = element['bones']['r_r_phalanx_intermediate']
            self.l_r_phalanx_intermediate = element['bones']['l_r_phalanx_intermediate']
            self.r_r_phalanx_distal = element['bones']['r_r_phalanx_distal']
            self.l_r_phalanx_distal = element['bones']['l_r_phalanx_distal']

            # Pinky
            self.r_p_phalanx_proximal = element['bones']['r_p_phalanx_proximal']
            self.l_p_phalanx_proximal = element['bones']['l_p_phalanx_proximal']
            self.r_p_phalanx_intermediate = element['bones']['r_p_phalanx_intermediate']
            self.l_p_phalanx_intermediate = element['bones']['l_p_phalanx_intermediate']
            self.r_p_phalanx_distal = element['bones']['r_p_phalanx_distal']
            self.l_p_phalanx_distal = element['bones']['l_p_phalanx_distal']

            # Pelvis
            self.sacrum = element['bones']['sacrum']
            self.coccyx = element['bones']['coccyx']
            self.r_hip = element['bones']['r_hip']
            self.l_hip = element['bones']['l_hip']

            # Legs
            self.r_femur = element['bones']['r_femur']
            self.l_femur = element['bones']['l_femur']
            self.r_patella = element['bones']['r_patella']
            self.l_patella = element['bones']['l_patella']
            self.r_tibia = element['bones']['r_tibia']
            self.l_tibia = element['bones']['l_tibia']
            self.r_fibula = element['bones']['r_fibula']
            self.l_fibula = element['bones']['l_fibula']

            # Foot

            # Metatarsal
            self.r_first_metatarsal = element['bones']['r_first_metatarsal']
            self.l_first_metatarsal = element['bones']['l_first_metatarsal']
            self.r_second_metatarsal = element['bones']['r_second_metatarsal']
            self.l_second_metatarsal = element['bones']['l_second_metatarsal']
            self.r_third_metatarsal = element['bones']['r_third_metatarsal']
            self.l_third_metatarsal = element['bones']['l_third_metatarsal']
            self.r_fourth_metatarsal = element['bones']['r_fourth_metatarsal']
            self.l_fourth_metatarsal = element['bones']['l_fourth_metatarsal']
            self.r_fifth_metatarsal = element['bones']['r_fifth_metatarsal']
            self.l_fifth_metatarsal = element['bones']['l_fifth_metatarsal']

            # Tarsal
            self.r_calcaneus = element['bones']['r_calcaneus']
            self.l_calcaneus = element['bones']['l_calcaneus']
            self.r_talus = element['bones']['r_talus']
            self.l_talus = element['bones']['l_talus']
            self.r_navicular = element['bones']['r_navicular']
            self.l_navicular = element['bones']['l_navicular']
            self.r_medial_cuneiform = element['bones']['r_medial_cuneiform']
            self.l_medial_cuneiform = element['bones']['l_medial_cuneiform']
            self.r_intermediate_cuneiform = element['bones']['r_intermediate_cuneiform']
            self.l_intermediate_cuneiform = element['bones']['l_intermediate_cuneiform']
            self.r_lateral_cuneiform = element['bones']['r_lateral_cuneiform']
            self.l_lateral_cuneiform = element['bones']['l_lateral_cuneiform']
            self.r_cuboid = element['bones']['r_cuboid']
            self.l_cuboid = element['bones']['l_cuboid']

            # Phalanges
            # First Toe
            self.r_1_phalanx_proximal = element['bones']['r_1_phalanx_proximal']
            self.l_1_phalanx_proximal = element['bones']['l_1_phalanx_proximal']
            self.r_1_phalanx_distal = element['bones']['r_1_phalanx_distal']
            self.l_1_phalanx_distal = element['bones']['l_1_phalanx_distal']

            # Second Toe
            self.r_2_phalanx_proximal = element['bones']['r_2_phalanx_proximal']
            self.l_2_phalanx_proximal = element['bones']['l_2_phalanx_proximal']
            self.r_2_phalanx_intermediate = element['bones']['r_2_phalanx_intermediate']
            self.l_2_phalanx_intermediate = element['bones']['l_2_phalanx_intermediate']
            self.r_2_phalanx_distal = element['bones']['r_2_phalanx_distal']
            self.l_2_phalanx_distal = element['bones']['l_2_phalanx_distal']

            # Third Toe
            self.r_3_phalanx_proximal = element['bones']['r_3_phalanx_proximal']
            self.l_3_phalanx_proximal = element['bones']['l_3_phalanx_proximal']
            self.r_3_phalanx_intermediate = element['bones']['r_3_phalanx_intermediate']
            self.l_3_phalanx_intermediate = element['bones']['l_3_phalanx_intermediate']
            self.r_3_phalanx_distal = element['bones']['r_3_phalanx_distal']
            self.l_3_phalanx_distal = element['bones']['l_3_phalanx_distal']

            # Fourth Toe
            self.r_4_phalanx_proximal = element['bones']['r_4_phalanx_proximal']
            self.l_4_phalanx_proximal = element['bones']['l_4_phalanx_proximal']
            self.r_4_phalanx_intermediate = element['bones']['r_4_phalanx_intermediate']
            self.l_4_phalanx_intermediate = element['bones']['l_4_phalanx_intermediate']
            self.r_4_phalanx_distal = element['bones']['r_4_phalanx_distal']
            self.l_4_phalanx_distal = element['bones']['l_4_phalanx_distal']

            # Fifth Toe
            self.r_5_phalanx_proximal = element['bones']['r_5_phalanx_proximal']
            self.l_5_phalanx_proximal = element['bones']['l_5_phalanx_proximal']
            self.r_5_phalanx_intermediate = element['bones']['r_5_phalanx_intermediate']
            self.l_5_phalanx_intermediate = element['bones']['l_5_phalanx_intermediate']
            self.r_5_phalanx_distal = element['bones']['r_5_phalanx_distal']
            self.l_5_phalanx_distal = element['bones']['l_5_phalanx_distal']
