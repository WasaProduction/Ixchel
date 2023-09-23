from mongodb.connection_handlers.mongo_local_database import MongoLocalDatabase
import re


class GetBoneNames:
    def __init__(self, language=0):
        self.name = ''
        self.language = language
        self.bone_names = MongoLocalDatabase('bone_names').collection
        self.get_bone_names()

    def get_bone_names(self):
        self.json_into_self(self.bone_names.find())

    def json_into_self(self, json):
        for element in json:
            """
                Bone names are inside a mongo object called bones, then in an array named by the bone, the words are the
                words in different languages
                0: English
                1: Spanish
            """
            """     Head        """
            #   Cranium
            self.cranium_frontal = element['bones']['cranium_frontal'][self.language]
            self.cranium_r_parietal = element['bones']['cranium_r_parietal'][self.language]
            self.cranium_l_parietal = element['bones']['cranium_l_parietal'][self.language]
            self.cranium_r_temporal = element['bones']['cranium_r_temporal'][self.language]
            self.cranium_l_temporal = element['bones']['cranium_l_temporal'][self.language]
            self.cranium_occipital = element['bones']['cranium_occipital'][self.language]
            self.cranium_sphenoid = element['bones']['cranium_sphenoid'][self.language]
            self.cranium_ethmoid = element['bones']['cranium_ethmoid'][self.language]

            self.r_ear_malleus = element['bones']['r_ear_malleus'][self.language]
            self.r_ear_incus = element['bones']['r_ear_incus'][self.language]
            self.r_ear_stapes = element['bones']['r_ear_stapes'][self.language]
            self.l_ear_malleus = element['bones']['l_ear_malleus'][self.language]
            self.l_ear_incus = element['bones']['l_ear_incus'][self.language]
            self.l_ear_stapes = element['bones']['l_ear_stapes'][self.language]

            self.facial_mandible = element['bones']['facial_mandible'][self.language]
            self.facial_r_maxilla = element['bones']['facial_r_maxilla'][self.language]
            self.facial_l_maxilla = element['bones']['facial_l_maxilla'][self.language]
            self.facial_r_palatine = element['bones']['facial_r_palatine'][self.language]
            self.facial_l_palatine = element['bones']['facial_l_palatine'][self.language]
            self.facial_r_zygomatic = element['bones']['facial_r_zygomatic'][self.language]
            self.facial_l_zygomatic = element['bones']['facial_l_zygomatic'][self.language]
            self.facial_r_nasal = element['bones']['facial_r_nasal'][self.language]
            self.facial_l_nasal = element['bones']['facial_l_nasal'][self.language]
            self.facial_r_lacrimal = element['bones']['facial_r_lacrimal'][self.language]
            self.facial_l_lacrimal = element['bones']['facial_l_lacrimal'][self.language]
            self.facial_vomer = element['bones']['facial_vomer'][self.language]
            self.facial_r_inferior_nasal_conchae = element['bones']['facial_r_inferior_nasal_conchae'][self.language]
            self.facial_l_inferior_nasal_conchae = element['bones']['facial_l_inferior_nasal_conchae'][self.language]

            # Teeth

            # Neck
            self.hyoid = element['bones']['hyoid'][self.language]

            # Thorax
            self.sternum = element['bones']['sternum'][self.language]

            # Accessory
            self.rib_r_a01 = element['bones']['rib_r_a01'][self.language]
            self.rib_l_a01 = element['bones']['rib_l_a01'][self.language]

            # Rib-sternum
            self.rib_r_t01 = element['bones']['rib_r_t01'][self.language]
            self.rib_l_t01 = element['bones']['rib_l_t01'][self.language]
            self.rib_r_t02 = element['bones']['rib_r_t02'][self.language]
            self.rib_l_t02 = element['bones']['rib_l_t02'][self.language]
            self.rib_r_t03 = element['bones']['rib_r_t03'][self.language]
            self.rib_l_t03 = element['bones']['rib_l_t03'][self.language]
            self.rib_r_t04 = element['bones']['rib_r_t04'][self.language]
            self.rib_l_t04 = element['bones']['rib_l_t04'][self.language]
            self.rib_r_t05 = element['bones']['rib_r_t05'][self.language]
            self.rib_l_t05 = element['bones']['rib_l_t05'][self.language]
            self.rib_r_t06 = element['bones']['rib_r_t06'][self.language]
            self.rib_l_t06 = element['bones']['rib_l_t06'][self.language]
            self.rib_r_t07 = element['bones']['rib_r_t07'][self.language]
            self.rib_l_t07 = element['bones']['rib_l_t07'][self.language]

            # Rib-rib-sternum
            self.rib_r_t08 = element['bones']['rib_r_t08'][self.language]
            self.rib_l_t08 = element['bones']['rib_l_t08'][self.language]
            self.rib_r_t09 = element['bones']['rib_r_t09'][self.language]
            self.rib_l_t09 = element['bones']['rib_l_t09'][self.language]
            self.rib_r_t10 = element['bones']['rib_r_t10'][self.language]
            self.rib_l_t10 = element['bones']['rib_l_t10'][self.language]

            # Floating
            self.rib_r_t11 = element['bones']['rib_r_t11'][self.language]
            self.rib_l_t11 = element['bones']['rib_l_t11'][self.language]
            self.rib_r_t12 = element['bones']['rib_r_t12'][self.language]
            self.rib_l_t12 = element['bones']['rib_l_t12'][self.language]

            # Vertebrae

            # Cervical
            self.c1 = element['bones']['c1'][self.language]
            self.c2 = element['bones']['c2'][self.language]
            self.c3 = element['bones']['c3'][self.language]
            self.c4 = element['bones']['c4'][self.language]
            self.c5 = element['bones']['c5'][self.language]
            self.c6 = element['bones']['c6'][self.language]
            self.c7 = element['bones']['c7'][self.language]

            # Lumbar
            self.l1 = element['bones']['l1'][self.language]
            self.l2 = element['bones']['l2'][self.language]
            self.l3 = element['bones']['l3'][self.language]
            self.l4 = element['bones']['l4'][self.language]
            self.l5 = element['bones']['l5'][self.language]

            # Thoracic
            self.t1 = element['bones']['t1'][self.language]
            self.t2 = element['bones']['t2'][self.language]
            self.t3 = element['bones']['t3'][self.language]
            self.t4 = element['bones']['t4'][self.language]
            self.t5 = element['bones']['t5'][self.language]
            self.t6 = element['bones']['t6'][self.language]
            self.t7 = element['bones']['t7'][self.language]
            self.t8 = element['bones']['t8'][self.language]
            self.t9 = element['bones']['t9'][self.language]
            self.t10 = element['bones']['t10'][self.language]
            self.t11 = element['bones']['t11'][self.language]
            self.t12 = element['bones']['t12'][self.language]

            # Shoulder
            self.r_omoplatae = element['bones']['r_omoplatae'][self.language]
            self.l_omoplatae = element['bones']['l_omoplatae'][self.language]
            self.r_clavicle = element['bones']['r_clavicle'][self.language]
            self.l_clavicle = element['bones']['l_clavicle'][self.language]

            # Arms
            self.r_humerus = element['bones']['r_humerus'][self.language]
            self.l_humerus = element['bones']['l_humerus'][self.language]
            self.r_radius = element['bones']['r_radius'][self.language]
            self.l_radius = element['bones']['l_radius'][self.language]
            self.r_ulna = element['bones']['r_ulna'][self.language]
            self.l_ulna = element['bones']['l_ulna'][self.language]

            # Hands

            # Carpals
            self.r_scaphoid = element['bones']['r_scaphoid'][self.language]
            self.l_scaphoid = element['bones']['l_scaphoid'][self.language]
            self.r_lunate = element['bones']['r_lunate'][self.language]
            self.l_lunate = element['bones']['l_lunate'][self.language]
            self.r_triquetrum = element['bones']['r_triquetrum'][self.language]
            self.l_triquetrum = element['bones']['l_triquetrum'][self.language]
            self.r_pisiform = element['bones']['r_pisiform'][self.language]
            self.l_pisiform = element['bones']['l_pisiform'][self.language]
            self.r_trapezium = element['bones']['r_trapezium'][self.language]
            self.l_trapezium = element['bones']['l_trapezium'][self.language]
            self.r_trapezoid = element['bones']['r_trapezoid'][self.language]
            self.l_trapezoid = element['bones']['l_trapezoid'][self.language]
            self.r_capitate = element['bones']['r_capitate'][self.language]
            self.l_capitate = element['bones']['l_capitate'][self.language]
            self.r_hamate = element['bones']['r_hamate'][self.language]
            self.l_hamate = element['bones']['l_hamate'][self.language]

            # Metacarpals
            self.r_first_metacarpal = element['bones']['r_first_metacarpal'][self.language]
            self.l_first_metacarpal = element['bones']['l_first_metacarpal'][self.language]
            self.r_second_metacarpal = element['bones']['r_second_metacarpal'][self.language]
            self.l_second_metacarpal = element['bones']['l_second_metacarpal'][self.language]
            self.r_third_metacarpal = element['bones']['r_third_metacarpal'][self.language]
            self.l_third_metacarpal = element['bones']['l_third_metacarpal'][self.language]
            self.r_fourth_metacarpal = element['bones']['r_fourth_metacarpal'][self.language]
            self.l_fourth_metacarpal = element['bones']['l_fourth_metacarpal'][self.language]
            self.r_fifth_metacarpal = element['bones']['r_fifth_metacarpal'][self.language]
            self.l_fifth_metacarpal = element['bones']['l_fifth_metacarpal'][self.language]

            # Phalanges

            # Thumb
            self.r_t_phalanx_proximal = element['bones']['r_t_phalanx_proximal'][self.language]
            self.l_t_phalanx_proximal = element['bones']['l_t_phalanx_proximal'][self.language]
            self.r_t_phalanx_distal = element['bones']['r_t_phalanx_distal'][self.language]
            self.l_t_phalanx_distal = element['bones']['l_t_phalanx_distal'][self.language]

            # Index
            self.r_i_phalanx_proximal = element['bones']['r_i_phalanx_proximal'][self.language]
            self.l_i_phalanx_proximal = element['bones']['l_i_phalanx_proximal'][self.language]
            self.r_i_phalanx_intermediate = element['bones']['r_i_phalanx_intermediate'][self.language]
            self.l_i_phalanx_intermediate = element['bones']['l_i_phalanx_intermediate'][self.language]
            self.r_i_phalanx_distal = element['bones']['r_i_phalanx_distal'][self.language]
            self.l_i_phalanx_distal = element['bones']['l_i_phalanx_distal'][self.language]

            # Middle
            self.r_m_phalanx_proximal = element['bones']['r_m_phalanx_proximal'][self.language]
            self.l_m_phalanx_proximal = element['bones']['l_m_phalanx_proximal'][self.language]
            self.r_m_phalanx_intermediate = element['bones']['r_m_phalanx_intermediate'][self.language]
            self.l_m_phalanx_intermediate = element['bones']['l_m_phalanx_intermediate'][self.language]
            self.r_m_phalanx_distal = element['bones']['r_m_phalanx_distal'][self.language]
            self.l_m_phalanx_distal = element['bones']['l_m_phalanx_distal'][self.language]

            # Ring
            self.r_r_phalanx_proximal = element['bones']['r_r_phalanx_proximal'][self.language]
            self.l_r_phalanx_proximal = element['bones']['l_r_phalanx_proximal'][self.language]
            self.r_r_phalanx_intermediate = element['bones']['r_r_phalanx_intermediate'][self.language]
            self.l_r_phalanx_intermediate = element['bones']['l_r_phalanx_intermediate'][self.language]
            self.r_r_phalanx_distal = element['bones']['r_r_phalanx_distal'][self.language]
            self.l_r_phalanx_distal = element['bones']['l_r_phalanx_distal'][self.language]

            # Pinky
            self.r_p_phalanx_proximal = element['bones']['r_p_phalanx_proximal'][self.language]
            self.l_p_phalanx_proximal = element['bones']['l_p_phalanx_proximal'][self.language]
            self.r_p_phalanx_intermediate = element['bones']['r_p_phalanx_intermediate'][self.language]
            self.l_p_phalanx_intermediate = element['bones']['l_p_phalanx_intermediate'][self.language]
            self.r_p_phalanx_distal = element['bones']['r_p_phalanx_distal'][self.language]
            self.l_p_phalanx_distal = element['bones']['l_p_phalanx_distal'][self.language]

            # Pelvis
            self.sacrum = element['bones']['sacrum'][self.language]
            self.coccyx = element['bones']['coccyx'][self.language]
            self.r_hip = element['bones']['r_hip'][self.language]
            self.l_hip = element['bones']['l_hip'][self.language]

            # Legs
            self.r_femur = element['bones']['r_femur'][self.language]
            self.l_femur = element['bones']['l_femur'][self.language]
            self.r_patella = element['bones']['r_patella'][self.language]
            self.l_patella = element['bones']['l_patella'][self.language]
            self.r_tibia = element['bones']['r_tibia'][self.language]
            self.l_tibia = element['bones']['l_tibia'][self.language]
            self.r_fibula = element['bones']['r_fibula'][self.language]
            self.l_fibula = element['bones']['l_fibula'][self.language]

            # Foot

            # Metatarsal
            self.r_first_metatarsal = element['bones']['r_first_metatarsal'][self.language]
            self.l_first_metatarsal = element['bones']['l_first_metatarsal'][self.language]
            self.r_second_metatarsal = element['bones']['r_second_metatarsal'][self.language]
            self.l_second_metatarsal = element['bones']['l_second_metatarsal'][self.language]
            self.r_third_metatarsal = element['bones']['r_third_metatarsal'][self.language]
            self.l_third_metatarsal = element['bones']['l_third_metatarsal'][self.language]
            self.r_fourth_metatarsal = element['bones']['r_fourth_metatarsal'][self.language]
            self.l_fourth_metatarsal = element['bones']['l_fourth_metatarsal'][self.language]
            self.r_fifth_metatarsal = element['bones']['r_fifth_metatarsal'][self.language]
            self.l_fifth_metatarsal = element['bones']['l_fifth_metatarsal'][self.language]

            # Tarsal
            self.r_calcaneus = element['bones']['r_calcaneus'][self.language]
            self.l_calcaneus = element['bones']['l_calcaneus'][self.language]
            self.r_talus = element['bones']['r_talus'][self.language]
            self.l_talus = element['bones']['l_talus'][self.language]
            self.r_navicular = element['bones']['r_navicular'][self.language]
            self.l_navicular = element['bones']['l_navicular'][self.language]
            self.r_medial_cuneiform = element['bones']['r_medial_cuneiform'][self.language]
            self.l_medial_cuneiform = element['bones']['l_medial_cuneiform'][self.language]
            self.r_intermediate_cuneiform = element['bones']['r_intermediate_cuneiform'][self.language]
            self.l_intermediate_cuneiform = element['bones']['l_intermediate_cuneiform'][self.language]
            self.r_lateral_cuneiform = element['bones']['r_lateral_cuneiform'][self.language]
            self.l_lateral_cuneiform = element['bones']['l_lateral_cuneiform'][self.language]
            self.r_cuboid = element['bones']['r_cuboid'][self.language]
            self.l_cuboid = element['bones']['l_cuboid'][self.language]

            # Phalanges
            # First Toe
            self.r_1_phalanx_proximal = element['bones']['r_1_phalanx_proximal'][self.language]
            self.l_1_phalanx_proximal = element['bones']['l_1_phalanx_proximal'][self.language]
            self.r_1_phalanx_distal = element['bones']['r_1_phalanx_distal'][self.language]
            self.l_1_phalanx_distal = element['bones']['l_1_phalanx_distal'][self.language]

            # Second Toe
            self.r_2_phalanx_proximal = element['bones']['r_2_phalanx_proximal'][self.language]
            self.l_2_phalanx_proximal = element['bones']['l_2_phalanx_proximal'][self.language]
            self.r_2_phalanx_intermediate = element['bones']['r_2_phalanx_intermediate'][self.language]
            self.l_2_phalanx_intermediate = element['bones']['l_2_phalanx_intermediate'][self.language]
            self.r_2_phalanx_distal = element['bones']['r_2_phalanx_distal'][self.language]
            self.l_2_phalanx_distal = element['bones']['l_2_phalanx_distal'][self.language]

            # Third Toe
            self.r_3_phalanx_proximal = element['bones']['r_3_phalanx_proximal'][self.language]
            self.l_3_phalanx_proximal = element['bones']['l_3_phalanx_proximal'][self.language]
            self.r_3_phalanx_intermediate = element['bones']['r_3_phalanx_intermediate'][self.language]
            self.l_3_phalanx_intermediate = element['bones']['l_3_phalanx_intermediate'][self.language]
            self.r_3_phalanx_distal = element['bones']['r_3_phalanx_distal'][self.language]
            self.l_3_phalanx_distal = element['bones']['l_3_phalanx_distal'][self.language]

            # Fourth Toe
            self.r_4_phalanx_proximal = element['bones']['r_4_phalanx_proximal'][self.language]
            self.l_4_phalanx_proximal = element['bones']['l_4_phalanx_proximal'][self.language]
            self.r_4_phalanx_intermediate = element['bones']['r_4_phalanx_intermediate'][self.language]
            self.l_4_phalanx_intermediate = element['bones']['l_4_phalanx_intermediate'][self.language]
            self.r_4_phalanx_distal = element['bones']['r_4_phalanx_distal'][self.language]
            self.l_4_phalanx_distal = element['bones']['l_4_phalanx_distal'][self.language]

            # Fifth Toe
            self.r_5_phalanx_proximal = element['bones']['r_5_phalanx_proximal'][self.language]
            self.l_5_phalanx_proximal = element['bones']['l_5_phalanx_proximal'][self.language]
            self.r_5_phalanx_intermediate = element['bones']['r_5_phalanx_intermediate'][self.language]
            self.l_5_phalanx_intermediate = element['bones']['l_5_phalanx_intermediate'][self.language]
            self.r_5_phalanx_distal = element['bones']['r_5_phalanx_distal'][self.language]
            self.l_5_phalanx_distal = element['bones']['l_5_phalanx_distal'][self.language]
