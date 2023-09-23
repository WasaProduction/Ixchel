#   https://www.anatomystandard.com


class SkeletonPaths:
    def __init__(self):
        folder = '/Users/jaimegonzalezquirarte/PycharmProjects/Ixchel/assets/anatomy_pixmaps/skeleton/pixmaps/'
        """     Files       """
        """     Head        """
        #   Cranium
        self.cranium_frontal = folder + 'frontal.png'
        self.cranium_r_parietal = folder + 'parietal.png'
        self.cranium_l_parietal = folder + 'parietal.png'
        self.cranium_r_temporal = folder + 'temporal.png'
        self.cranium_l_temporal = folder + 'temporal.png'
        self.cranium_occipital = folder + 'occipital.png'
        self.cranium_sphenoid = folder + 'sphenoid.png'
        self.cranium_ethmoid = folder + 'ethmoid.png'
        #   Ear
        self.r_ear_malleus = folder + 'malleus.png'
        self.r_ear_incus = folder + 'incus.png'
        self.r_ear_stapes = folder + 'stapes.png'
        self.l_ear_malleus = folder + 'malleus.png'
        self.l_ear_incus = folder + 'incus.png'
        self.l_ear_stapes = folder + 'stapes.png'
        #   Facial
        self.facial_mandible = folder + 'mandible.png'
        self.facial_r_maxilla = folder + 'maxilla.png'
        self.facial_l_maxilla = folder + 'maxilla.png'
        self.facial_r_palatine = folder + 'palatine.png'
        self.facial_l_palatine = folder + 'palatine.png'
        self.facial_r_zygomatic = folder + 'zygomatic.png'
        self.facial_l_zygomatic = folder + 'zygomatic.png'
        self.facial_r_nasal = folder + 'nasal.png'
        self.facial_l_nasal = folder + 'nasal.png'
        self.facial_r_lacrimal = folder + 'lacrimal.png'
        self.facial_l_lacrimal = folder + 'lacrimal.png'
        self.facial_vomer = folder + 'vomer.png'
        self.facial_r_inferior_nasal_conchae = folder + 'nasal_conchae.png'
        self.facial_l_inferior_nasal_conchae = folder + 'nasal_conchae.png'
        """     Teeth       """

        """     Neck        """
        self.hyoid = folder + 'hyoid.png'

        """     Thorax      """
        self.sternum = folder + 'frontal.png'
        #   Accessory
        self.rib_r_a01 = folder + 'frontal.png'
        self.rib_l_a01 = folder + 'frontal.png'
        #   Rib-sternum
        self.rib_r_t01 = folder + 'frontal.png'
        self.rib_l_t01 = folder + 'frontal.png'
        self.rib_r_t02 = folder + 'frontal.png'
        self.rib_l_t02 = folder + 'frontal.png'
        self.rib_r_t03 = folder + 'frontal.png'
        self.rib_l_t03 = folder + 'frontal.png'
        self.rib_r_t04 = folder + 'frontal.png'
        self.rib_l_t04 = folder + 'frontal.png'
        self.rib_r_t05 = folder + 'frontal.png'
        self.rib_l_t05 = folder + 'frontal.png'
        self.rib_r_t06 = folder + 'frontal.png'
        self.rib_l_t06 = folder + 'frontal.png'
        self.rib_r_t07 = folder + 'frontal.png'
        self.rib_l_t07 = folder + 'frontal.png'
        #   Rib-rib-sternum
        self.rib_r_t08 = folder + 'frontal.png'
        self.rib_l_t08 = folder + 'frontal.png'
        self.rib_r_t09 = folder + 'frontal.png'
        self.rib_l_t09 = folder + 'frontal.png'
        self.rib_r_t10 = folder + 'frontal.png'
        self.rib_l_t10 = folder + 'frontal.png'
        #   Floating
        self.rib_r_t11 = folder + 'frontal.png'
        self.rib_l_t11 = folder + 'frontal.png'
        self.rib_r_t12 = folder + 'frontal.png'
        self.rib_l_t12 = folder + 'frontal.png'

        """     Vertebrae   """
        #   Cervical
        self.c1 = folder + 'frontal.png'
        self.c2 = folder + 'frontal.png'
        self.c3 = folder + 'frontal.png'
        self.c4 = folder + 'frontal.png'
        self.c5 = folder + 'frontal.png'
        self.c6 = folder + 'frontal.png'
        self.c7 = folder + 'frontal.png'
        #   Lumbar
        self.l1 = folder + 'frontal.png'
        self.l2 = folder + 'frontal.png'
        self.l3 = folder + 'frontal.png'
        self.l4 = folder + 'frontal.png'
        self.l5 = folder + 'frontal.png'
        #   Thoracic
        self.t1 = folder + 'frontal.png'
        self.t2 = folder + 'frontal.png'
        self.t3 = folder + 'frontal.png'
        self.t4 = folder + 'frontal.png'
        self.t5 = folder + 'frontal.png'
        self.t6 = folder + 'frontal.png'
        self.t7 = folder + 'frontal.png'
        self.t8 = folder + 'frontal.png'
        self.t9 = folder + 'frontal.png'
        self.t10 = folder + 'frontal.png'
        self.t11 = folder + 'frontal.png'
        self.t12 = folder + 'frontal.png'

        """     Shoulder    """
        self.r_omoplatae = folder + 'frontal.png'
        self.l_omoplatae = folder + 'frontal.png'
        self.r_clavicle = folder + 'frontal.png'
        self.l_clavicle = folder + 'frontal.png'

        """     Arms        """
        self.r_humerus = folder + 'frontal.png'
        self.l_humerus = folder + 'frontal.png'
        self.r_radius = folder + 'frontal.png'
        self.l_radius = folder + 'frontal.png'
        self.r_ulna = folder + 'frontal.png'
        self.l_ulna = folder + 'frontal.png'

        """     Hands       """
        #   Carpals
        """
                Nomenclature
                    First letter of left/right + _ + Carpal
        """
        self.r_scaphoid = folder + 'frontal.png'
        self.l_scaphoid = folder + 'frontal.png'
        self.r_lunate = folder + 'frontal.png'
        self.l_lunate = folder + 'frontal.png'
        self.r_triquetrum = folder + 'frontal.png'
        self.l_triquetrum = folder + 'frontal.png'
        self.r_pisiform = folder + 'frontal.png'
        self.l_pisiform = folder + 'frontal.png'
        self.r_trapezium = folder + 'frontal.png'
        self.l_trapezium = folder + 'frontal.png'
        self.r_trapezoid = folder + 'frontal.png'
        self.l_trapezoid = folder + 'frontal.png'
        self.r_capitate = folder + 'frontal.png'
        self.l_capitate = folder + 'frontal.png'
        self.r_hamate = folder + 'frontal.png'
        self.l_hamate = folder + 'frontal.png'
        #   Metacarpals
        """
                Nomenclature
                    First letter of left/right + _ + Number + _ + Metacarpal
        """
        self.r_first_metacarpal = folder + 'frontal.png'
        self.l_first_metacarpal = folder + 'frontal.png'
        self.r_second_metacarpal = folder + 'frontal.png'
        self.l_second_metacarpal = folder + 'frontal.png'
        self.r_third_metacarpal = folder + 'frontal.png'
        self.l_third_metacarpal = folder + 'frontal.png'
        self.r_fourth_metacarpal = folder + 'frontal.png'
        self.l_fourth_metacarpal = folder + 'frontal.png'
        self.r_fifth_metacarpal = folder + 'frontal.png'
        self.l_fifth_metacarpal = folder + 'frontal.png'
        #   Phalanges
        """
        Nomenclature
            First letter of left/right + _ + First letter of the finger + _ + Proximal || Intermediate || Distal
        """
        #   Thumb
        self.r_t_phalanx_proximal = folder + 'frontal.png'
        self.l_t_phalanx_proximal = folder + 'frontal.png'
        self.r_t_phalanx_distal = folder + 'frontal.png'
        self.l_t_phalanx_distal = folder + 'frontal.png'
        #   Index
        self.r_i_phalanx_proximal = folder + 'frontal.png'
        self.l_i_phalanx_proximal = folder + 'frontal.png'
        self.r_i_phalanx_intermediate = folder + 'frontal.png'
        self.l_i_phalanx_intermediate = folder + 'frontal.png'
        self.r_i_phalanx_distal = folder + 'frontal.png'
        self.l_i_phalanx_distal = folder + 'frontal.png'
        #   Middle
        self.r_m_phalanx_proximal = folder + 'frontal.png'
        self.l_m_phalanx_proximal = folder + 'frontal.png'
        self.r_m_phalanx_intermediate = folder + 'frontal.png'
        self.l_m_phalanx_intermediate = folder + 'frontal.png'
        self.r_m_phalanx_distal = folder + 'frontal.png'
        self.l_m_phalanx_distal = folder + 'frontal.png'
        #   Ring
        self.r_r_phalanx_proximal = folder + 'frontal.png'
        self.l_r_phalanx_proximal = folder + 'frontal.png'
        self.r_r_phalanx_intermediate = folder + 'frontal.png'
        self.l_r_phalanx_intermediate = folder + 'frontal.png'
        self.r_r_phalanx_distal = folder + 'frontal.png'
        self.l_r_phalanx_distal = folder + 'frontal.png'
        #   Pinky
        self.r_p_phalanx_proximal = folder + 'frontal.png'
        self.l_p_phalanx_proximal = folder + 'frontal.png'
        self.r_p_phalanx_intermediate = folder + 'frontal.png'
        self.l_p_phalanx_intermediate = folder + 'frontal.png'
        self.r_p_phalanx_distal = folder + 'frontal.png'
        self.l_p_phalanx_distal = folder + 'frontal.png'

        """     Pelvis      """
        self.sacrum = folder + 'frontal.png'
        self.coccyx = folder + 'frontal.png'
        self.r_hip = folder + 'frontal.png'
        self.l_hip = folder + 'frontal.png'

        """     Legs        """
        self.r_femur = folder + 'frontal.png'
        self.l_femur = folder + 'frontal.png'
        self.r_patella = folder + 'frontal.png'
        self.l_patella = folder + 'frontal.png'
        self.r_tibia = folder + 'frontal.png'
        self.l_tibia = folder + 'frontal.png'
        self.r_fibula = folder + 'frontal.png'
        self.l_fibula = folder + 'frontal.png'

        """     Foot        """
        #   Metatarsal
        self.r_first_metatarsal = folder + 'frontal.png'
        self.l_first_metatarsal = folder + 'frontal.png'
        self.r_second_metatarsal = folder + 'frontal.png'
        self.l_second_metatarsal = folder + 'frontal.png'
        self.r_third_metatarsal = folder + 'frontal.png'
        self.l_third_metatarsal = folder + 'frontal.png'
        self.r_fourth_metatarsal = folder + 'frontal.png'
        self.l_fourth_metatarsal = folder + 'frontal.png'
        self.r_fifth_metatarsal = folder + 'frontal.png'
        self.l_fifth_metatarsal = folder + 'frontal.png'
        #   Tarsal
        self.r_calcaneus = folder + 'frontal.png'
        self.l_calcaneus = folder + 'frontal.png'
        self.r_talus = folder + 'frontal.png'
        self.l_talus = folder + 'frontal.png'
        self.r_navicular = folder + 'frontal.png'
        self.l_navicular = folder + 'frontal.png'
        self.r_medial_cuneiform = folder + 'frontal.png'
        self.l_medial_cuneiform = folder + 'frontal.png'
        self.r_intermediate_cuneiform = folder + 'frontal.png'
        self.l_intermediate_cuneiform = folder + 'frontal.png'
        self.r_lateral_cuneiform = folder + 'frontal.png'
        self.l_lateral_cuneiform = folder + 'frontal.png'
        self.r_cuboid = folder + 'frontal.png'
        self.l_cuboid = folder + 'frontal.png'
        #   Phalanges
        """
                Nomenclature
                    First letter of left/right + _ Toe number + _ + Proximal || Intermediate
        """
        #   First
        self.r_1_phalanx_proximal = folder + 'frontal.png'
        self.l_1_phalanx_proximal = folder + 'frontal.png'
        self.r_1_phalanx_distal = folder + 'frontal.png'
        self.l_1_phalanx_distal = folder + 'frontal.png'
        #   Second
        self.r_2_phalanx_proximal = folder + 'frontal.png'
        self.l_2_phalanx_proximal = folder + 'frontal.png'
        self.r_2_phalanx_intermediate = folder + 'frontal.png'
        self.l_2_phalanx_intermediate = folder + 'frontal.png'
        self.r_2_phalanx_distal = folder + 'frontal.png'
        self.l_2_phalanx_distal = folder + 'frontal.png'
        #   Third
        self.r_3_phalanx_proximal = folder + 'frontal.png'
        self.l_3_phalanx_proximal = folder + 'frontal.png'
        self.r_3_phalanx_intermediate = folder + 'frontal.png'
        self.l_3_phalanx_intermediate = folder + 'frontal.png'
        self.r_3_phalanx_distal = folder + 'frontal.png'
        self.l_3_phalanx_distal = folder + 'frontal.png'
        #   Fourth
        self.r_4_phalanx_proximal = folder + 'frontal.png'
        self.l_4_phalanx_proximal = folder + 'frontal.png'
        self.r_4_phalanx_intermediate = folder + 'frontal.png'
        self.l_4_phalanx_intermediate = folder + 'frontal.png'
        self.r_4_phalanx_distal = folder + 'frontal.png'
        self.l_4_phalanx_distal = folder + 'frontal.png'
        #   Fifth
        self.r_5_phalanx_proximal = folder + 'frontal.png'
        self.l_5_phalanx_proximal = folder + 'frontal.png'
        self.r_5_phalanx_intermediate = folder + 'frontal.png'
        self.l_5_phalanx_intermediate = folder + 'frontal.png'
        self.r_5_phalanx_distal = folder + 'frontal.png'
        self.l_5_phalanx_distal = folder + 'frontal.png'
